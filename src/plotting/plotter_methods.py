"""
Creates some additional plots, needed as an
explanation on how the model works (mainly the factors)
"""
import os

import matplotlib.pyplot as plt
import numpy as np

from src.model.seaweed_growth import (ammonium_subfactor,
                                      illumination_single_value,
                                      nitrate_subfactor, phosphate_subfactor,
                                      salinity_single_value,
                                      temperature_single_value)

plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)


def plot_factors():
    """
    Plots the factors used in the model, with a range that fits to the factor
    Arguments:
        None
    Returns:
        None
    """
    # Contains the ranges and the units
    factor_dict = {
        "Illumination": (140, "W per m²"), "Temperature": (40, "°C"),
        "Nutrient": (20, "μmol per m³"), "Salinity": (50, "ppt")}
    # Iterates over the factors and plot them
    for factor, (factor_range, unit) in factor_dict.items():
        # Creates the x-axis
        x = np.linspace(0, factor_range, 10000)
        # Creates the y-axis
        if factor == "Illumination":
            y = [illumination_single_value(i) for i in x]
        elif factor == "Temperature":
            y = [temperature_single_value(i) for i in x]
        elif factor == "Salinity":
            y = [salinity_single_value(i) for i in x]
        if factor != "Nutrient":
            # Creates the plot
            plt.plot(x, y, linewidth=2.5, color="black")
            plt.plot(x, y, linewidth=2)
        else:
            for subfactor, sub_function in {"Nitrate": nitrate_subfactor,
                                            "Phosphate": phosphate_subfactor,
                                            "Ammonium": ammonium_subfactor}.items():
                y = [sub_function(i) for i in x]
                plt.plot(x, y, linewidth=2.5, color="black")
                plt.plot(x, y, label=subfactor, linewidth=2)
                plt.legend()
        # Adds the unit to the y-axis
        plt.ylabel(f"{factor} Factor")
        # Adds the unit to the x-axis
        plt.xlabel(f"{factor} [{unit}]")
        # Change the size
        plt.gcf().set_size_inches(8, 2)
        # Saves the plot
        plt.savefig(
            "results"
            + os.sep
            + "factors"
            + os.sep
            + f"{factor}_factor.png"
            + ".png",
            dpi=250,
            bbox_inches="tight",
        )
        # Closes the plot
        plt.close()


if __name__ == "__main__":
    plot_factors()
