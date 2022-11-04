"""
This file is meant to take the clustered and processed output of the seaweed model
and make the appropriate plots
"""
import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geoplot as gplt
from shapely.geometry import Point
import numpy as np
plt.style.use("https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle")


def cluster_spatial_voronoi(growth_df, global_or_US):
    """
    Creates a spatial plot of the clusters
    """
    global_map = gpd.read_file(
        "data/geospatial_information/Countries/ne_50m_admin_0_countries.shp"
    )
    growth_df.set_crs(epsg=4326, inplace=True)
    growth_df.to_crs(global_map.crs, inplace=True)
    growth_df["cluster"] = growth_df["cluster"].astype(str)
    # # Make sure that each entry has a value
    num_nan = growth_df.isna().sum().sum()
    assert num_nan == 0, "The dataframe has {} nan".format(num_nan)
    ax = gplt.voronoi(growth_df.dropna(), hue="cluster", legend=True, linewidth=0.3, cmap="viridis")
    fig = plt.gcf()
    fig.set_size_inches(15, 15)
    global_map.plot(ax=ax, color="white", edgecolor="black")
    if global_or_US == "US":
        ax.set_ylim(18, 55)
        ax.set_xlim(-130, -65)
    plt.savefig(
        "results" + os.sep + "grid" + os.sep + "cluster_spatial_" + global_or_US + ".png",
        dpi=350,
        bbox_inches="tight",
    )


def prepare_geometry(growth_df):
    """
    Prepares the geometry for the growth_df. For some reason the spatial data has
    a longitude that is 0-360 instead of -180 to 180. This function converts it to
    the latter
    """
    growth_df["latlon"] = growth_df.index
    growth_df["latitude"] = growth_df["latlon"].str[0]
    growth_df["longitude"] = growth_df["latlon"].str[1]
    growth_df["longitude"] = growth_df["longitude"].apply(lambda x: x - 360 if x > 180 else x)
    growth_df["geometry"] = growth_df[["longitude", "latitude"]].apply(tuple, axis=1)
    growth_df["geometry"] = growth_df["geometry"].apply(Point)
    growth_df = growth_df[["cluster", "geometry"]]
    growth_df = gpd.GeoDataFrame(growth_df)
    return growth_df


def cluster_timeseries_all_parameters_q_lines(parameters, global_or_US):
    """
    Plots line plots for all clusters and all parameters
    Arguments:
        parameters: a dictionary of dataframes of all parameters
    Returns:
        None, but saves the plot
    """
    clusters = 5 if global_or_US == "US" else 4
    fig, axes = plt.subplots(
        nrows=5, ncols=clusters, sharey=True, sharex=True, figsize=(20, 20)
    )
    i = 0
    for parameter, parameter_df in parameters.items():
        j = 0
        for cluster, cluster_df in parameter_df.groupby("cluster"):
            del cluster_df["cluster"]
            ax = axes[i, j]

            for q in np.arange(0.1, 0.6, 0.1):
                q_up = cluster_df.quantile(1 - q)
                q_down = cluster_df.quantile(q)
                ax.fill_between(
                    x=q_up.index.astype(float), y1=q_down, y2=q_up, color="#3A913F", alpha=q * 2
                )
            ax.plot(cluster_df.median(), color="black")
            if j == 0:
                ax.set_ylabel(parameter)
            if (i == 4 and global_or_US == "US") or (i == 3 and global_or_US == "global"):
                ax.set_xlabel("Months since war")
            if i == 0:
                ax.set_title("Cluster: " + str(cluster) + ", n: " + str(cluster_df.shape[0]))
            # Add a legend
            if j == 0 and i == 0:
                # Create the legend
                patches_list = []
                patches_list.append(mpatches.Patch(color="black", label="Median"))
                patches_list.append(mpatches.Patch(color="#3A913F", label="Q40 - Q60", alpha=0.8))
                patches_list.append(mpatches.Patch(color="#3A913F", label="Q30 - Q70", alpha=0.6))
                patches_list.append(mpatches.Patch(color="#3A913F", label="Q20 - Q80", alpha=0.4))
                patches_list.append(mpatches.Patch(color="#3A913F", label="Q10 - Q90", alpha=0.2))
                ax.legend(handles=patches_list)
            j += 1
        i += 1
    plt.savefig(
        "results" + os.sep + "grid" + os.sep + "cluster_timeseries_all_param_q_lines_"
        + global_or_US + ".png",
        dpi=350,
        bbox_inches="tight",
    )
    plt.close()


if __name__ == "__main__":
    # Either calculate for the whole world or just the US
    global_or_US = "US"
    growth_df = gpd.GeoDataFrame(
        pd.read_pickle(
            "data" + os.sep + "interim_results" + os.sep
            + "seaweed_growth_rate_clustered_" + global_or_US + ".pkl"
        )
    )
    # Add one to the cluster
    growth_df["cluster"] = growth_df["cluster"] + 1
    # Make sure that each entry has a value
    num_nan = growth_df.isna().sum().sum()
    assert num_nan == 0, "The dataframe has {} nan".format(num_nan)
    cluster_timeseries_only_growth(growth_df, global_or_US)
    growth_df = prepare_geometry(growth_df)
    cluster_spatial_voronoi(growth_df, global_or_US)
    parameters = {}
    parameter_names = [
        "salinity_factor", "nutrient_factor",
        "illumination_factor", "temp_factor", "seaweed_growth_rate"
    ]
    for parameter in parameter_names:
        parameters[parameter] = pd.DataFrame(
            pd.read_pickle(
                "data" + os.sep + "interim_results" + os.sep
                + parameter + "_clustered_" + global_or_US + ".pkl"
            )
        # Add one to the cluster
        parameters[parameter]["cluster"] = parameters[parameter]["cluster"] + 1
        )
    cluster_timeseries_all_parameters_individual_lines(parameters, global_or_US)
    cluster_timeseries_all_parameters_q_lines(parameters, global_or_US)
