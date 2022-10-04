"""
This file takes the output of the seaweed model and does time series analysis with it
"""
import os
from src.model.seaweed_model import SeaweedModel
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tslearn.clustering import TimeSeriesKMeans
from tslearn.utils import to_time_series_dataset


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


def time_series_analysis(growth_df, n_clusters):
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
        scaler.fit_transform(growth_df), columns=growth_df.columns)
    # A good rule of thumb is choosing k as the square root of the number
    # of points in the training data set in kNN
    km = TimeSeriesKMeans(n_clusters=n_clusters, metric="dtw")
    timeseries_ds = to_time_series_dataset(growth_df_scaled)
    labels = km.fit_predict(timeseries_ds)
    return labels, km


def elbow_method(growth_df, max_clusters):
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
        "data" + os.sep + "interim_results" + os.sep + "inertias.csv",
        sep=";",)
    ax = inertias_df.plot()
    ax.set_xlabel("Number of clusters")
    ax.set_ylabel("Distortion")
    ax.set_title("Elbow method")
    ax.get_figure().savefig(
        "data" + os.sep + "interim_results" + os.sep + "elbow_method.png")


if __name__ == "__main__":
    # Either calculate for the whole world or just the US
    global_or_US = "US"
    if global_or_US == "US":
        # only run this if the file does not exist
        if not os.path.isfile("data" + os.sep + "interim_results" + os.sep + "growth_df.pkl"):
            parameter = "seaweed_growth_rate"
            path = "data" + os.sep + "interim_results"
            file = "data_gridded_all_parameters.pkl"
            # Transpose the dataframe so that the time serieses are the columns
            growth_df = get_parameter_dataframe(parameter, path, file).transpose()
            growth_df.to_pickle("data" + os.sep + "interim_results" + os.sep + "growth_df.pkl")
        else:
            growth_df = pd.read_pickle(
                "data" + os.sep + "interim_results" + os.sep + "growth_df.pkl")
        # Do the time series analysis
        # elbow_method(growth_df, 50)
        # elbow method says 5 is the optimal number of clusters
        if not os.path.isfile(
            "data" + os.sep + "interim_results" + os.sep + "growth_df_clustered.pkl"):
            labels, km = time_series_analysis(growth_df, 5)
            growth_df["cluster"] = labels
            growth_df.to_pickle(
                "data" + os.sep + "interim_results" + os.sep + "growth_df_clustered.pkl")
        else:
            growth_df = pd.read_pickle(
                "data" + os.sep + "interim_results" + os.sep + "growth_df_clustered.pkl")
