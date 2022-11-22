#


### get_parameter_dataframe
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L26)
```python
.get_parameter_dataframe(
   parameter, path, file
)
```

---
Initializes the seaweed model and returns the dataframe with the parameter
for all the grid sections

**Arguments**

* **parameter**  : the parameter to construct the dataframe for
* **path**  : The path to the file
* **file**  : The file name


**Returns**

* **df**  : pandas.DataFrame


----


### time_series_analysis
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L46)
```python
.time_series_analysis(
   growth_df, n_clusters, global_or_US
)
```

---
Does time series analysis on the dataframe
All the time serieses are clustered based on their
overall shape using k-means
Inspired by this article:
https://www.kaggle.com/code/izzettunc/introduction-to-time-series-clustering/notebook

**Arguments**

* **growth_df**  : pandas.DataFrame
* **n_clusters**  : int - the number of clusters to use


**Returns**

* **labels**  : list - the labels for each time series
* **km**  : TimeSeriesKMeans - the k-means object


----


### elbow_method
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L76)
```python
.elbow_method(
   growth_df, max_clusters, global_or_US
)
```

---
Finds the optimal number of clusters using the elbow method
https://predictivehacks.com/k-means-elbow-method-code-for-python/

**Arguments**

* **growth_df**  : pandas.DataFrame
* **max_clusters**  : int - the maximum number of clusters to try


**Returns**

None, just plots the elbow method and saves it

----


### area_cap
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L116)
```python
.area_cap(
   lat, radius = 6371.0
)
```

---
Area of a cap of radius r and latitude lat.


**Arguments**

* **lat**  : float
    Latitude of the cap in degrees.
* **radius**  : float, optional
    Radius of the sphere in km.
    Default is the radius of the Earth.


**Returns**

* **area**  : float
    Area of the cap in km^2.


----


### lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L167)
```python
.lme()
```

---
Calculates growth rate and all the factors for the lme
and saves it in files appropriate for the plotting functions

**Arguments**

None

**Returns**

None

----


### grid
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L207)
```python
.grid()
```

---
Calculates growth rate and all the factors for the grid
and saves it in files appropriate for the plotting functions

**Arguments**

None

**Returns**

None
