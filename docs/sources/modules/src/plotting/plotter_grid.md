#


### cluster_spatial
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L22)
```python
.cluster_spatial(
   growth_df, global_or_US, scenario
)
```

---
Creates a spatial plot of the clusters

**Arguments**

* **growth_df**  : a dataframe of the growth rate
* **global_or_US**  : a string of either "global" or "US" that indicates the scale


**Returns**

None, but saves the plot

----


### prepare_geometry
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L66)
```python
.prepare_geometry(
   growth_df
)
```

---
Prepares the geometry for the growth_df. For some reason the spatial data has
a longitude that is 0-360 instead of -180 to 180. This function converts it to
the latter

**Arguments**

* **growth_df**  : a dataframe of the growth rate


**Returns**

None, but saves the plot

----


### growth_rate_spatial_by_year
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L89)
```python
.growth_rate_spatial_by_year(
   growth_df, global_or_US, scenario
)
```

---
Plots the growth rate by year. This includes the first
three months without nuclear war, in the case of the first year

**Arguments**

* **growth_df**  : a dataframe of the growth rate


**Returns**

None, but saves the plot

----


### cluster_timeseries_all_parameters_q_lines
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L153)
```python
.cluster_timeseries_all_parameters_q_lines(
   parameters, global_or_US, scenario, areas
)
```

---
Plots line plots for all clusters and all parameters

**Arguments**

* **parameters**  : a dictionary of dataframes of all parameters


**Returns**

None, but saves the plot

----


### compare_nw_scenarios
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L278)
```python
.compare_nw_scenarios(
   areas
)
```

---
Compares the results of the nuclear war scenarios as weigthed median

**Arguments**

None

**Returns**

None

----


### compare_nutrient_subfactors
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L383)
```python
.compare_nutrient_subfactors(
   nitrate, ammonium, phosphate, scenario, areas
)
```

---
Takes the weighted average of the nutrient subfactors globally and plots them
in the same plot to be able to compare them.

**Arguments**

* **nitrate**  : The nitrate subfactor
* **ammonium**  : The ammonium subfactor
* **phosphate**  : The phosphate subfactor
* **scenario**  : The scenario to plot
* **areas**  : The areas of the grid cells


**Returns**

None
