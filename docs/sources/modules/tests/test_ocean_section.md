#


### create_test_dataframe_reasonable_values
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L10)
```python
.create_test_dataframe_reasonable_values()
```

---
Creates a reasonable test dataframe and returns it

----


### test_initialization
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L25)
```python
.test_initialization()
```

---
Tests if the Ocean Section class can create an instance

----


### test_get_section_data
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L35)
```python
.test_get_section_data()
```

---
Tests if the Ocean Section class can get the data from the database

----


### test_calculate_factors
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L49)
```python
.test_calculate_factors()
```

---
Tests if the ocean section class can calculate the factors from the data

----


### test_calculate_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L62)
```python
.test_calculate_growth_rate()
```

---
Tests if the ocean section class can calculate the growth rate

----


### test_create_section_df
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L73)
```python
.test_create_section_df()
```

---
Tests if the ocean section class can create a dataframe from the data

----


### test_failed_creation_section_df
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L85)
```python
.test_failed_creation_section_df()
```

---
Tests if the creation of the dataframe failes when the
factors have not been calculated

----


### test_select_section_df_date
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L96)
```python
.test_select_section_df_date()
```

---
Tests if a dataframe can be selected by date

----


### test_select_section_df_date_fail
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L109)
```python
.test_select_section_df_date_fail()
```

---
Tests if a dataframe can be selected by date
if the section df has not yet been created

----


### test_calculate_mean_growth_rate
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/tests/test_ocean_section.py/#L122)
```python
.test_calculate_mean_growth_rate()
```

---
Tests if the mean growth rate can be calculated
