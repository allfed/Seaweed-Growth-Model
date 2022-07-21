
from src import ocean_section as oc_se

class SeaweedModel:
    """
    Wrapper class that encapsulates the model and its parameters.
    And is meant to provide a simple interface to the model.
    """
    def __init__(self):
        self.sections = {}

    def add_data_by_grid(self):
        """
        Adds data from the database to the model.
        Based on a grid.
        """
        pass

    def add_data_by_lme(self):
        """
        Adds data from the database to the model.
        Based on a LME.
        """
        pass

    def calculate_factors(self):
        """
        Calculates the growth factors for the model
        for all ocean sections (either grid or LME).
        """
        pass

    def calculate_growth_rate(self):
        """
        Calculates the growth rate for the model
        for all ocean sections (either grid or LME).
        """
        pass

    def plot_growth_rate_by_lme(self):
        """
        Plots the growth rate for the model based on LME
        """
        pass

    def plot_growth_rate_by_grid(self):
        """
        Plots the growth rate for the model based on grid
        """
        pass
