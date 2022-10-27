#


## PlotterLME
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L11)
```python 
PlotterLME(
   seaweed_model
)
```


---
Class to organize all the plotting functions


**Methods:**


### .plot_growth_rate_by_lme_bar
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L19)
```python
.plot_growth_rate_by_lme_bar(
   month, path = ''
)
```

---
Plots the growth rate for the model based on LME as a bar chart

### .plot_growth_rate_by_lme_global
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L38)
```python
.plot_growth_rate_by_lme_global(
   month, path = ''
)
```

---
Plots the growth rate fraction for all LME on a global map

### .calculate_mean_groth_rate_by_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L70)
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
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L94)
```python
.plot_growth_rate_by_best_lme_as_line(
   path = '', window = 10
)
```

---
Takes the growthrate of the 3 best LMEs (by mean growth rate)
29    0.391329
11    0.309920
38    0.304329
and plots them over time.


**Arguments**

* **path**  : the path to save the plot to
* **window**  : the window size for the rolling mean


**Returns**

None

----


### lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/plotting/plotter_lme.py/#L138)
```python
.lme()
```

---
Initializes all the data for the LME model and calls the plotting functions
