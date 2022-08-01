"""
Reads in the ocean data after nuclear war provided by Cherryl Harrison
"""
import pandas as pd


class DataLME:
    """
    Creates a data object for the LME
    Meant to only read in the data once
    and provide the data for each LME as needed
    """
    def __init__(self, file):
        assert file is not None
        self.file= file
        self.lme_data = None
        self.lme_dict = {}
        # Prepare the data
        self.read_data()
        self.sort_data()
     

    def read_data(self):
        """
        read in the file
        """
        self.lme_data = pd.read_csv(self.file)


    def sort_data(self):
        """
        Sorts as a dictionary of pandas dataframes
        The data is ocean data after nuclear war seperated by 
        Large Marine Ecosystems (LME)
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
            self.lme_dict[i].columns = ["surface_temperature", "salinity", "nitrate", "illumination", "phosphate", "ammonium"]
            # For some reason some of the nitrate values are below 0, which is impossible. 
            # Set those to 0
            self.lme_dict[i]["nitrate"] = self.lme_dict[i]["nitrate"].clip(lower=0)


    def provide_data(self, lme_number):
        """
        Provides the data for a given LME
        Arguments:
            lme_number: the LME number
        Returns:
            a dataframe
        """
        return self.lme_dict[lme_number]


def read_file_by_lme(file):
    """
    Reads in a file and returns it as a dictionary of pandas dataframes
    The data is ocean data after nuclear war seperated by 
    Large Marine Ecosystems (LME)
    Arguments:
        file: the file to be read in
    Returns:
        A dictionary of pandas dataframes
    """
    # read in the file
    lme = pd.read_csv(file)
    # create a dictionary of dataframes
    lme_dict = {}
    # loop through the LMEs
    for i in range(1, 67):
        # create a dataframe for each LME
        lme_dict[i] = lme[lme["LME_number"] == i]
        # remove the LME column
        lme_dict[i] = lme_dict[i].drop(columns=["LME_number"])
        # set dates as index
        lme_dict[i].set_index("dates", inplace=True)
        # change format of index to datetime
        lme_dict[i].index = pd.to_datetime(lme_dict[i].index)
        # rename columns
        lme_dict[i].columns = ["surface_temperature", "salinity", "nitrate", "illumination", "phosphate", "ammonium"]
        # For some reason some of the nitrate values are below 0, which is impossible. 
        # Set those to 0
        lme_dict[i]["nitrate"] = lme_dict[i]["nitrate"].clip(lower=0)
    # return the dataframe
    return lme_dict

