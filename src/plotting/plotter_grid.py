"""
This file is meant to take the clustered and processed output of the seaweed model
and make the appropriate plots
"""
import os

import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Point

plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)


def cluster_spatial(growth_df, global_or_US, scenario):
    """
    Creates a spatial plot of the clusters
    Arguments:
        growth_df: a dataframe of the growth rate
        global_or_US: a string of either "global" or "US" that indicates the scale
    Returns:
        None, but saves the plot
    """
    global_map = gpd.read_file(
        "data/geospatial_information/Countries/ne_50m_admin_0_countries.shp"
    )
    growth_df.set_crs(epsg=4326, inplace=True)
    growth_df.to_crs(global_map.crs, inplace=True)
    growth_df["cluster"] = growth_df["cluster"].astype(str)
    ax = growth_df.plot(column="cluster", legend=True, cmap="viridis")
    fig = plt.gcf()
    fig.set_size_inches(12, 12)
    global_map.plot(ax=ax, color="lightgrey", edgecolor="black", linewidth=0.2)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.get_legend().set_title("Cluster")
    if global_or_US == "US":
        ax.set_ylim(18, 55)
        ax.set_xlim(-130, -65)
    else:
        ax.set_ylim(-75, 85)
        ax.set_xlim(-180, 180)
    plt.savefig(
        "results"
        + os.sep
        + "grid"
        + os.sep
        + scenario
        + os.sep
        + "cluster_spatial_"
        + global_or_US
        + ".png",
        dpi=350,
        bbox_inches="tight",
    )


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
    growth_df = growth_df[["cluster", "geometry"]]
    growth_df = gpd.GeoDataFrame(growth_df)
    return growth_df


def cluster_timeseries_all_parameters_q_lines(parameters, global_or_US, scenario):
    """
    Plots line plots for all clusters and all parameters
    Arguments:
        parameters: a dictionary of dataframes of all parameters
    Returns:
        None, but saves the plot
    """
    # Make the labels more clear
    parameter_names = {
        "salinity_factor": "Salinity Factor",
        "nutrient_factor": "Nutrient Factor",
        "illumination_factor": "Illumination Factor",
        "temp_factor": "Temperature Factor",
        "seaweed_growth_rate": "Seaweed Growth Rate",
    }
    clusters = 4 if global_or_US == "US" else 3
    fig, axes = plt.subplots(
        nrows=5, ncols=clusters, sharey=True, sharex=True, figsize=(12, 12)
    )
    i = 0
    # Iterate over all parameters and cluster to make all the subplots
    for parameter, parameter_df in parameters.items():
        j = 0
        for cluster, cluster_df in parameter_df.groupby("cluster"):
            del cluster_df["cluster"]
            ax = axes[i, j]
            for q in np.arange(0.1, 0.6, 0.1):
                q_up = cluster_df.quantile(1 - q)
                q_down = cluster_df.quantile(q)
                ax.fill_between(
                    x=q_up.index.astype(float),
                    y1=q_down,
                    y2=q_up,
                    color="#3A913F",
                    # Make the color more transparent with each quantile
                    alpha=q * 2,
                )
            ax.plot(cluster_df.median(), color="black")
            # Labels
            if j == 0:
                ax.set_ylabel(parameter_names[parameter])
            if i == 4:
                ax.set_xlabel("Months since nuclear war")
            if i == 0:
                ax.set_title(
                    "Cluster: " + str(cluster) + ", n: " + str(cluster_df.shape[0])
                )
            # Add a legend
            if j == 0 and i == 0:
                # Create the legend
                patches_list = []
                patches_list.append(mpatches.Patch(color="black", label="Median"))
                patches_list.append(
                    mpatches.Patch(color="#3A913F", label="Q40 - Q60", alpha=0.8)
                )
                patches_list.append(
                    mpatches.Patch(color="#3A913F", label="Q30 - Q70", alpha=0.6)
                )
                patches_list.append(
                    mpatches.Patch(color="#3A913F", label="Q20 - Q80", alpha=0.4)
                )
                patches_list.append(
                    mpatches.Patch(color="#3A913F", label="Q10 - Q90", alpha=0.2)
                )
                ax.legend(handles=patches_list)
            j += 1
        i += 1
    plt.savefig(
        "results"
        + os.sep
        + "grid"
        + os.sep
        + scenario
        + os.sep
        + "cluster_timeseries_all_param_q_lines_"
        + global_or_US
        + ".png",
        dpi=350,
        bbox_inches="tight",
    )
    plt.close()


def main(scenario, global_or_US):
    """
    Runs the other functions to read the data and make the plots
    Arguments:
        None
    Returns:
        None
    """
    growth_df = gpd.GeoDataFrame(
        pd.read_pickle(
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
    )
    # Add one to the cluster
    growth_df["cluster"] = growth_df["cluster"] + 1
    # Make sure that each entry has a value
    num_nan = growth_df.isna().sum().sum()
    assert num_nan == 0, "The dataframe has {} nan".format(num_nan)
    # Fix the geometry
    growth_df = prepare_geometry(growth_df)
    cluster_spatial(growth_df, global_or_US, scenario)

    # Read in the other parameters for the line plot
    parameters = {}
    parameter_names = [
        "salinity_factor",
        "nutrient_factor",
        "illumination_factor",
        "temp_factor",
        "seaweed_growth_rate",
    ]
    for parameter in parameter_names:
        parameters[parameter] = pd.DataFrame(
            pd.read_pickle(
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
        )
        # Add one to the cluster
        parameters[parameter]["cluster"] = parameters[parameter]["cluster"] + 1

    cluster_timeseries_all_parameters_q_lines(parameters, global_or_US, scenario)


if __name__ == "__main__":
    main("150tg", "US")
    main("150tg", "global")
