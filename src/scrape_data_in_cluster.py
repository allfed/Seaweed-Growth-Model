import xarray as xr
import geopandas as gpd


def scrape_data(path, file, length_time, env_param):
    """
    Reads the nuclear war data from Cheryls workspace.
    Creates a geopandas dataframe for it for a given
    environmental parameter and saves it in cwd as a pickle.

    This code is only used on the NCAR cluster.

    Arguments:
        path: path to the file
        file: file name
        length_time: how much of the original dataset should
                     be used. Measured in month, max = 300
        env_param: the environmental parameter to look at
    Returns:
        None
    """
    # Read in the data
    ds = xr.open_dataset(path + file)
    # 0 here means we are only using the uppermost layer of the ocean
    env_time = ds[env_param][:length_time, 0, :, :]
    # Make it a dataframe
    env_time_df = env_time.to_dataframe()
    # Delete the depth column, as it is not needed
    if env_param == "PAR_avg":
        del env_time_df["z_t_150m"]
    else:
        del env_time_df["z_t"]
    # Convert it to a geodataframe
    env_time_df_geo = gpd.GeoDataFrame(
        env_time_df, geometry=gpd.points_from_xy(env_time_df.TLONG, env_time_df.TLAT)
    )
    # Create a new index to remove redundant informations
    env_time_df_geo.reset_index(inplace=True)
    env_time_df_geo.set_index(["time", "TLONG", "TLAT"], inplace=True)
    # delte the nlat and nlon columns, as thy are not needed anymore
    del env_time_df_geo["nlat"]
    del env_time_df_geo["nlon"]
    # Save to pickle
    env_time_df_geo.to_pickle(
        "nw_" + env_param + "_" + str(length_time) + "_months_pickle.pkl"
    )


if __name__ == "__main__":
    env_params = ["TEMP", "SALT", "PO4", "NO3", "PAR_surf"]
    for env_param in env_params:
        path = "/glade/u/home/chsharri/Work/NW/"
        file = "nw_ur_150_07.pop.h." + env_param + ".nc"
        length_time = 3
        if env_param == "PAR_surf":
            env_param = "PAR_avg"
        scrape_data(path, file, length_time, env_param)
    print("done")
