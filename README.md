# Seaweed-Growth-Model
---


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6866654.svg)](https://doi.org/10.5281/zenodo.6866654)
![Testing](https://github.com/allfed/seaweed-growth-model/actions/workflows/testing.yml/badge.svg)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---
The Seaweed Growth Model is a tool that simulates the potential growth of seaweed in the aftermath of a nuclear war. The output of the model can be used to identify areas where seaweed growth is be possible. This model can be useful for researchers, environmentalists, and disaster response teams who are interested in understanding the potential impact of nuclear war on marine life. The model is implemented in Python and can be easily integrated into other analysis and visualization tools.

## Installation
To install the Seaweed Growth Model package, we recommend setting up a virtual environment. This will ensure that the package and its dependencies are isolated from other projects on your machine, which can prevent conflicts and make it easier to manage your dependencies. Here are the steps to follow:

* Create a virtual environment using either conda by running the command `conda env create -f environment.yml`. This will create an environment called "seaweed-growth-model". A virtual environment is like a separate Python environment, which you can think of as a separate "room" for your project to live in, it's own space which is isolated from the rest of the system, and it will have it's own set of packages and dependencies, that way you can work on different projects with different versions of packages without interfering with each other.

* Activate the environment by running `conda activate seaweed-growth-model`. This command will make the virtual environment you just created the active one, so that when you run any python command or install any package, it will do it within the environment.

* Install the package by running `pip install -e .` in the main folder of the repository. This command will install the package you are currently in as a editable package, so that when you make changes to the package, you don't have to reinstall it again.

* If you want to run the example Jupyter notebook, you'll need to create a kernel for the environment. First, install the necessary tools by running `conda install -c anaconda ipykernel`. This command will install the necessary tools to create a kernel for the Jupyter notebook. A kernel is a component of Jupyter notebook that allows you to run your code. It communicates with the notebook web application and the notebook document format to execute code and display the results.

* Then, create the kernel by running `python -m ipykernel install --user --name=seaweed-growth-model`. This command will create a kernel with the name you specified "seaweed-growth-model" , which you can use to run the example notebook or play around with the model yourself.

You can now use the kernel "seaweed-growth-model" to run the example notebook or play around with the model yourself. If you are using the kernel and it fails due an import error for the model package, you might have to rerun: `pip install -e .`.

If you encounter any issues, feel free to open an issue in the repository.

## How this model works in general

![Model](https://raw.githubusercontent.com/allfed/Seaweed-Growth-Model/main/results/model_description/structure.png)

This model here uses nuclear winter environmental data and an empirical model based on [James and Boriah (2010)](https://www.researchgate.net/publication/44797785_Modeling_Algae_Growth_in_an_Open-Channel_Raceway). It calculates the growth rate of *Gracilaria tikvahiae* on a global scale. The growth rate results are then used to simulate the [scale-up](https://github.com/allfed/Seaweed-Scaleup-Model) of seaweed production. 

## Example of usage
An example notebook on how this model can be used can be found in the [script folder](https://github.com/allfed/Seaweed-Growth-Model/blob/main/scripts/Example.ipynb). This example runs out of the box with the test data delivered with this repository. If you want to reproduce the results, you have to download the complete dataset. 

## Getting the global data

The data is available in a [Zenodo Repository](https://zenodo.org/record/7553874). Once you download it simply copy it to `data/gridded_data_global` folder. Once there, you can run the model with the global data. However, if you just want to play around with the model, there is a dataset available for testing directly in this repository. 

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

The following flow chart describes how different parts of this repository interact with each other and how data is transferred between them. 

![Model](https://raw.githubusercontent.com/allfed/Seaweed-Growth-Model/main/results/model_description/flow_chart.png)




