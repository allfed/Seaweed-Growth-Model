
from src import ocean_section as oc_se

class SeaweedModel:
    """
    Wrapper class that encapsulates the model
    and is meant to provide a simple interface.
    """
    def __init__(self):
        self.sections = {}

    def add_data_by_grid(self, grid_names, file):
        """
        Adds data from the database to the model.
        Based on a grid.
        Arguments:
            grid_names: a list of grid names
        Returns:
            None
        """
        for grid_name in grid_names:
            self.sections[grid_name] = oc_se.OceanSection(grid_name)
            self.sections[grid_name].get_grid_data(file)


    def add_data_by_lme(self, lme_names, file):
        """
        Adds data from the database to the model.
        Based on a LME.
        Arguments:
            lme_names: a list of LME names
        Returns:
            None
        """
        for lme_name in lme_names:
            self.sections[lme_name] = oc_se.OceanSection(lme_name)
            self.sections[lme_name].get_lme_data(file)


    def calculate_factors(self):
        """
        Calculates the growth factors for the model
        for all ocean sections (either grid or LME).
        """
        for section in self.sections.values():
            section.calculate_factors()


    def calculate_growth_rate(self):
        """
        Calculates the growth rate for the model
        for all ocean sections (either grid or LME).
        """
        for section in self.sections.values():
            section.calculate_growth_rate()

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
