import os

import matplotlib.pyplot as plt
import pandas as pd

# Import the ALLFED stle
plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)


def cluster_timeseries_all_parameters_q_lines(parameters, lme, lme_dict):
    """
    Plots line plots for all clusters and all parameters
    Arguments:
        parameters: a dictionary of dataframes of all parameters
        lme: an integer of the LME number
        lme_dict: a dictionary of LME names
    Returns:
        None, but saves the plot
    """
    fig, axes = plt.subplots(
        nrows=5, ncols=1, sharey=True, sharex=True, figsize=(10, 10)
    )
    i = 0
    for parameter, parameter_df in parameters.items():
        ax = axes[i]
        lme_df = parameter_df.loc[lme, :]
        lme_df.plot(kind="line", ax=ax, legend=False, color="black", linewidth=2)
        lme_df.plot(kind="line", ax=ax, legend=False, linewidth=1.5)
        ax.set_ylabel(parameter)
        ax.set_xlabel("Months since nuclear war")
        if i == 0:
            ax.set_title("LME: " + lme_dict[lme])
        i += 1

    plt.savefig(
        "results"
        + os.sep
        + "lme"
        + os.sep
        + "cluster_timeseries_all_param_q_lines_LME_"
        + lme_dict[lme]
        + ".png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()


def create_name_dict():
    """
    Creates a lookup dictionary for the LME names
    Arguments:
        None
    Returns:
        A dictionary with LME names
    """
    lme_df = pd.read_csv(
        "data"
        + os.sep
        + "geospatial_information"
        + os.sep
        + "lme_shp"
        + os.sep
        + "lme_metadata.csv"
    )
    return dict(zip(lme_df.LME_NUMBER, lme_df.LME_NAME))


def main():
    """
    Runs the other functions to read the data and make the plots
    Arguments:
        None
    Returns:
        None
    """
    parameters = {}
    parameter_names = [
        "salinity_factor",
        "nutrient_factor",
        "illumination_factor",
        "temp_factor",
        "seaweed_growth_rate",
    ]
    for parameter in parameter_names:
        parameters[parameter] = pd.DataFrame(
            pd.read_pickle(
                "data"
                + os.sep
                + "interim_data"
                + os.sep
                + "150tg"
                + os.sep
                + parameter
                + "_LME.pkl"
            )
        )
    lme_dict = create_name_dict()
    for lme in range(1, 67):
        cluster_timeseries_all_parameters_q_lines(parameters, lme, lme_dict)


if __name__ == "__main__":
    main()
