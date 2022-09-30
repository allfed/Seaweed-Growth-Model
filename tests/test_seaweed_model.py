"""
Test the whole model
"""
from src.model.seaweed_model import SeaweedModel


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
    model.add_data_by_lme(
        [i for i in range(1, 4)], "data/lme_data/seaweed_environment_data_in_nuclear_war.csv"
    )
    assert len(model.sections.keys()) == 3


def test_grid_data():
    """
    Test the reading in of grid data and the calculation of factors
    This all happens in one function, so it only has to be read in once
    """
    # Testing the reading
    model = SeaweedModel()
    model.add_data_by_grid(
        "data/temporary_files/data_gridded_all_parameters.pkl",
    )
    # Number of grid cells with water
    assert len(model.sections.keys()) == 2259
    # Testing the calculation of factors
    model.calculate_factors()
    section_1 = model.sections[(17.474949344648152, 296.9649842693172)]
    assert section_1.salinity_factor is not None
    assert section_1.nutrient_factor is not None
    assert section_1.illumination_factor is not None
    assert section_1.temp_factor is not None
    # Testing the calculation of growth rate
    model.calculate_growth_rate()
    assert section_1.seaweed_growth_rate is not None


def test_calculating_factors_lme():
    """
    Test the calculation of factors
    """
    model = SeaweedModel()
    model.add_data_by_lme(
        [i for i in range(1, 4)], "data/lme_data/seaweed_environment_data_in_nuclear_war.csv"
    )
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
    model.add_data_by_lme(
        [i for i in range(1, 4)], "data/lme_data/seaweed_environment_data_in_nuclear_war.csv"
    )
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
    model.add_data_by_lme(
        [i for i in range(1, number_sections + 1)],
        "data/lme_data/seaweed_environment_data_in_nuclear_war.csv",
    )
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    sections_df = model.construct_df_from_sections_for_date(0)
    assert len(sections_df.index) == number_sections
    assert len(sections_df.columns) == 11


def test_construct_df_for_parameter():
    """
    Tests if the dataframe is correctly constructed from the sections
    """
    parameter = "seaweed_growth_rate"
    model = SeaweedModel()
    model.add_data_by_lme(
        [i for i in range(1, 3 + 1)],
        "data/lme_data/seaweed_environment_data_in_nuclear_war.csv",
    )
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    parameter_df = model.construct_df_for_parameter(parameter)
    # 240 is the number of months in the dataset
    # 3 is the number of sections
    assert len(parameter_df.index) == 240
    assert len(parameter_df.columns) == 3
