#



## PlotterLME
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L12)
```python 
PlotterLME(
   seaweed_model
)
```


---
Class to organize all the plotting functions


**Methods:**


### .plot_growth_rate_by_lme_bar
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L20)
```python
.plot_growth_rate_by_lme_bar(
   month, path = ''
)
```

---
Plots the growth rate for the model based on LME as a bar chart

### .plot_growth_rate_by_lme_global
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L39)
```python
.plot_growth_rate_by_lme_global(
   month, path = ''
)
```

---
Plots the growth rate fraction for all LME on a global map

### .calculate_mean_groth_rate_by_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L71)
```python
.calculate_mean_groth_rate_by_lme()
```

---
Calculates the mean growth rate for a LME for the whole
time period modelled.

**Arguments**

None

**Returns**

None

### .plot_growth_rate_by_best_lme_as_line
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L95)
```python
.cluster_timeseries_all_parameters_q_lines(
   parameters, lme, lme_dict
)
```

---
Plots line plots for all clusters and all parameters

**Arguments**

* **parameters**  : a dictionary of dataframes of all parameters


**Returns**

None, but saves the plot

----


```python
.create_name_dict()
```

---
Creates a lookup dictionary for the LME names

**Returns**

A dictionary with LME names
