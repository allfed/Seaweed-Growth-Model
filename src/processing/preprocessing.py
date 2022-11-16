"""
This files contains code to make the data ready for the model
"""
import os
import pickle

import pandas as pd
import xarray as xr


def prepare_gridded_data(path, folder, file_ending, global_or_US):
    """
    Reads in the pickles of the geodataframes of the
    different environmental paramters. Checks if they
    all have the same geometry and reorders them to fit
    the rest of the code.
    Arguments:
        path: the path for the pickled files
        folder: the folder where the pickled files are
        file_ending: the ending of the pickled files
        global_or_US: if "global", the global data is used,
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
    }
    dict_env_dfs = {}
    for science_name in env_params.keys():
        full_path = path + os.sep + "data" + os.sep + folder + os.sep
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
    full_path = path + os.sep + "data" + os.sep + "interim_results"
    with open(
        full_path + os.sep + "data_gridded_all_parameters_" + global_or_US + ".pkl",
        "wb",
    ) as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def prep_nw_data(
    path,
    file,
    length_time,
    env_param,
    min_lat=None,
    max_lat=None,
    min_lon=None,
    max_lon=None,
    all_cells=False,
):
    """
    ### This code is only used on the NCAR cluster. ###

    Reads the nuclear war data from Cheryls workspace.
    Creates a geopandas dataframe for it for a given
    environmental parameter and saves it in cwd as a pickle.
    Arguments:
        path: path to the file
        file: file name
        min_lon: index of the minimal longitude to sample from
        max_lon: index of the maximal longitude to sample from
        min_lat: index of the minimal latitude to sample from
        max_lat: index of the maximal latitude to sample from
        length_time: how much of the original dataset should
                     be used. Measured in month, max = 300
        env_param: the environmental parameter to look at
        all_cells: if True, all cells are used, if False, only selection
    Returns:
        None, but saves a pickle of the geodataframe
    """
    # Read in the data
    ds = xr.open_dataset(path + file)
    # 0 here means we are only using the uppermost layer of the ocean
    if all_cells:
        env_time = ds[env_param][:length_time, 0, :, :]
    else:
        env_time = ds[env_param][:length_time, 0, min_lat:max_lat, min_lon:max_lon]
    # Make it a dataframe
    env_time_df = env_time.to_dataframe()
    # Delete the depth column, as it is not needed
    if env_param == "PAR_avg":
        del env_time_df["z_t_150m"]
    else:
        del env_time_df["z_t"]
    # Create a new index to remove redundant information
    env_time_df.reset_index(inplace=True)
    env_time_df.set_index(["time", "TLONG", "TLAT"], inplace=True)
    # delte the nlat and nlon columns, as thy are not needed anymore
    del env_time_df["nlat"]
    del env_time_df["nlon"]
    # remove all columns that are only nan
    env_time_df.dropna(axis=0, how="all", inplace=True)
    # Save to pickle
    env_time_df.to_pickle(
        "nw_" + env_param + "_" + str(length_time) + "_months_pickle.pkl"
    )


def call_prep_nw_data(global_or_US):
    """
    ### This code is only used on the NCAR cluster. ###
    Calls the prep_nw_data function for all environmental parameters
    and saves the results in cwd as pickles.
    Arguments:
        global_or_US: string, either "global" or "US"
    Returns:
        None, but saves pickles
    """
    env_params = ["TEMP", "SALT", "PO4", "NO3", "PAR_surf", "NH4"]
    for env_param in env_params:
        print(env_param)
        path = "/glade/u/home/chsharri/Work/NW/"
        file = "nw_ur_150_07.pop.h." + env_param + ".nc"
        # Index positions of the US in the dataset
        min_lat = 250
        max_lat = 320
        min_lon = 235
        max_lon = 300
        length_time = 36
        if env_param == "PAR_surf":
            env_param = "PAR_avg"
        if global_or_US == "US":
            prep_nw_data(
                path, file, length_time, env_param, min_lat, max_lat, min_lon, max_lon
            )
        elif global_or_US == "global":
            prep_nw_data(path, file, 120, env_param, all_cells=True)
    print("done")


if __name__ == "__main__":
    prepare_gridded_data(".", "gridded_data_global", "120_months_pickle", "global")
    prepare_gridded_data(
        ".", "gridded_data_test_dataset_US_only", "36_months_pickle", "US"
    )
