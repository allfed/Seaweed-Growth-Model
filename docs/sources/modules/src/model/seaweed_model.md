#


## SeaweedModel
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L10)
```python 

```


---
Wrapper class that encapsulates the model
and is meant to provide a simple interface.


**Methods:**


### .add_data_by_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L21)
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

### .add_data_by_grid
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L41)
```python
.add_data_by_grid(
   file
)
```

---
Adds data from the database to the model.
Based on a grid.

**Arguments**

* **lat_lons**  : a list of lat_lon tuples
* **file**  : the file to read the data from


**Returns**

None

### .calculate_factors
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L62)
```python
.calculate_factors()
```

---
Calculates the growth factors for the model
for all ocean sections (either grid or LME).

### .calculate_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L70)
```python
.calculate_growth_rate()
```

---
Calculates the growth rate for the model
for all ocean sections (either grid or LME).

### .create_section_dfs
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L78)
```python
.create_section_dfs()
```

---
Creates a dataframe for each section in the model.

### .construct_df_from_sections_for_date
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L85)
```python
.construct_df_from_sections_for_date(
   months
)
```

---
Constructs a dataframe from the data in the model for a given date.
This uses the months since the beginning of the nuclear war.
Mininum is -3, as the data starts before the war.
Maximum is 357, as the data ends after the war.

**Arguments**

* **min_months**  : the number of months since the beginning of the war (start date)
* **max_months**  : the number of months since the beginning of the war (end date)


**Returns**

a dataframe

### .construct_df_for_parameter
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_model.py/#L102)
```python
.construct_df_for_parameter(
   parameter
)
```

---
Constructs a dataframe that contains complete time series of a given
parameter for all sections in the model.

**Arguments**

* **parameter**  : the parameter to construct the dataframe for


**Returns**

a dataframe with the date as index and the sections as columns
