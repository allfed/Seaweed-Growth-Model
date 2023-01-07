"""
This files contains a collection of functions that are used in the main file,
but are not directly related to the main functionality of the program.
"""
import os

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from statsmodels.stats.weightstats import DescrStatsW


def prepare_geometry(growth_df):
    """
    Prepares the geometry for the growth_df. For some reason the spatial data has
    a longitude that is 0-360 instead of -180 to 180. This function converts it to
    the latter
    Arguments:
        growth_df: a dataframe of the growth rate
    Returns:
        None, but saves the plot
    """
    growth_df["latlon"] = growth_df.index
    growth_df["latitude"] = growth_df["latlon"].str[0]
    growth_df["longitude"] = growth_df["latlon"].str[1]
    growth_df["longitude"] = growth_df["longitude"].apply(
        lambda x: x - 360 if x > 180 else x
    )
    growth_df["geometry"] = (
        growth_df[["longitude", "latitude"]].apply(tuple, axis=1).apply(Point)
    )
    growth_df = gpd.GeoDataFrame(growth_df)
    growth_df = growth_df.set_crs("EPSG:4326")
    return growth_df


def weighted_quantile(data: pd.Series, weights: pd.Series, quantile: float) -> float:
    """
    Calculates the weighted quantile of s1 based on s2
    Arguments:
        data: pandas.Series - the series to calculate the quantile for
        weights: pandas.Series - the series to use as weights
        quantile: float - the quantile to calculate
    Returns:
        float - the weighted quantile
    """
    # Ensure that s1 and s2 have the same length
    assert len(data) == len(weights), "The input series must have the same length"

    # Ensure that the quantile is between 0 and 1
    assert isinstance(quantile, float), "The quantile must be a float"
    assert 0 <= quantile <= 1, "The quantile must be between 0 and 1"
    # Calculate the weighted quantile
    wq = DescrStatsW(data=data, weights=weights)
    quantile = wq.quantile(probs=quantile, return_pandas=False)
    return quantile
