#


### prepare_geometry
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/utilities.py/#L11)
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


### weighted_quantile
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/utilities.py/#L35)
```python
.weighted_quantile(
   data: pd.Series, weights: pd.Series, quantile: float
)
```

---
Calculates the weighted quantile of s1 based on s2

**Arguments**

* **data**  : pandas.Series - the series to calculate the quantile for
* **weights**  : pandas.Series - the series to use as weights
* **quantile**  : float - the quantile to calculate


**Returns**

float - the weighted quantile
