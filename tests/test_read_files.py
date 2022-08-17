"""
Tests the reading and writing of files
"""
import pandas as pd
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
