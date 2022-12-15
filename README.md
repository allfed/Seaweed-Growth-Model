# Seaweed-Growth-Model
---


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6866654.svg)](https://doi.org/10.5281/zenodo.6866654)
![Testing](https://github.com/allfed/seaweed-growth-model/actions/workflows/testing.yml/badge.svg)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---
Model to calculate where seaweed can grow in a nuclear war. 

## Installation
We recommend setting up a virtual environment to install this model and all its dependencies. A more in depth explanation of virtual environments can be found [here](https://goodresearch.dev/). The short version is: just create a virtual environment from the `environment.yml` file here by using either conda or mamba:

`conda env create -f environment.yml`

This will create a virtual environment called "seaweed-growth-model". Once you activated it, you can install this model as a package into it by running the following line in the main folder of the repository:

`pip install -e .`

When you follow these steps you should have a virtual environment that is able to run the seaweed growth model. If you run into any problems feel free to open an issue in this repository or contact IT-support@allfed.info. 

## How this model works in general

![Model](https://raw.githubusercontent.com/allfed/Seaweed-Growth-Model/main/results/model_description/structure.png)

This model here uses nuclear winter environmental data and an empirical model based on [James and Boriah (2010)](https://www.researchgate.net/publication/44797785_Modeling_Algae_Growth_in_an_Open-Channel_Raceway). It calculates the growth rate of *Gracilaria tikvahiae* on a global scale. The growth rate results are then used to simulate the [scale-up](https://github.com/allfed/Seaweed-Scaleup-Model) of seaweed production. 

## Getting the global data

The data is available in a [Zenodo Repository](). Once you download it simply copy it to `data/gridded_data_global` folder. Once there, you can run the model with the global data. However, if you just want to play around with the model, there is a dataset available for testing directly in this repository. 

### Pickle Format

The data is stored in the pickle format to ensure a quick read time, as the overall dataset is several gigabytes large. Learn more about pickle [here](https://www.youtube.com/watch?v=Pl4Hp8qwwes).

### Original data download

The original data source is from [Harrison et al. (2022)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021AV000610). The files provided here are a subset of the total dataset. The script on how the data was downloaded from the original source can be found [here](https://github.com/florianjehn/Seaweed-Growth-Model/blob/main/scripts/Data_Download.ipynb). 

## Structure

The code in this repository is split into three parts:

### The actual model

The code for the actual model can be found in the model folder. It consists of three files:

* `seaweed_growth.py`: The equations of the empirical seaweed model by James and Boriah (2010). It can either do this for a single value or for a complete pandas series of values. 

* `ocean_section.py`: Meant to represent a section of the ocean. It is agnostic about the size of this section. So, it can be either a grid cell or a large marine ecosystem.

* `seaweed_model.py`: Interface to actually run the model. It reads in the data you provide it with, calculates the seaweed growth rate and saves the calculation results to a file. 

### Processing

Mainly concerned with handling/prepping the data for and by the model. 

#### Preprocessing

Reads in the raw data and transforms it into a format that can be understood by the model. 

#### Postprocessing

Calls the model (this can also be seen as an example of usage), runs it, reads in the output of the model, clusters it using [tslearn](https://tslearn.readthedocs.io/en/stable/) and saves it in a format more convenient for plotting. 

#### Reading/Writing

Code to read and write files. 

### Plotting

Makes the plots for the publication. 

## Flow Chart for Structure

![Model](https://raw.githubusercontent.com/allfed/Seaweed-Growth-Model/main/results/model_description/flow_chart.png)




