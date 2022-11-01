#


### get_parameter_dataframe
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L19)
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
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L39)
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
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/postprocessing.py/#L70)
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
