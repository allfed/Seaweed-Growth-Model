"""
This files contains a collection of functions that are used in the main file,
but are not directly related to the main functionality of the program.
"""
import geopandas as gpd
from shapely.geometry import Point


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
