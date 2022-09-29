"""
This files contains code to make the data ready for the model
"""
import xarray as xr
import pickle
import geopandas as gpd
import pandas as pd
import os


def prepare_gridded_data(path):
    """
    Reads in the pickles of the geodataframes of the
    different environmental paramters. Checks if they
    all have the same geometry and reorders them to fit
    the rest of the code.

    Arguments:
        path: the path for the pickled files
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
        full_path = path + os.sep + "data" + os.sep + "gridded_data_test_dataset_US_only" + os.sep
        env_df = pd.read_pickle(full_path + "nw_" + science_name + "_36_months_pickle.pkl")
        env_df.reset_index(inplace=True)
        env_df.columns = ["time", "TLONG", "TLAT", env_params[science_name], "geometry"]
        dict_env_dfs[science_name] = gpd.GeoDataFrame(env_df)
    # Assert if they all have the same geometry
    # This is needed so we can use the geometry of all dfs interchangeably
    list_env_dfs_geometry = [
        dict_env_dfs[env_param]["geometry"] for env_param in env_params.keys()
    ]
    i = 0
    while i < len(list_env_dfs_geometry) - 1:
        assert list_env_dfs_geometry[i].equals(list_env_dfs_geometry[i + 1])
        i += 1
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
                env_param_latlon_df.loc[env_param_latlon_df["nitrate"] < 0, "nitrate"] = 0
            list_env_param_latlon_df.append(pd.DataFrame(env_param_latlon_df))
        concat_latlon_dfs = pd.concat(list_env_param_latlon_df, axis=1)
        # Remove duplicate columns
        concat_latlon_dfs = concat_latlon_dfs.loc[
            :, ~concat_latlon_dfs.columns.duplicated()
        ].copy()
        # Add a column with the month since war
        concat_latlon_dfs["months_since_war"] = list(
            range(-4, concat_latlon_dfs.shape[0] - 4, 1)
        )
        # Convert back to geodataframe before saving
        data_dict[lat_lon] = gpd.GeoDataFrame(concat_latlon_dfs)
    # Make pickle out of it, so we don't have to run this every time
    full_path = path + os.sep + "data" + os.sep + "gridded_data_test_dataset_US_only" + os.sep
    with open(full_path + "data_gridded_all_parameters.pkl", "wb") as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def prep_nw_data(path, file, min_lat, max_lat, min_lon, max_lon, length_time, env_param):
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
    Returns:
        None
    """
    # Read in the data
    ds = xr.open_dataset(path + file)
    # 0 here means we are only using the uppermost layer of the ocean

    env_time = ds[env_param][:length_time, 0, min_lat:max_lat, min_lon:max_lon]
    # Make it a dataframe
    env_time_df = env_time.to_dataframe()
    # Delete the depth column, as it is not needed
    if env_param == "PAR_avg":
        del (env_time_df["z_t_150m"])
    else:
        del (env_time_df["z_t"])
    # Convert it to a geodataframe
    env_time_df_geo = gpd.GeoDataFrame(
        env_time_df, geometry=gpd.points_from_xy(env_time_df.TLONG, env_time_df.TLAT))
    # Create a new index to remove redundant information
    env_time_df_geo.reset_index(inplace=True)
    env_time_df_geo.set_index(["time", "TLONG", "TLAT"], inplace=True)
    # delte the nlat and nlon columns, as thy are not needed anymore
    del (env_time_df_geo["nlat"])
    del (env_time_df_geo["nlon"])
    # Save to pickle
    env_time_df_geo.to_pickle("nw_" + env_param + "_" + str(length_time) + "_months_pickle.pkl")

def call_prep_nw_data():
    env_params = ["TEMP", "SALT", "PO4", "NO3", "PAR_surf", "NH4"]
    for env_param in env_params:
        print(env_param)
        path = '/glade/u/home/chsharri/Work/NW/'
        file = 'nw_ur_150_07.pop.h.' + env_param + '.nc'
        # Index positions of the US in the dataset
        min_lat = 250
        max_lat = 320
        min_lon = 235
        max_lon = 300
        length_time = 36
        if env_param == "PAR_surf":
            env_param = "PAR_avg"
        prep_nw_data(path, file, min_lat, max_lat, min_lon, max_lon, length_time, env_param)
    print("done")


if __name__ == "__main__":
    prepare_gridded_data(".")