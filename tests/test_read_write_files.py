"""
Tests the reading and writing of files
"""
import sys
import pandas as pd
from pathlib import Path
import pytest

# Add the source directory to the path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.read_write_files import read_file_by_LME


def test_read_file_by_LME():
    """
    Tests the read_file_by_LME function
    """
    # Test 1
    assert read_file_by_LME("data/seaweed_environment_data_in_nuclear_war.csv") is not None
    # Test 2
    assert isinstance(read_file_by_LME("data/seaweed_environment_data_in_nuclear_war.csv"), dict)
    # Test 3
    assert len(read_file_by_LME("data/seaweed_environment_data_in_nuclear_war.csv").keys()) == 66 # number of LMEs
    # Test 4
    df_dict = read_file_by_LME("data/seaweed_environment_data_in_nuclear_war.csv")
    for df in df_dict.values():
        assert isinstance(df, pd.DataFrame)
        # 240 months, 7 parameters
        assert df.shape == (240, 6)


