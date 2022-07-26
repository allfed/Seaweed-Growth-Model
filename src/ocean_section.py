"""
File contains the class OceanSection, which is used to represent
a section of the ocean. This can be either a large marine ecosystem
or simply a part of a global grid.
"""
import pandas as pd

from src import read_write_files as rwf
from src import seaweed_growth as sg

class OceanSection():
    """
    Class the represents a section of the ocean.
    alculates for every section how quickly seaweed can grow
    and also saves the single factors for growth
    """
    def __init__(self, name):
        # Add the name
        self.name = name
        # Add the data
        self.salinity = None
        self.temperature = None
        self.nitrate = None
        self.ammonium = None
        self.phosphate = None
        self.illumination = None
        # Add the factors
        self.salinity_factor = None
        self.nutrient_factor = None
        self.illumination_factor = None
        self.temp_factor = None
        self.seaweed_growth_rate = None
        # Add the dataframe
        self.section_df = None


    def get_lme_data(self, file):
        """
        Gets the data from the database based on the LME number
        Arguments:
            section_name: the name of the section
        Returns:
            None
        """
        # Get the data from the database
        lme_dict = rwf.read_file_by_lme(file)
        # Get the data for the LME
        lme = lme_dict[self.name]
        # Set the data (those are all pandas dataframes)
        self.salinity = lme["salinity"]
        self.temperature = lme["surface_temperature"]
        self.nitrate = lme["nitrate"]
        self.ammonium = lme["ammonium"]
        self.phosphate = lme["phosphate"]
        self.illumination = lme["illumination"]


    def get_grid_data(self, file):
        """
        Gets the data from the database based on the section name
        Arguments:
            grid_name: the name of the grid section
        Returns:
            None
        """
        # Get the data from the database
        section_dict = rwf.read_file_by_grid(file)
        # Get the data for the section
        section = section_dict[self.name]
        # Set the data (those are all pandas dataframes)
        self.salinity = section["salinity"]
        self.temperature = section["surface_temperature"]
        self.nitrate = section["nitrate"]
        self.ammonium = section["ammonium"]
        self.phosphate = section["phosphate"]
        self.illumination = section["illumination"]


    def calculate_factors(self):
        """
        Calculates the factors and growth rate for the ocean section
        Arguments:
            None
        Returns:
            None
        """
        # Calculate the factors
        self.salinity_factor = sg.calculate_salinity_factor(self.salinity)
        self.nutrient_factor = sg.calculate_nutrient_factor(self.nitrate, self.ammonium, self.phosphate)
        self.illumination_factor = sg.calculate_illumination_factor(self.illumination)
        self.temp_factor = sg.calculate_temperature_factor(self.temperature)


    def calculate_growth_rate(self):
        """
        Calculates the growth rate for the ocean section
        Arguments:
            None
        Returns:
            None
        """
        # Calculate the growth rate
        self.seaweed_growth_rate = sg.growth_factor_combination(self.illumination_factor, self.temp_factor, self.nutrient_factor, self.salinity_factor)
    

    def create_section_df(self):
        """
        Creates a dataframe that contains all the data for a given section
        This can only be run once the factors have been calculated
        """
        # check if the factors have been calculated
        assert self.salinity_factor is not None
        assert self.nutrient_factor is not None
        assert self.illumination_factor is not None
        assert self.temp_factor is not None
        assert self.seaweed_growth_rate is not None

        # Create the dataframe
        section_df = pd.DataFrame({"salinity": self.salinity,
                            "temperature": self.temperature,
                            "nitrate": self.nitrate,
                            "ammonium": self.ammonium,
                            "phosphate": self.phosphate,
                            "illumination": self.illumination,
                            "salinity_factor": self.salinity_factor,
                            "nutrient_factor": self.nutrient_factor,
                            "illumination_factor": self.illumination_factor,
                            "temp_factor": self.temp_factor,
                            "seaweed_growth_rate": self.seaweed_growth_rate})
        section_df.name = self.name
        self.section_df = section_df


    def select_section_df_date(self, date):
        """
        Selectes a date from the section df and returns it
        Arguments:
            date: the date to select
        Returns:
            the dataframe for the date
        """
        # check if the dataframe has been created
        assert self.section_df is not None
        # select the dataframe for the date
        return self.section_df.loc[date]


if __name__ == "__main__":
    test_section = OceanSection(1)
    test_section.get_lme_data("../data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
