#


### get_area
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L11)
```python
.get_area(
   path, file
)
```

---
Gets the file with all the areas for grid_cells and saves it as a csv

**Arguments**

* **path**  : path to the file
* **file**  : filename


**Returns**

None

----


### prepare_gridded_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/preprocessing.py/#L31)
```python
.prepare_gridded_data(
   path, folder, scenario, file_ending, global_or_US
)
```

---
Reads in the pickles of the geodataframes of the
different environmental paramters. Checks if they
all have the same geometry and reorders them to fit
the rest of the code.

**Arguments**

* **path**  : the path for the pickled files
* **folder**  : the folder where the pickled files are
* **file_ending**  : the ending of the pickled files
* **global_or_US**  : if "global", the global data is used
* **scenario**  : the scenario to use (e.g. 150tg)


**Returns**

None, but saves a pickle of the dictionary of geo
dataframes. Each geodataframe is assigned a key
consisting of a tuple of floats of the latitude
and longitude.
