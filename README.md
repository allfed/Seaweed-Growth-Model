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

## Structure

## How to use it




