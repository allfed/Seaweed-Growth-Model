"""
Main Interface
"""
import pandas as pd
import matplotlib.pyplot as plt
from src import ocean_section as oc_se

class SeaweedModel:
    """
    Wrapper class that encapsulates the model
    and is meant to provide a simple interface.
    """
    def __init__(self):
        self.sections = {}
        self.lme_or_grid = None


    def add_data_by_grid(self, grid_names, file):
        """
        Adds data from the database to the model.
        Based on a grid.
        Arguments:
            grid_names: a list of grid names
        Returns:
            None
        """
        # Make sure that the model is empty
        assert self.lme_or_grid is None
        # Set the model to grid
        self.lme_or_grid = "grid"
        # Add the data to the model
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
        # Make sure that the model is empty
        assert self.lme_or_grid is None
        # Set the model to LME
        self.lme_or_grid = "lme"
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


    def create_section_dfs(self):
        """
        Creates a dataframe for each section in the model.
        """
        for section in self.sections.values():
            section.create_section_df()


    def construct_df_from_sections_for_date(self, date):
        """
        Constructs a dataframe from the data in the model for a given date.
        Arguments:
            date: the date for which to construct the dataframe
        Returns:
            a dataframe
        """
        date_dict = {}
        for section_name, section_object in self.sections.items():
            date_dict[section_name] = section_object.select_section_df_date(date)
        return pd.DataFrame.from_dict(date_dict, orient="index")
    

    def plot_growth_rate_by_lme_bar(self, date, path=""):
        """
        Plots the growth rate for the model based on LME
        """
        assert self.lme_or_grid == "lme"
        date_section_df = self.construct_df_from_sections_for_date(date)
        ax = date_section_df.seaweed_growth_rate.sort_values().plot(kind="bar")
        ax.set_title("Growth Rate by LME")
        ax.set_xlabel("LME")
        ax.set_ylabel("Fraction of optimal growth rate")
        fig = plt.gcf()
        fig.set_size_inches(10, 5)
        plt.savefig(path + "growth_rate_by_lme_bar.png",dpi=200)


    def plot_growth_rate_by_grid(self, date):
        """
        Plots the growth rate for the model based on grid
        """
        assert self.lme_or_grid == "grid"


if __name__ == "__main__":
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, 67)], 
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    model.plot_growth_rate_by_lme_bar('2001-01-31')
    