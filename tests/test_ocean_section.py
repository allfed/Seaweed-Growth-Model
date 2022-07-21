"""
Tests the ocean section class
"""
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
    assert test_section.seaweed_growth_rate is not None
