import os
from src.model.seaweed_model import SeaweedModel


class PlotterGrid:
    def __init__(self, seaweed_model):
        self.seaweed_model = seaweed_model


def grid_US():
    """
    Initializes all the data for the grid model for the US and calls the plotting functions
    """
    model = SeaweedModel()
    path = "data" + os.sep + "gridded_data_test_dataset_US_only"
    file = "data_gridded_all_parameters.pkl"
    model.add_data_by_grid(path + os.sep + file)
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    df = model.construct_df_for_parameter("seaweed_growth_rate")
    df.plot(subplots=True, figsize=(50, 50))
