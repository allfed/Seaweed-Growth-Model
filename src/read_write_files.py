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

def read_file_by_grid(file):
    """
    Reads in a file and returns it as a dictionary of pandas dataframes
    Arguments:
        file: the file to be read in
    Returns:
        A dictionary of pandas dataframes
    """
    # read in the file
    grids = pd.read_csv(file)
    # create a dictionary of dataframes
    grid_dict = {}
    # loop through the sections
    for i in range(1, 67):
        # create a dataframe for each section
        grid_dict[i] = grids[grids["section_number"] == i]
        # remove the section column
        grid_dict[i] = grid_dict[i].drop(columns=["section_number"])
        # set dates as index
        grid_dict[i].set_index("dates", inplace=True)
        # change format of index to datetime
        grid_dict[i].index = pd.to_datetime(grid_dict[i].index)
        # rename columns
        grid_dict[i].columns = ["surface_temperature", "salinity", "nitrate", "illumination", "phosphate", "ammonium"]
    # return the dataframe
    return grid_dict


def write_factors_by_section(file, factors):
    """
    Writes the factors to a file
    Arguments:
        section_name: the name of the section
        file: the file to be written to
        factors: the factors to be written
    Returns:
        None
    """
    # create a dataframe
    factors_df = pd.DataFrame(factors)
    # set the index to the section name
    factors_df.set_index(section_name, inplace=True)
    # write the dataframe to the file
    factors_df.to_csv(file) 


if __name__ == "__main__":
    lme_dict = read_file_by_lme("../data/seaweed_environment_data_in_nuclear_war.csv")
    lme = lme_dict[1]
