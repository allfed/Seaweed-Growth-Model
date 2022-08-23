#


## DataLME
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/read_files.py/#L7)
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


### .read_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/read_files.py/#L23)
```python
.read_data()
```

---
read in the file

### .sort_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/read_files.py/#L29)
```python
.sort_data()
```

---
Sorts as a dictionary of pandas dataframes
The data is ocean data after nuclear war seperated by
Large Marine Ecosystems (LME)

### .provide_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/read_files.py/#L58)
```python
.provide_data(
   lme_number
)
```

---
Provides the data for a given LME

**Arguments**

* **lme_number**  : the LME number


**Returns**

a dataframe
