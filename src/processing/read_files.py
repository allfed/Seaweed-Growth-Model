"""
Reads in the ocean data after nuclear war provided by Cherryl Harrison
"""
import pickle

import pandas as pd


class DataLME:
    """
    Creates a data object for the LME
    Meant to only read in the data once
    and provide the data for each LME as needed
    """

    def __init__(self, file):
        assert file is not None
        self.file = file
        self.lme_data = None
        self.lme_dict = {}
        # Prepare the data
        self.read_data_lme()
        self.sort_data_lme()

    def read_data_lme(self):
        """
        read in the file
        Arguments:
            None
        Returns:
            None
        """
        self.lme_data = pd.read_csv(self.file)

    def sort_data_lme(self):
        """
        Sorts as a dictionary of pandas dataframes
        The data is ocean data after nuclear war seperated by
        Large Marine Ecosystems (LME)
        Arguments:
            None
        Returns:
            None
        """
        # loop through the LMEs
        for i in range(1, 67):
            # create a dataframe for each LME
            self.lme_dict[i] = self.lme_data[self.lme_data["LME_number"] == i]
            # remove the LME column
            self.lme_dict[i] = self.lme_dict[i].drop(columns=["LME_number"])
            # set dates as index
            self.lme_dict[i].set_index("dates", inplace=True)
            # change format of index to datetime
            self.lme_dict[i].index = pd.to_datetime(self.lme_dict[i].index)
            # rename columns
            self.lme_dict[i].columns = [
                "temperature",
                "salinity",
                "nitrate",
                "illumination",
                "phosphate",
                "ammonium",
                "iron",
            ]
            # For some reason some of the nitrate values are below 0, which is impossible.
            # Set those to 0
            self.lme_dict[i]["nitrate"] = self.lme_dict[i]["nitrate"].clip(lower=0)

    def provide_data_lme(self, lme_number):
        """
        Provides the data for a given LME
        Arguments:
            lme_number: the LME number
        Returns:
            a dataframe
        """
        return self.lme_dict[lme_number]


class DataGrid:
    """
    Creates a data object for the gridded data
    Meant to only read in the data once
    and provide the data for each grid cell as needed
    """

    def __init__(self, file):
        assert file is not None
        self.file = file
        self.grid_dict = {}
        # Prepare the data
        self.read_data_grid()
        # The gridded data does not have to be sorted
        # As it is already sorted in prep_data.py

    def read_data_grid(self):
        """
        Reads in the gridded data
        Arguments:
            None
        Returns:
            None
        """
        with open(self.file, "rb") as handle:
            self.grid_dict = pickle.load(handle)

    def provide_data_grid(self, lat_lon):
        """
        Provides the data for a given grid cell
        Arguments:
            lat_lon: the lat_lon coordinates as tuple of floats
        Returns:
            a geodataframe with all the environmental data
            for this grid cell
        """
        return self.grid_dict[lat_lon]
