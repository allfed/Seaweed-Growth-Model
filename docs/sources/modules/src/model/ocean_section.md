#


## OceanSection
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L11)
```python 
OceanSection(
   name, data
)
```


---
Class the represents a section of the ocean.
alculates for every section how quickly seaweed can grow
and also saves the single factors for growth


**Methods:**


### .calculate_factors
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L36)
```python
.calculate_factors()
```

---
Calculates the factors and growth rate for the ocean section

**Arguments**

None

**Returns**

None

### .calculate_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L52)
```python
.calculate_growth_rate()
```

---
Calculates the growth rate for the ocean section

**Arguments**

None

**Returns**

None

### .create_section_df
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L68)
```python
.create_section_df()
```

---
Creates a dataframe that contains all the data for a given section
This can only be run once the factors have been calculated

**Arguments**

None

**Returns**

None

### .calculate_mean_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L107)
```python
.calculate_mean_growth_rate()
```

---
Calculates the mean growth rate and returns it

**Arguments**

None

**Returns**

the mean growth rate of the section

### .select_section_df_date
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/ocean_section.py/#L120)
```python
.select_section_df_date(
   month
)
```

---
Selectes a date from the section df and returns it

**Arguments**

* **date**  : the date to select


**Returns**

the dataframe for the date
