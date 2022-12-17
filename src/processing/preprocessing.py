"""
This files contains code to make the data ready for the model
"""
import os
import pickle

import pandas as pd
import xarray as xr


def get_area(path, file):
    """
    Gets the file with all the areas for grid_cells and saves it as a csv
    Arguments:
        path: path to the file
        file: filename
    Returns:
        None
    """
    data_set = xr.open_mfdataset(path + file)
    area = data_set["TAREA"][0, :, :]
    area = area.to_dataframe()
    # convert from cm² to km²
    area["TAREA"] = area["TAREA"] / 1e10
    area = area.reset_index()
    area = area.set_index(["TLONG", "TLAT"])
    area = area["TAREA"].to_frame()
    area.to_csv("area_grid.csv", sep=";")


def prepare_gridded_data(path, folder, scenario, file_ending, global_or_US):
    """
    Reads in the pickles of the geodataframes of the
    different environmental paramters. Checks if they
    all have the same geometry and reorders them to fit
    the rest of the code.
    Arguments:
        path: the path for the pickled files
        folder: the folder where the pickled files are
        file_ending: the ending of the pickled files
        global_or_US: if "global", the global data is used
        scenario: the scenario to use (e.g. 150tg)
    Returns:
        None, but saves a pickle of the dictionary of geo
        dataframes. Each geodataframe is assigned a key
        consisting of a tuple of floats of the latitude
        and longitude.
    """
    # Read in all the geopandas dataframes for the environmental parameters
    env_params = {
        "NO3": "nitrate",
        "NH4": "ammonium",
        "PAR_avg": "illumination",
        "PO4": "phosphate",
        "SALT": "salinity",
        "TEMP": "temperature",
        "Fe": "iron",
    }
    dict_env_dfs = {}
    for science_name in env_params.keys():
        full_path = (
            path + os.sep + "data" + os.sep + folder + os.sep + scenario + os.sep
        )
        env_df = pd.read_pickle(
            full_path + "nw_" + science_name + "_" + file_ending + ".pkl"
        )
        env_df.reset_index(inplace=True)
        env_df.columns = ["time", "TLONG", "TLAT", env_params[science_name]]
        dict_env_dfs[science_name] = env_df
    # Create all the groupby objects
    dict_env_dfs_grouped = {
        env_param: dict_env_dfs[env_param].groupby(["TLAT", "TLONG"])
        for env_param in env_params.keys()
    }
    data_dict = {}
    # Itereate over all the lat_lon combos, those are the same for all environmental parameters
    for lat_lon in dict_env_dfs_grouped["NO3"].groups.keys():
        list_env_param_latlon_df = []
        for env_param in env_params.keys():
            env_param_latlon_df = dict_env_dfs_grouped[env_param].get_group(lat_lon)
            env_param_latlon_df.set_index("time", inplace=True)
            # Add some fixes to the data, as some of them go slightly out of bounds
            # This is happening due to the way the climate model works
            if env_param == "NO3":
                env_param_latlon_df.loc[
                    env_param_latlon_df["nitrate"] < 0, "nitrate"
                ] = 0
            elif env_param == "NH4":
                env_param_latlon_df.loc[
                    env_param_latlon_df["ammonium"] < 0, "ammonium"
                ] = 0
            elif env_param == "PO4":
                env_param_latlon_df.loc[
                    env_param_latlon_df["phosphate"] < 0, "phosphate"
                ] = 0
            list_env_param_latlon_df.append(pd.DataFrame(env_param_latlon_df))
        concat_latlon_dfs = pd.concat(list_env_param_latlon_df, axis=1)
        # Remove duplicate columns
        concat_latlon_dfs = concat_latlon_dfs.loc[
            :, ~concat_latlon_dfs.columns.duplicated()
        ].copy()
        # Add a column with the month since war. This replaces the
        # time column, which only contains arbitrary numbers and not real dates
        concat_latlon_dfs["months_since_war"] = list(
            range(-4, concat_latlon_dfs.shape[0] - 4, 1)
        )
        # Convert back to geodataframe before saving
        data_dict[lat_lon] = concat_latlon_dfs
    # Make pickle out of it, so we don't have to run this every time
    full_path = path + os.sep + "data" + os.sep + "interim_data" + os.sep + scenario
    with open(
        full_path + os.sep + "data_gridded_all_parameters_" + global_or_US + ".pkl",
        "wb",
    ) as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    # Iterate over all scenarios
    for scenario in [str(i) + "tg" for i in [5, 16, 27, 37, 47, 150]]:
        print("Preparing scenario: " + scenario)
        prepare_gridded_data(
            ".", "gridded_data_global", scenario, "120_months_" + scenario, "global"
        )
    # Also prepare the test dataset with only the US
    prepare_gridded_data(
        ".", "gridded_data_test_dataset_US_only", "150tg", "36_months_150tg", "US"
    )
    # Prepare the control run
    prepare_gridded_data(
        ".", "gridded_data_global", "control", "120_months_control", "global"
    )
