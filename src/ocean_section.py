"""
File contains the class OceanSection, which is used to represent 
a section of the ocean. This can be either a large marine ecosystem
or simply a part of a global grid. 
"""
from src import read_write_files as rwf
from src import seaweed_growth as sg

class OceanSection():
    """
    Class the represents a section of the ocean.
    alculates for every section how quickly seaweed can grow
    and also saves the single factors for growth
    """
    def __init__(self):
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

    def get_lme_data(self, lme_number, file):
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
        lme = lme_dict[lme_number]
        # Set the data (those are all pandas dataframes)
        self.salinity = lme["salinity"]
        self.temperature = lme["surface_temperature"]
        self.nitrate = lme["nitrate"]
        self.ammonium = lme["ammonium"]
        self.phosphate = lme["phosphate"]
        self.illumination = lme["illumination"]

    def get_grid_data(self, grid_name, file):
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
        section = section_dict[grid_name]
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
        self.seaweed_growth_rate = sg.growth_factor_combination(self.illumination_factor, self.temp_factor, self.nutrient_factor, self.salinity_factor)


if __name__ == "__main__":
    test_section = OceanSection()
    test_section.get_lme_data(1, "data/seaweed_environment_data_in_nuclear_war.csv")
    test_section.calculate_factors()
