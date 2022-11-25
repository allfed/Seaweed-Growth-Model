#


### cluster_spatial
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L19)
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
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L62)
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


### cluster_timeseries_all_parameters_q_lines
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L86)
```python
.cluster_timeseries_all_parameters_q_lines(
   parameters, global_or_US, scenario
)
```

---
Plots line plots for all clusters and all parameters

**Arguments**

* **parameters**  : a dictionary of dataframes of all parameters


**Returns**

None, but saves the plot
