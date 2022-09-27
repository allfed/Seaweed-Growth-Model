"""
Tests the reading and writing of files
"""
import os

import geopandas as gpd
import pandas as pd
import pytest

from src import read_files


def test_read_file_by_lme():
    """
    Tests the read_file class DataLME
    """
    data_LME = read_files.DataLME("data/seaweed_environment_data_in_nuclear_war.csv")
    # Make sure the correct object gets created
    assert isinstance(data_LME, read_files.DataLME)
    assert data_LME is not None
    # Make sure the data is read in
    assert isinstance(data_LME.lme_dict, dict)
    # Make sure the data is correct
    assert len(data_LME.lme_dict) == 66  # number of LMEs
    for df in data_LME.lme_dict.values():
        assert isinstance(df, pd.DataFrame)
        # 240 months, 6 parameters
        assert df.shape == (240, 6)


reason = """Skip this when not run locally, as it requires the data to be present
 Had to skip this file for Github as it is too large """


@pytest.mark.skipif("zorin" not in os.environ, reason=reason)
def test_read_file_by_grid():
    """
    Tests the read_file class DataGrid
    """
    data_grid = read_files.DataGrid
    ("data/gridded_data_test_dataset/data_gridded_all_parameters.pkl")
    # Make sure the correct object gets created
    assert isinstance(data_grid, read_files.DataGrid)
    assert data_grid is not None
    # Make sure the data is read in
    assert isinstance(data_grid.grid_dict, dict)
    # Make sure the data is correct
    assert len(data_grid.grid_dict) == 122880  # number of lat_lon combos
    for df in data_grid.grid_dict.values():
        assert isinstance(df, gpd.GeoDataFrame)
        # 6 parameters + geometry + lat + lon
        assert df.shape[1] == 9
