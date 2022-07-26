"""
Test the whole model
"""

from src.seaweed_model import SeaweedModel


def test_create_model_instance():
    """
    Test the creation of a model instance
    """
    model = SeaweedModel()
    assert model is not None


def test_reading_in_lme_data():
    """
    Test the reading in of LME data
    """
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, 4)],
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    assert len(model.sections.keys()) == 3


def test_reading_in_grid_data():
    """
    Test the reading in of grid data
    """
    pass
    #TODO implement this test once I have the grid data


def test_calculating_factors():
    """
    Test the calculation of factors
    """
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, 4)],
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    model.calculate_factors()
    section_1 = model.sections[1]
    assert section_1.salinity_factor is not None
    assert section_1.nutrient_factor is not None
    assert section_1.illumination_factor is not None
    assert section_1.temp_factor is not None


def test_calculating_growth_rate():
    """
    Test the calculation of growth rate
    """
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, 4)],
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    model.calculate_factors()
    model.calculate_growth_rate()
    section_1 = model.sections[1]
    assert section_1.seaweed_growth_rate is not None


def test_construct_dataframe_from_section_data():
    """
    Tests if the dataframe is correctly constructed from the sections
    """
    number_sections = 3
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, number_sections+1)],
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    sections_df = model.construct_df_from_sections_for_date("2001-01-31")
    assert len(sections_df.index) == number_sections
    assert len(sections_df.columns) == 11
