#


## SeaweedModel
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L11)
```python 

```


---
Wrapper class that encapsulates the model
and is meant to provide a simple interface.


**Methods:**


### .add_data_by_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L22)
```python
.add_data_by_lme(
   lme_names, file
)
```

---
Adds data from the database to the model.
Based on a LME.

**Arguments**

* **lme_names**  : a list of LME names


**Returns**

None

### .calculate_factors
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L43)
```python
.calculate_factors()
```

---
Calculates the growth factors for the model
for all ocean sections (either grid or LME).

### .calculate_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L51)
```python
.calculate_growth_rate()
```

---
Calculates the growth rate for the model
for all ocean sections (either grid or LME).

### .create_section_dfs
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L59)
```python
.create_section_dfs()
```

---
Creates a dataframe for each section in the model.

### .construct_df_from_sections_for_date
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L66)
```python
.construct_df_from_sections_for_date(
   date
)
```

---
Constructs a dataframe from the data in the model for a given date.

**Arguments**

* **date**  : the date for which to construct the dataframe


**Returns**

a dataframe

### .plot_growth_rate_by_lme_bar
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L79)
```python
.plot_growth_rate_by_lme_bar(
   date, path = ''
)
```

---
Plots the growth rate for the model based on LME as a bar chart

### .plot_growth_rate_by_lme_global
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L98)
```python
.plot_growth_rate_by_lme_global(
   date, path = ''
)
```

---
Plots the growth rate fraction for all LME on a global map

### .calculate_mean_groth_rate_by_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L127)
```python
.calculate_mean_groth_rate_by_lme()
```

---
Calculates the mean growth rate for a LME for the whole
time period modelled.

### .plot_growth_rate_by_best_lme_as_line
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/seaweed_model.py/#L147)
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
