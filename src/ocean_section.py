"""
Main file that ties the other ones together.
"""
import read_write_files as rwf



class Ocean_Section():
    """
    Class the represents a section of the ocean.
    alculates for every section how quickly seaweed can grow
    and also saves the single factors for growth
    """
    def __init__(self):
        # Add the original data
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
        self.self_shading_factor = None
        self.temp_factor = None
        self.seaweed_growth_rate = None

    def get_lme_data(self, lme_number):
        """
        Gets the data from the database based on the LME number
        Arguments:
            section_name: the name of the section
        Returns:
            The data of the section
        """
        # Get the data from the database
        lme_dict = rwf.read_file_by_lme("../data/seaweed_environment_data_in_nuclear_war.csv")
        # Get the data for the LME
        lme = lme_dict[lme_number]
        # Set the data
        self.salinity = lme["salinity"]
        self.temperature = lme["surface_temperature"]
        self.nitrate = lme["nitrate"]
        self.ammonium = lme["ammonium"]
        self.phosphate = lme["phosphate"]
        self.illumination = lme["illumination"]

    def calculate_factors(self):
        
        