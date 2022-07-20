"""
Reads in the ocean data after nuclear war provided by Cherryl Harrison
"""
import pandas as pd

def read_file_by_lme(file):
    """
    Reads in a file and returns it as a dictionary of pandas dataframes
    The data is ocean data after nuclear war seperated by 
    Large Marine Ecosystems (LME)
    Arguments:
        file: the file to be read in
    Returns:
        A pandas dataframe
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
    # return the dataframe
    return lme_dict


if __name__ == "__main__":
    lme_dict = read_file_by_lme("../data/seaweed_environment_data_in_nuclear_war.csv")
    lme = lme_dict[1]
