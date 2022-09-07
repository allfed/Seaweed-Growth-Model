"""
Main Interface
"""
import pandas as pd
from src import ocean_section as oc_se
from src import read_files


class SeaweedModel:
    """
    Wrapper class that encapsulates the model
    and is meant to provide a simple interface.
    """

    def __init__(self):
        self.sections = {}
        self.lme_or_grid = None
        self.data = None

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
        # Add the data to the model
        data_lme = read_files.DataLME(file)
        # Add the sections to the model
        for lme_name in lme_names:
            self.sections[lme_name] = oc_se.OceanSection(
                lme_name, data_lme.provide_data_lme(lme_name)
            )
        self.lme_or_grid = "lme"

    def add_data_by_grid(self, lat_lons, file):
        """
        Adds data from the database to the model.
        Based on a grid.
        Arguments:
            lat_lons: a list of lat_lon tuples
        Returns:
            None
        """
        # Make sure that the model is empty
        assert self.lme_or_grid is None
        # Add the data to the model
        data_grid = read_files.DataGrid(file)
        # Add the sections to the model
        for lat_lon in lat_lons:
            self.sections[lat_lon] = oc_se.OceanSection(
                lat_lon, data_grid.provide_data_grid(lat_lon)
            )
        self.lme_or_grid = "grid"

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

    def construct_df_from_sections_for_date(self, min_month, max_month):
        """
        Constructs a dataframe from the data in the model for a given date.
        This uses the months since the beginning of the nuclear war.
        Mininum is -3, as the data starts before the war.
        Maximum is 357, as the data ends after the war.
        Arguments:
            min_months: the number of months since the beginning of the war (start date)
            max_months: the number of months since the beginning of the war (end date)
        Returns:
            a dataframe
        """
        assert self.lme_or_grid == "lme"
        date_dict = {}
        for section_name, section_object in self.sections.items():
            date_dict[section_name] = section_object.select_section_df_date_lme
            (
                min_month,
                max_month
            )
        return pd.DataFrame.from_dict(date_dict, orient="index")
