"""
Tests the ocean section class
"""
from src.ocean_section import Ocean_Section

def test_initialization():
    """
    Tests if the Ocean Section class can create an instance
    """
    test_section = Ocean_Section()
    assert test_section is not None
    assert isinstance(test_section, Ocean_Section)


def test_get_section_data():
    """
    Tests if the Ocean Section class can get the data from the database
    """
    test_section = Ocean_Section()
    test_section.get_lme_data(1)
    assert test_section.salinity is not None
    assert test_section.temperature is not None
    assert test_section.nitrate is not None
    assert test_section.ammonium is not None
    assert test_section.phosphate is not None
    assert test_section.illumination is not None
