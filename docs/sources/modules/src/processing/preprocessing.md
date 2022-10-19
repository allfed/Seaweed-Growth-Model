#


### prepare_gridded_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L13)
```python
.prepare_gridded_data(
   path
)
```

---
Reads in the pickles of the geodataframes of the
different environmental paramters. Checks if they
all have the same geometry and reorders them to fit
the rest of the code.


**Arguments**

* **path**  : the path for the pickled files


**Returns**

None, but saves a pickle of the dictionary of geo
dataframes. Each geodataframe is assigned a key
consisting of a tuple of floats of the latitude
and longitude.

----


### prep_nw_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L89)
```python
.prep_nw_data(
   path, file, min_lat, max_lat, min_lon, max_lon, length_time, env_param,
   all_cells = False
)
```

---
### This code is only used on the NCAR cluster. ###

Reads the nuclear war data from Cheryls workspace.
Creates a geopandas dataframe for it for a given
environmental parameter and saves it in cwd as a pickle.


**Arguments**

* **path**  : path to the file
* **file**  : file name
* **min_lon**  : index of the minimal longitude to sample from
* **max_lon**  : index of the maximal longitude to sample from
* **min_lat**  : index of the minimal latitude to sample from
* **max_lat**  : index of the maximal latitude to sample from
* **length_time**  : how much of the original dataset should
             be used. Measured in month, max = 300
* **env_param**  : the environmental parameter to look at
* **all_cells**  : if True, all cells are used, if False, only selection


**Returns**

None

----


### call_prep_nw_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L149)
```python
.call_prep_nw_data()
```


----


### create_seaweed_land_buffer
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L169)
```python
.create_seaweed_land_buffer(
   file_countries, file_harbors, buffer_country, buffer_harbor
)
```

---
Creates a buffer around harbors and countries and saves it GeoJSON.


**Arguments**

* **file_countries**  : path to the file with the countries
* **file_harbors**  : path to the file with the harbors
* **buffer_harbor**  : size buffer around harbors (km)
* **buffer_country**  : size buffer around countries (km)

