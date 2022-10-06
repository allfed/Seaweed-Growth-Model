"""
This file is meant to take the clustered and processed output of the seaweed model
and make the appropriate plots
"""
import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geoplot as gplt
from shapely.geometry import Point


def cluster_timeseries(growth_df):
    """
    Plots the clusters that were found in postprocessing
    The plot is seperated by clusters and the median growth rate is plotted
    """
    fig, axes = plt.subplots(nrows=3, ncols=2, sharey=True, sharex=True, figsize=(15, 15))

    axes = axes.flatten()
    for cluster, cluster_df in growth_df.groupby("cluster"):
        del (cluster_df["cluster"])
        ax = axes[cluster]
        cluster_df.transpose().plot(ax=ax, color="lightgrey", legend=False)
        cluster_df.median().transpose().plot(ax=ax, color="green", legend=False)
        ax.set_ylabel("Fraction Optimal")
        ax.set_xlabel("Months since war")
        ax.set_title("Cluster: " + str(cluster) + ", n: " + str(cluster_df.shape[0]))
    plt.savefig(
        "results" + os.sep + "grid" + os.sep + "cluster_timeseries.png",
        dpi=200, bbox_inches="tight")

    plt.close()


def cluster_spatial(growth_df, global_or_US):
    """
    Creates a spatial plot of the clusters
    """
    global_map = gpd.read_file(
        "data/geospatial_information/world_map/ne_10m_admin_0_countries.shp")
    growth_df.set_crs(epsg=4326, inplace=True)
    growth_df.to_crs(global_map.crs, inplace=True)
    growth_df["cluster"] = growth_df["cluster"].astype(str)
    ax = gplt.voronoi(growth_df, hue="cluster", legend=True, linewidth=0.3)
    fig = plt.gcf()
    fig.set_size_inches(15, 15)
    global_map.plot(ax=ax, color="white", edgecolor="black")
    if global_or_US == "US":
        ax.set_ylim(18, 55)
        ax.set_xlim(-130, -65)
    plt.savefig(
        "results" + os.sep + "grid" + os.sep + "cluster_spatial.png", dpi=200, bbox_inches="tight")


def prepare_geometry(growth_df):
    """
    Prepares the geometry for the growth_df. For some reason the spatial data has
    a longitude that is 0-360 instead of -180 to 180. This function converts it to
    the latter
    """
    growth_df["latlon"] = growth_df.index
    growth_df['latitude'] = growth_df["latlon"].str[0]
    growth_df['longitude'] = growth_df['latlon'].str[1]
    growth_df['longitude'] = growth_df[growth_df["longitude"] > 180]["longitude"] - 360
    growth_df["geometry"] = growth_df[['longitude', 'latitude']].apply(tuple, axis=1)
    growth_df["geometry"] = growth_df["geometry"].apply(Point)
    growth_df = growth_df[["cluster", "geometry"]]
    growth_df = gpd.GeoDataFrame(growth_df)
    return growth_df


if __name__ == "__main__":
    # Either calculate for the whole world or just the US
    global_or_US = "US"
    if global_or_US == "US":
        growth_df = gpd.GeoDataFrame(
            pd.read_pickle(
                "data" + os.sep + "interim_results" + os.sep + "growth_df_clustered.pkl"))
        cluster_timeseries(growth_df)
        growth_df = prepare_geometry(growth_df)
        cluster_spatial(growth_df, global_or_US)
