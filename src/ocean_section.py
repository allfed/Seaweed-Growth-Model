"""
File contains the class OceanSection, which is used to represent
a section of the ocean. This can be either a large marine ecosystem
or simply a part of a global grid.
"""
import pandas as pd

from src import seaweed_growth as sg


class OceanSection:
    """
    Class the represents a section of the ocean.
    alculates for every section how quickly seaweed can grow
    and also saves the single factors for growth
    """

    def __init__(self, name, data):
        # Add the name
        self.name = name
        # Add the data
        self.salinity = data["salinity"]
        self.temperature = data["temperature"]
        self.nitrate = data["nitrate"]
        self.ammonium = data["ammonium"]
        self.phosphate = data["phosphate"]
        self.illumination = data["illumination"]
        # Add the factors
        self.salinity_factor = None
        self.nutrient_factor = None
        self.illumination_factor = None
        self.temp_factor = None
        self.seaweed_growth_rate = None
        # Add the dataframe
        self.section_df = None

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
        self.nutrient_factor = sg.calculate_nutrient_factor(
            self.nitrate, self.ammonium, self.phosphate
        )
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
        self.seaweed_growth_rate = sg.growth_factor_combination(
            self.illumination_factor,
            self.temp_factor,
            self.nutrient_factor,
            self.salinity_factor,
        )

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
        section_df = pd.DataFrame(
            {
                "salinity": self.salinity,
                "temperature": self.temperature,
                "nitrate": self.nitrate,
                "ammonium": self.ammonium,
                "phosphate": self.phosphate,
                "illumination": self.illumination,
                "salinity_factor": self.salinity_factor,
                "nutrient_factor": self.nutrient_factor,
                "illumination_factor": self.illumination_factor,
                "temp_factor": self.temp_factor,
                "seaweed_growth_rate": self.seaweed_growth_rate,
            }
        )
        # Add a column with the month since war
        section_df["months_since_war"] = list(range(-3, section_df.shape[0] - 3, 1))
        # Add the dataframe to the class
        section_df.name = self.name
        self.section_df = section_df

    def calculate_mean_growth_rate(self):
        """
        Calculates the mean growth rate and returns it
        """
        # check if the dataframe has been created
        assert self.section_df is not None
        # calculate the mean growth rate
        return self.section_df["seaweed_growth_rate"].mean()

    def select_section_df_date(self, month):
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
        return self.section_df[
            self.section_df["months_since_war"].where("months_since_war", month)
        ]
