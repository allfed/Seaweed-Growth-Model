"""
Tests the ocean section class
"""
import pytest

from src.ocean_section import OceanSection

def test_initialization():
    """
    Tests if the Ocean Section class can create an instance
    """
    test_section = OceanSection(1)
    assert test_section is not None
    assert isinstance(test_section, OceanSection)


def test_get_section_data():
    """
    Tests if the Ocean Section class can get the data from the database
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
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
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    assert test_section.salinity_factor is not None
    assert test_section.nutrient_factor is not None
    assert test_section.illumination_factor is not None
    assert test_section.temp_factor is not None


def test_calculate_growth_rate():
    """
    Tests if the ocean section class can calculate the growth rate
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    assert test_section.seaweed_growth_rate is not None


def test_create_section_df():
    """
    Tests if the ocean section class can create a dataframe from the data
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    assert test_section.section_df is not None


def test_failed_creation_section_df():
    """
    Tests if the creation of the dataframe failes when the
    factors have not been calculated
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    with pytest.raises(AssertionError):
        test_section.create_section_df()


def test_section_df_shape():
    """
    Tests if the dataframe has the correct shape when it is created
    for LMEs data
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    assert test_section.section_df.shape == (240, 11)


def test_select_section_df_date():
    """
    Tests if a dataframe can be selected by date
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    test_section.create_section_df()
    date_df = test_section.select_section_df_date('2001-01-31')
    assert date_df.shape == (11,)


def test_select_section_df_date_fail():
    """
    Tests if a dataframe can be selected by date 
    if the section df has not yet been created
    """
    test_section = OceanSection(1)
    test_section.get_lme_data("data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
    test_section.calculate_growth_rate()
    with pytest.raises(AssertionError):
        test_section.select_section_df_date('2001-01-31')
