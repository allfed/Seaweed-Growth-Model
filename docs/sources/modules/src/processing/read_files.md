#


## DataLME
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L10)
```python 
DataLME(
   file
)
```


---
Creates a data object for the LME
Meant to only read in the data once
and provide the data for each LME as needed


**Methods:**


### .read_data_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L26)
```python
.read_data_lme()
```

---
read in the file

**Arguments**

None

**Returns**

None

### .sort_data_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L36)
```python
.sort_data_lme()
```

---
Sorts as a dictionary of pandas dataframes
The data is ocean data after nuclear war seperated by
Large Marine Ecosystems (LME)

**Arguments**

None

**Returns**

None

### .provide_data_lme
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L69)
```python
.provide_data_lme(
   lme_number
)
```

---
Provides the data for a given LME

**Arguments**

* **lme_number**  : the LME number


**Returns**

a dataframe

----


## DataGrid
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L80)
```python 
DataGrid(
   file
)
```


---
Creates a data object for the gridded data
Meant to only read in the data once
and provide the data for each grid cell as needed


**Methods:**


### .read_data_grid
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L96)
```python
.read_data_grid()
```

---
Reads in the gridded data

**Arguments**

None

**Returns**

None

### .provide_data_grid
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L107)
```python
.provide_data_grid(
   lat_lon
)
```

---
Provides the data for a given grid cell

**Arguments**

* **lat_lon**  : the lat_lon coordinates as tuple of floats


**Returns**

a geodataframe with all the environmental data
for this grid cell

----


### read_area_file
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/processing/read_files.py/#L119)
```python
.read_area_file(
   path, file
)
```

---
Reads in the area file

**Arguments**

* **file**  : the file to read in


**Returns**

a dataframe with the area of each LME
