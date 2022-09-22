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
        env_df = pd.read_pickle(path+os.sep+"data" + os.sep + "gridded_data_test_dataset" + os.sep + "nw_" + science_name + "_3_months_pickle.pkl")
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
    with open("data_gridded_all_parameters.pkl", "wb") as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    prepare_gridded_data(".")
