#


### cluster_spatial
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L18)
```python
.cluster_spatial(
   growth_df, global_or_US
)
```

---
Creates a spatial plot of the clusters

----


### prepare_geometry
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L53)
```python
.prepare_geometry(
   growth_df
)
```

---
Prepares the geometry for the growth_df. For some reason the spatial data has
a longitude that is 0-360 instead of -180 to 180. This function converts it to
the latter

----


### cluster_timeseries_all_parameters_q_lines
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_grid.py/#L73)
```python
.cluster_timeseries_all_parameters_q_lines(
   parameters, global_or_US
)
```

---
Plots line plots for all clusters and all parameters

**Arguments**

* **parameters**  : a dictionary of dataframes of all parameters


**Returns**

None, but saves the plot
