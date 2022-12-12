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

from src.processing import read_files as rf
from src.processing import postprocessing as pp

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
    growth_df = growth_df[["cluster", "geometry"]]
    global_map = gpd.read_file(
        "data/geospatial_information/Countries/ne_50m_admin_0_countries.shp"
    )
    growth_df.set_crs(epsg=4326, inplace=True)
    growth_df.to_crs(global_map.crs, inplace=True)
    growth_df["cluster"] = growth_df["cluster"].astype(str)
    ax = growth_df.plot(column="cluster", legend=True, cmap="summer_r")
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
    growth_df = gpd.GeoDataFrame(growth_df)
    return growth_df


def growth_rate_spatial_by_year(growth_df, global_or_US, scenario):
    """
    Plots the growth rate by year. This includes the first
    three months without nuclear war, in the case of the first year
    Arguments:
        growth_df: a dataframe of the growth rate
    Returns:
        None, but saves the plot
    """
    global_map = gpd.read_file(
        "data/geospatial_information/Countries/ne_50m_admin_0_countries.shp"
    )
    for year, i in enumerate(np.arange(-4, len(growth_df.columns) - 10, 12)):
        # Calculate the mean growth rate per year
        growth_df_year = growth_df.loc[:, i + 1 : i + 12]
        growth_df_year = growth_df_year.mean(axis=1)
        growth_df_year = growth_df_year.to_frame()
        growth_df_year.columns = ["growth_rate"]
        # Multiply it by 60 to get the actual growth rate
        growth_df_year["growth_rate"] = growth_df_year["growth_rate"] * 60
        # Make it a geodataframe
        growth_df_year["geometry"] = growth_df["geometry"]
        growth_df_year = gpd.GeoDataFrame(growth_df_year)
        growth_df_year.set_crs(epsg=4326, inplace=True)
        growth_df_year.to_crs(global_map.crs, inplace=True)
        # Plot it
        ax = growth_df_year.plot(
            column="growth_rate",
            legend=True,
            cmap="viridis",
            vmin=0,
            vmax=45,
            legend_kwds={
                "label": "Mean Daily Growth Rate [%]",
                "orientation": "vertical",
            },
        )
        global_map.plot(ax=ax, color="lightgrey", edgecolor="black", linewidth=0.2)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_title("Year " + str(year + 1))
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
            + "growth_rate_spatial_year_"
            + str(year + 1)
            + "_"
            + global_or_US
            + ".png",
            dpi=350,
            bbox_inches="tight",
        )


def cluster_timeseries_all_parameters_q_lines(parameters, global_or_US, scenario, areas):
    """
    Plots line plots for all clusters and all parameters
    Arguments:
        parameters: a dictionary of dataframes of all parameters
    Returns:
        None, but saves the plot
    """
    # This is slightly larger than the actual area of the ocean due to the way the grid
    # is structured
    total_ocean_area = 361140210.2
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
            # Combine area and cluster into one dataframe, merge by index
            # Reset the index, so we can join on column instead of index
            areas_reset = areas.reset_index()
            cluster_df = cluster_df.reset_index()
            # ROund the level and lat lon values to 4 decimals to make sure they match
            # level just refers to the level of the multi index, but contains the same
            # information as the lat lon
            cluster_df["level_0"] = cluster_df["level_0"].round(4)
            cluster_df["level_1"] = cluster_df["level_1"].round(4)
            areas_reset["TLAT"] = areas_reset["TLAT"].round(4)
            areas_reset["TLONG"] = areas_reset["TLONG"].round(4)
            cluster_df = pd.merge(
                cluster_df, areas_reset, left_on=["level_0", "level_1"], right_on=["TLAT", "TLONG"]
            )
            # Calculate the area
            cluster_area = cluster_df["TAREA"].sum()
            # Remove the columsn we don't need anymore
            area_weights = cluster_df["TAREA"]
            cluster_df = cluster_df.drop(
                columns=["cluster", "TLAT", "TLONG", "level_0", "level_1", "TAREA"]
            )
            ax = axes[i, j]
            for q in np.arange(0.1, 0.6, 0.1):
                # Calculate the quantiles for each months, weighted by area
                q_up = cluster_df.apply(pp.weighted_quantile, args=(area_weights, 1 - q))
                q_down = cluster_df.apply(pp.weighted_quantile, args=(area_weights, q))
                # Transpose the dataframes so that the index is the month
                q_up = q_up.transpose()
                q_down = q_down.transpose()
                # Make the quantiles into a series, so that we can plot them
                q_up = pd.Series(q_up.iloc[:, 0])
                q_down = pd.Series(q_down.iloc[:, 0])
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
                    "Cluster: "
                    + str(cluster)
                    + ", "
                    + str(int(round(cluster_area / total_ocean_area * 100, 0)))
                    + "% of Ocean Area"
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


def compare_nw_scenarios(areas):
    """
    Compares the results of the nuclear war scenarios as weigthed median
    Arguments:
        None
    Returns:
        None
    """
    ax = plt.subplot(111)
    # Iterate over all scenarios and plot them in the same plot
    i = 1
    for scenario in [str(i) + "tg" for i in [150, 47, 37, 27, 16, 5]]:
        # Read the data
        growth_df_scenario = pd.read_pickle(
            "data"
            + os.sep
            + "interim_data"
            + os.sep
            + scenario
            + os.sep
            + "seaweed_growth_rate_global.pkl"
        )
        # Calculate the weighted median
        median = growth_df_scenario.apply(pp.weighted_quantile, args=(areas, 0.5))
        # Plot the median
        ax.plot(median, label=scenario, color="#3A913F", alpha=i)
        i -= 0.15
    plt.legend()
    plt.savefig(
        "results"
        + os.sep
        + "grid"
        + os.sep
        + "comparing_nw_scenarios.png",
        dpi=350,
        bbox_inches="tight",
    )


def main(scenario, global_or_US):
    """
    Runs the other functions to read the data and make the plots
    Arguments:
        None
    Returns:
        None
    """
    # Read the data
    areas = rf.read_area_file("data" + os.sep + "geospatial_information" + os.sep + "grid", "area_grid.csv")
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
    # Add one to the cluster to make it start at 1
    growth_df["cluster"] = growth_df["cluster"] + 1
    # Make sure that each entry has a value
    num_nan = growth_df.isna().sum().sum()
    assert num_nan == 0, "The dataframe has {} nan".format(num_nan)
    # Fix the geometry
    growth_df = prepare_geometry(growth_df)
    # Make the spatial plots
    #growth_rate_spatial_by_year(growth_df, global_or_US, scenario)
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

    cluster_timeseries_all_parameters_q_lines(parameters, global_or_US, scenario, areas)


if __name__ == "__main__":
    # main("150tg", "US")
    # Compare the nuclear war scenarios
    # Call this seperately, as it needs to access all scenarios
    areas = rf.read_area_file("data" + os.sep + "geospatial_information" + os.sep + "grid", "area_grid.csv")
    compare_nw_scenarios(areas)
    # Iterate over all scenarios
    # for scenario in [str(i) + "tg" for i in [5, 16, 27, 37, 47, 150]]:
    #     print("Preparing scenario: " + scenario)
    #     main(scenario, "global")
