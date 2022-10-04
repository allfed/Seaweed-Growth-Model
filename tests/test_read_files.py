"""
Tests the reading and writing of files
"""
import pandas as pd

from src.processing.read_files import DataGrid, DataLME


def test_read_file_by_lme():
    """
    Tests the read_file class DataLME
    """
    data_LME = DataLME("data/lme_data/seaweed_environment_data_in_nuclear_war.csv")
    # Make sure the correct object gets created
    assert isinstance(data_LME, DataLME)
    assert data_LME is not None
    # Make sure the data is read in
    assert isinstance(data_LME.lme_dict, dict)
    # Make sure the data is correct
    assert len(data_LME.lme_dict) == 66  # number of LMEs
    for df in data_LME.lme_dict.values():
        assert isinstance(df, pd.DataFrame)
        # 240 months, 6 parameters
        assert df.shape == (240, 6)


def test_read_file_by_grid():
    """
    Tests the read_file class DataGrid
    """
    data_grid = DataGrid(
        "data/interim_results/data_gridded_all_parameters.pkl"
    )
    # Make sure the correct object gets created
    assert data_grid is not None
    assert isinstance(data_grid, DataGrid)
    # Make sure the data is read in
    assert isinstance(data_grid.grid_dict, dict)
    # Make sure the data is correct
    for df in data_grid.grid_dict.values():
        assert isinstance(df, pd.DataFrame)
        # 6 parameters + lat + lon
        assert df.shape[1] == 9
