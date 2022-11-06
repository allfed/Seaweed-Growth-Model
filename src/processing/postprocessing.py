"""
This file takes the output of the seaweed model and does time series analysis with it
"""
import os
import numpy as np
import random
from src.model.seaweed_model import SeaweedModel
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tslearn.clustering import TimeSeriesKMeans
from tslearn.utils import to_time_series_dataset


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
    # define the cores
    cores = None if global_or_US == "US" else -1
    km = TimeSeriesKMeans(n_clusters=n_clusters, metric="dtw", n_jobs=cores)
    timeseries_ds = to_time_series_dataset(growth_df_scaled)
    labels = km.fit_predict(timeseries_ds)
    return labels, km


def elbow_method(growth_df, max_clusters, global_or_US):
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
    for i in range(1, max_clusters):
        print("Trying {} clusters".format(i))
        labels, km = time_series_analysis(growth_df, i)
        inertias[i] = km.inertia_
    inertias_df = pd.DataFrame.from_dict(inertias, orient="index")
    inertias_df.to_csv(
        "data"
        + os.sep
        + "interim_results"
        + os.sep
        + "inertias"
        + global_or_US
        + ".csv",
        sep=";",
    )
    ax = inertias_df.plot()
    ax.set_xlabel("Number of clusters")
    ax.set_ylabel("Distortion")
    ax.set_title("Elbow method")
    ax.get_figure().savefig(
        "data"
        + os.sep
        + "interim_results"
        + os.sep
        + "elbow_method"
        + global_or_US
        + ".png"
    )


if __name__ == "__main__":
    # Either calculate for the whole world or just the US
    global_or_US = "global"
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
        + "interim_results"
        + os.sep
        + "seaweed_growth_rate_"
        + global_or_US
        + ".pkl"
    ):
        print("Creating the dataframe")
        path = "data" + os.sep + "interim_results"
        file = "data_gridded_all_parameters_" + global_or_US + ".pkl"
        # Transpose the dataframe so that the time serieses are the columns
        # Get all the parameters
        for parameter in parameters:
            print("Getting parameter {}".format(parameter))
            growth_df = get_parameter_dataframe(parameter, path, file).transpose()
            growth_df.to_pickle(
                "data"
                + os.sep
                + "interim_results"
                + os.sep
                + parameter
                + "_"
                + global_or_US
                + ".pkl"
            )

    # Do the time series analysis
    # growth_df = pd.read_pickle(
    #     "data" + os.sep + "interim_results" + os.sep
    #     + "seaweed_growth_rate_" + global_or_US + ".pkl"
    # )
    # elbow_method(growth_df, 15, global_or_US)
    # elbow method says 5 is the optimal number of clusters for US
    # and 4 for the whole world
    number_of_clusters = 4 if global_or_US == "global" else 5
    if not os.path.isfile(
        "data"
        + os.sep
        + "interim_results"
        + os.sep
        + "seaweed_growth_rate_clustered_"
        + global_or_US
        + ".pkl"
    ):
        print("Clustering the data")
        growth_df = pd.read_pickle(
            "data"
            + os.sep
            + "interim_results"
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
                + "interim_results"
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
                + "interim_results"
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
            + "interim_results"
            + os.sep
            + "seaweed_growth_rate_clustered_"
            + global_or_US
            + ".pkl"
        )
