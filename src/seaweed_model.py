"""
Main Interface
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from src import ocean_section as oc_se

class SeaweedModel:
    """
    Wrapper class that encapsulates the model
    and is meant to provide a simple interface.
    """
    def __init__(self):
        self.sections = {}
        self.lme_or_grid = None


    def add_data_by_grid(self, grid_names, file):
        """
        Adds data from the database to the model.
        Based on a grid.
        Arguments:
            grid_names: a list of grid names
        Returns:
            None
        """
        # Make sure that the model is empty
        assert self.lme_or_grid is None
        # Set the model to grid
        self.lme_or_grid = "grid"
        # Add the data to the model
        for grid_name in grid_names:
            self.sections[grid_name] = oc_se.OceanSection(grid_name)
            self.sections[grid_name].get_grid_data(file)


    def add_data_by_lme(self, lme_names, file):
        """
        Adds data from the database to the model.
        Based on a LME.
        Arguments:
            lme_names: a list of LME names
        Returns:
            None
        """
        # Make sure that the model is empty
        assert self.lme_or_grid is None
        # Set the model to LME
        self.lme_or_grid = "lme"
        for lme_name in lme_names:
            self.sections[lme_name] = oc_se.OceanSection(lme_name)
            self.sections[lme_name].get_lme_data(file)


    def calculate_factors(self):
        """
        Calculates the growth factors for the model
        for all ocean sections (either grid or LME).
        """
        for section in self.sections.values():
            section.calculate_factors()


    def calculate_growth_rate(self):
        """
        Calculates the growth rate for the model
        for all ocean sections (either grid or LME).
        """
        for section in self.sections.values():
            section.calculate_growth_rate()


    def create_section_dfs(self):
        """
        Creates a dataframe for each section in the model.
        """
        for section in self.sections.values():
            section.create_section_df()


    def construct_df_from_sections_for_date(self, date):
        """
        Constructs a dataframe from the data in the model for a given date.
        Arguments:
            date: the date for which to construct the dataframe
        Returns:
            a dataframe
        """
        date_dict = {}
        for section_name, section_object in self.sections.items():
            date_dict[section_name] = section_object.select_section_df_date(date)
        return pd.DataFrame.from_dict(date_dict, orient="index")
    

    def plot_growth_rate_by_lme_bar(self, date, path=""):
        """
        Plots the growth rate for the model based on LME as a bar chart
        """
        assert self.lme_or_grid == "lme"
        date_section_df = self.construct_df_from_sections_for_date(date)
        ax = date_section_df.seaweed_growth_rate.sort_values().plot(kind="bar")
        ax.set_title("Growth Rate by LME")
        ax.set_xlabel("LME")
        ax.set_ylabel("Fraction of optimal growth rate")
        fig = plt.gcf()
        fig.set_size_inches(10, 5)
        plt.savefig(path + "growth_rate_by_lme_bar"+str(date)+".png",dpi=200)
        plt.close()


    def plot_growth_rate_by_lme_global(self, date, path=""):
        """
        Plots the growth rate fraction for all LME on a global map
        """
        assert self.lme_or_grid == "lme"
        date_section_df = self.construct_df_from_sections_for_date(date)
        lme_shape = gpd.read_file("data/lme_shp/lme66.shp")
        lme_global = lme_shape.merge(date_section_df, left_on="LME_NUMBER", right_index=True)
        ax = lme_global.plot(column="seaweed_growth_rate", cmap="Greens", legend=True, 
                            edgecolor="black", linewidth=0.3)
        ax.set_title("Fraction of optimal growth rate on date: " + str(date))
        fig = plt.gcf()
        fig.set_size_inches(10, 5)
        plt.savefig(path + "growth_rate_by_lme_global_"+str(date)+".png",dpi=200)
        plt.close()


    def calculate_mean_groth_rate_by_lme(self):
        """
        Calculates the mean growth rate for a LME for the whole
        time period modelled. 
        """
        assert self.lme_or_grid == "lme"        
        growth_rate_dict = {}
        for section_name, section_instance in self.sections.items():
            growth_rate_dict[section_name] = section_instance.calculate_mean_growth_rate()
        growth_df = pd.DataFrame.from_dict(growth_rate_dict, orient="index")
        growth_df.columns = ["mean_growth_rate"]
        print("LMEs with highest mean growth rates are:")
        print(growth_df["mean_growth_rate"].sort_values(ascending=False).head())
            

    def plot_growth_rate_by_best_lme_as_line(self, path=""):
        """
        Takes the growthrate of the 5 best LMEs (by mean growth rate)
        29    0.391329
        11    0.309920
        38    0.304329
        37    0.299366
        31    0.266062
        and plots them over time. 
        """
        assert self.lme_or_grid == "lme"
        best_lme = [29,11,38,37,31]
        colors = ["red", "blue", "green", "orange", "purple"]
        ax = plt.gca()
        i = 0
        for section_name, section_instance in self.sections.items():
            if section_name in best_lme:
                section_instance.section_df["seaweed_growth_rate"].plot(ax=ax, label=section_name, color=colors[i])
                i += 1
        ax.set_title("Growth Rate of the 5 best LMEs")
        fig = plt.gcf()
        fig.set_size_inches(10, 5)
        plt.savefig(path + "growth_rate_by_best.png",dpi=200)
        plt.close()


    def plot_growth_rate_by_grid(self, date):
        """
        Plots the growth rate for the model based on grid
        """
        assert self.lme_or_grid == "grid"


if __name__ == "__main__":
    model = SeaweedModel()
    model.add_data_by_lme([i for i in range(1, 67)], 
                            "data/seaweed_environment_data_in_nuclear_war.csv")
    model.calculate_factors()
    model.calculate_growth_rate()
    model.create_section_dfs()
    # Plot for a selection of dates
    # beginning of simulation before nuclear war
    # one month after nuclear war
    # one year after nuclear war
    # two years after nuclear war
    # and so forth
    dates = ['2001-01-31'] + ["200" + str(i) + "-06-30" for i in range(2, 10)] + \
            ["20" + str(i) + "-06-30" for i in range(10, 18)]

    for date in dates:
        model.plot_growth_rate_by_lme_bar(date, path="results/lme/")
        model.plot_growth_rate_by_lme_global(date, path="results/lme/")

    # Print the best 5 LMEs by mean growth rate
    model.calculate_mean_groth_rate_by_lme()

    # Plot the growth rate of the 5 best LMEs
    model.plot_growth_rate_by_best_lme_as_line(path="results/lme/")