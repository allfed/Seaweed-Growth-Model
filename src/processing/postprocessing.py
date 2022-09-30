"""
This file takes the output of the seaweed model and does time series analysis with it
"""
import os
from src.model.seaweed_model import SeaweedModel
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


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


def time_series_analysis(growth_df):
    """
    Does time series analysis on the dataframe
    All the time serieses are clustered based on their
    overall shape using k-means
    Inspired by this article:
    https://www.kaggle.com/code/izzettunc/introduction-to-time-series-clustering/notebook
    Arguments:
        growth_df: pandas.DataFrame
    Returns:
        clustered growth_df: pandas.DataFrame
    """
    pass


if __name__ == "__main__":
    # Either calculate for the whole world or just the US
    global_or_US = "US"
    # only run this if the file does not exist
    if not os.path.isfile("data" + os.sep + "temporary_files" + os.sep + "growth_df.pkl"):
        parameter = "seaweed_growth_rate"
        path = "data" + os.sep + "temporary_files"
        file = "data_gridded_all_parameters.pkl"
        growth_df = get_parameter_dataframe(parameter, path, file)
        growth_df.to_pickle("data" + os.sep + "temporary_files" + os.sep + "growth_df.pkl")
    else:
        growth_df = pd.read_pickle("data" + os.sep + "temporary_files" + os.sep + "growth_df.pkl")
    # Do the time series analysis
    # only run this if the file does not exist
    if not os.path.isfile("data" + os.sep + "temporary_files" + os.sep + "clustered_growth_df.pkl"):
        clustered_growth_df = time_series_analysis(growth_df)
        clustered_growth_df.to_pickle("data" + os.sep + "temporary_files" + os.sep + "clustered_growth_df.pkl")
    else:
        clustered_growth_df = pd.read_pickle("data" + os.sep + "temporary_files" + os.sep + "clustered_growth_df.pkl")

    
