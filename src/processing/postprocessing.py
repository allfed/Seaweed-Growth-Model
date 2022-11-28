"""
This file takes the output of the seaweed model and does time series analysis with it
"""
import os
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tslearn.clustering import TimeSeriesKMeans
from tslearn.utils import to_time_series_dataset

from src.model.seaweed_model import SeaweedModel

# Import the ALLFED stle
plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)

# Make sure that everything is reproducible
random.seed(42)
np.random.seed(42)


def get_parameter_dataframe(parameter, path, file):
    """
    Initializes the seaweed model and returns the dataframe with the parameter
    for all the grid sections
    Arguments:
        parameter: the parameter to construct the dataframe for
        path: The path to the file
        file: The file name
    Returns:
        df: pandas.DataFrame
    """
    model = SeaweedModel()
    model.add_data_by_grid(path + os.sep + file)
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    param_df = model.construct_df_for_parameter(parameter)
    return param_df


def time_series_analysis(growth_df, n_clusters, global_or_US):
    """
    Does time series analysis on the dataframe
    All the time serieses are clustered based on their
    overall shape using k-means
    Inspired by this article:
    https://www.kaggle.com/code/izzettunc/introduction-to-time-series-clustering/notebook
    Arguments:
        growth_df: pandas.DataFrame
        n_clusters: int - the number of clusters to use
    Returns:
        labels: list - the labels for each time series
        km: TimeSeriesKMeans - the k-means object
    """
    # Make sure that each entry has a value
    assert growth_df.notna().all().all(), "The dataframe has nan"
    # Normalize the data
    scaler = MinMaxScaler()
    growth_df_scaled = pd.DataFrame(
        scaler.fit_transform(growth_df), columns=growth_df.columns
    )
    # A good rule of thumb is choosing k as the square root of the number
    # of points in the training data set in kNN
    cores = None if global_or_US == "US" else -1  # define the cores to use
    km = TimeSeriesKMeans(n_clusters=n_clusters, metric="dtw", n_jobs=cores)
    timeseries_ds = to_time_series_dataset(growth_df_scaled)
    labels = km.fit_predict(timeseries_ds)
    return labels, km


def elbow_method(growth_df, max_clusters, global_or_US, scenario):
    """
    Finds the optimal number of clusters using the elbow method
    https://predictivehacks.com/k-means-elbow-method-code-for-python/
    Arguments:
        growth_df: pandas.DataFrame
        max_clusters: int - the maximum number of clusters to try
    Returns:
        None, just plots the elbow method and saves it
    """
    # Find the optimal number of clusters
    inertias = {}
    for i in range(2, max_clusters):
        print("Trying {} clusters".format(i))
        labels, km = time_series_analysis(growth_df, i, global_or_US)
        inertias[i] = km.inertia_
    inertias_df = pd.DataFrame.from_dict(inertias, orient="index")
    inertias_df.to_csv(
        "data"
        + os.sep
        + "interim_data"
        + os.sep
        + scenario
        + os.sep
        + "inertias_"
        + global_or_US
        + ".csv",
        sep=";",
    )
    ax = inertias_df.plot(legend=False)
    ax.set_xlabel("Number of clusters")
    ax.set_ylabel("Distortion")
    ax.set_title("Elbow method")
    ax.get_figure().savefig(
        "results"
        + os.sep
        + "elbow_plots"
        + os.sep
        + "elbow_method_"
        + global_or_US
        + "_"
        + scenario
        + ".png"
    )


def area_cap(lat, radius=6371.0):  # Earth radius in km
    """Area of a cap of radius r and latitude lat.

    Arguments:
        lat : float
            Latitude of the cap in degrees.
        radius : float, optional
            Radius of the sphere in km.
            Default is the radius of the Earth.

    Returns:
        area : float
            Area of the cap in km^2.
    """
    # convert to radians
    theta = lat / 180. * np.pi

    # area of a spherical cap (see Wikipedia)
    return 2 * np.pi * radius**2 * (1 - np.sin(theta))


@np.vectorize
def area_grid_cell(lat, radius=6371.0):  # Earth radius in km
    """Area of a grid cell on a sphere. The grid cell is assumed
    to 1 deg x 1 deg, aligned with the latitude and longitude.

    Arguments:
        lat : float or array_like
            Latitude of the grid cell in degrees.
        radius : float, optional
            Radius of the sphere in km.
            Default is the radius of the Earth.

    Returns:
        area : float
            Area of the grid cell in km^2.
    """
    # Don't pass latitudes outside the range [-90, 90]
    assert np.abs(lat) <= 90, "Latitude must be in the range [-90, 90]."

    # latitudes are capped at +/- 90 degrees
    lower_lat = max(lat - 0.5, -90.)
    upper_lat = min(lat + 0.5, 90.)

    # the area of the grid cell is the difference between the
    # area of the upper and lower cap divided by the number of
    # grid cells that you count if you walk around the globe
    # once along the latitude
    return (area_cap(lower_lat, radius=radius) - area_cap(upper_lat, radius=radius)) / 360.


def lme(scenario):
    """
    Calculates growth rate and all the factors for the lme
    and saves it in files appropriate for the plotting functions
    Arguments:
        None
    Returns:
        None
    """
    model = SeaweedModel()
    model.add_data_by_lme(
        [i for i in range(1, 67)],
        "data/lme_data/seaweed_environment_data_in_nuclear_war.csv",
    )
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    # Define the parameters we look at
    parameters = [
        "salinity_factor",
        "nutrient_factor",
        "illumination_factor",
        "temp_factor",
        "seaweed_growth_rate",
    ]
    # only run this if the file does not exist
    if not os.path.isfile(
        "data" + os.sep + "interim_data" + os.sep + "seaweed_growth_rate_LME.pkl"
    ):
        print("Creating the dataframe")
        # Transpose the dataframe so that the time serieses are the columns
        # Get all the parameters
        for parameter in parameters:
            print("Getting parameter {}".format(parameter))
            growth_df = model.construct_df_for_parameter(parameter).transpose()
            growth_df.to_pickle(
                "data"
                + os.sep
                + "interim_data"
                + os.sep
                + scenario
                + os.sep
                + parameter
                + "_LME.pkl"
            )


def grid(scenario, global_or_US, with_elbow_method=False):
    """
    Calculates growth rate and all the factors for the grid
    and saves it in files appropriate for the plotting functions
    Arguments:
        None
    Returns:
        None
    """
    # Define the parameters we look at
    parameters = [
        "salinity_factor",
        "nutrient_factor",
        "illumination_factor",
        "temp_factor",
        "seaweed_growth_rate",
    ]
    # only run this if the file does not exist
    if not os.path.isfile(
        "data"
        + os.sep
        + "interim_data"
        + os.sep
        + scenario
        + os.sep
        + "seaweed_growth_rate_"
        + global_or_US
        + ".pkl"
    ):
        print("Creating the dataframe")
        path = "data" + os.sep + "interim_data" + os.sep + scenario
        file = "data_gridded_all_parameters_" + global_or_US + ".pkl"
        # Transpose the dataframe so that the time serieses are the columns
        # Get all the parameters
        for parameter in parameters:
            print("Getting parameter {}".format(parameter))
            growth_df = get_parameter_dataframe(parameter, path, file).transpose()
            growth_df.to_pickle(
                "data"
                + os.sep
                + "interim_data"
                + os.sep
                + scenario
                + os.sep
                + parameter
                + "_"
                + global_or_US
                + ".pkl"
            )
    if with_elbow_method:
        # Do the time series analysis
        growth_df = pd.read_pickle(
            "data" + os.sep + "interim_data" + os.sep + scenario + os.sep
            + "seaweed_growth_rate_" + global_or_US + ".pkl"
        )
        elbow_method(growth_df, 7, global_or_US, scenario)
    # elbow method says 4 is the optimal number of clusters for US
    # and 3 for the whole world
    number_of_clusters = 3 if global_or_US == "global" else 4
    if not os.path.isfile(
        "data"
        + os.sep
        + "interim_data"
        + os.sep
        + scenario
        + os.sep
        + "seaweed_growth_rate_clustered_"
        + global_or_US
        + ".pkl"
    ):
        print("Clustering the data")
        growth_df = pd.read_pickle(
            "data"
            + os.sep
            + "interim_data"
            + os.sep
            + scenario
            + os.sep
            + "seaweed_growth_rate_"
            + global_or_US
            + ".pkl"
        )
        labels, km = time_series_analysis(growth_df, number_of_clusters, global_or_US)
        growth_df["cluster"] = labels
        for parameter in parameters:
            print("Getting parameter {} for clustering".format(parameter))
            param_df = pd.read_pickle(
                "data"
                + os.sep
                + "interim_data"
                + os.sep
                + scenario
                + os.sep
                + parameter
                + "_"
                + global_or_US
                + ".pkl"
            )
            param_df["cluster"] = labels
            param_df.to_pickle(
                "data"
                + os.sep
                + "interim_data"
                + os.sep
                + scenario
                + os.sep
                + parameter
                + "_clustered_"
                + global_or_US
                + ".pkl"
            )
    else:
        growth_df = pd.read_pickle(
            "data"
            + os.sep
            + "interim_data"
            + os.sep
            + scenario
            + os.sep
            + "seaweed_growth_rate_clustered_"
            + global_or_US
            + ".pkl"
        )


if __name__ == "__main__":
   # lme("150tg")
    grid("150tg", "US")
   # grid("150tg", "global")
