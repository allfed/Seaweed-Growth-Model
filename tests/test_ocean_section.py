"""
Tests the ocean section class
"""
import pandas as pd
import pytest

from src.model.ocean_section import OceanSection


def create_test_dataframe_reasonable_values():
    """
    Creates a reasonable test dataframe and returns it
    """
    df = pd.DataFrame()
    df["illumination"] = [50, 55, 65, 70, 0, 10, 5]
    df["temperature"] = [5, 15, 5, 10, 0.25, -1, 2]
    df["nitrate"] = [5, 15, 5, 10, 0, 1, 2]
    df["phosphate"] = [5, 15, 5, 10, 0, 1, 2]
    df["ammonium"] = [5, 15, 5, 10, 0, 1, 2]
    df["salinity"] = [25, 45, 5, 0, 30, 10, 20]
    df.index = pd.date_range("2001-01-01", periods=7, freq="D")
    return df


def test_initialization():
    """
    Tests if the Ocean Section class can create an instance
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    assert test_section is not None
    assert isinstance(test_section, OceanSection)


def test_get_section_data():
    """
    Tests if the Ocean Section class can get the data from the database
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    assert test_section.salinity is not None
    assert test_section.temperature is not None
    assert test_section.nitrate is not None
    assert test_section.ammonium is not None
    assert test_section.phosphate is not None
    assert test_section.illumination is not None


def test_calculate_factors():
    """
    Tests if the ocean section class can calculate the factors from the data
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    assert test_section.salinity_factor is not None
    assert test_section.nutrient_factor is not None
    assert test_section.illumination_factor is not None
    assert test_section.temp_factor is not None


def test_calculate_growth_rate():
    """
    Tests if the ocean section class can calculate the growth rate
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    assert test_section.seaweed_growth_rate is not None


def test_create_section_df():
    """
    Tests if the ocean section class can create a dataframe from the data
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    assert test_section.section_df is not None


def test_failed_creation_section_df():
    """
    Tests if the creation of the dataframe failes when the
    factors have not been calculated
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    with pytest.raises(AssertionError):
        test_section.create_section_df()


def test_select_section_df_date():
    """
    Tests if a dataframe can be selected by date
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    date_df = test_section.select_section_df_date(0)
    assert date_df.shape == (12)


def test_select_section_df_date_fail():
    """
    Tests if a dataframe can be selected by date
    if the section df has not yet been created
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    with pytest.raises(AssertionError):
        test_section.select_section_df_date(0)


def test_calculate_mean_growth_rate():
    """
    Tests if the mean growth rate can be calculated
    """
    df = create_test_dataframe_reasonable_values()
    test_section = OceanSection(1, df)
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    test_section.calculate_mean_growth_rate()
    assert test_section.calculate_mean_growth_rate() == 0.0006159845582776335
