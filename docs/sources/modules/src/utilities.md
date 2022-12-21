#


### prepare_geometry
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/utilities.py/#L9)
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
