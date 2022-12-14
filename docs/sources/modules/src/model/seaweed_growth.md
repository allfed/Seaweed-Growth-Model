#


### growth_factor_combination_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L25)
```python
.growth_factor_combination_single_value(
   illumination_factor: float, temperature_factor: float, nutrient_factor: float,
   salinity_factor: float
)
```

---
Calculates the actual production rate of the seaweed

**Arguments**

* **illumination_factor**  : the illumination factor
* **temperature_factor**  : the temperature factor
* **nutrient_factor**  : the nutrient factor
* **salinity_factor**  : the salinity factor


**Returns**

fraction of the actual production rate the seaweed could
reach in optimal circumstances

----


### growth_factor_combination
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L63)
```python
.growth_factor_combination(
   illumination_factor: pd.Series, temperature_factor: pd.Series,
   nutrient_factor: pd.Series, salinity_factor: pd.Series
)
```

---
Calculates the actual production rate of the seaweed for a whole dataframe
And returns it as a pandas series

**Arguments**

* **illumination_factor**  : the illumination factor
* **temperature_factor**  : the temperature factor
* **nutrient_factor**  : the nutrient factor
* **salinity_factor**  : the salinity factor


**Returns**

fraction of the actual production rate the seaweed could

----


### illumination_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L103)
```python
.illumination_single_value(
   illumination: float
)
```

---
Calculates the illumination factor for a single value based on an empirical model

**Arguments**

* **illumination**  : the illumination of the algae in W/m²


**Returns**

The illumination factor

----


### calculate_illumination_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L127)
```python
.calculate_illumination_factor(
   illumination: pd.Series
)
```

---
Calculates the illumination factor for a whole series

**Arguments**

* **illumination**  : the illumination of the algae in W/m²


**Returns**

The illumination factor as a pandas series

----


### temperature_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L138)
```python
.temperature_single_value(
   temperature: float
)
```

---
Calculates the temperature factor for a single value based on an empirical model

**Arguments**

* **temperature**  : the temperature of the water in °C


**Returns**

The temperature factor as a float

----


### calculate_temperature_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L164)
```python
.calculate_temperature_factor(
   temperature: pd.Series
)
```

---
Calculates the temperature factor for a whole dataframe column

**Arguments**

* **temperature**  : the temperature of the water in celcius


**Returns**

The temperature factor as a pandas series

----


### nitrate_subfactor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L176)
```python
.nitrate_subfactor(
   nitrate
)
```

---
Calculates the nitrate subfactor for a single value

**Arguments**

* **nitrate**  : the nitrate concentration in mmol/m³


**Returns**

The nitrate subfactor as a float

----


### phosphate_subfactor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L188)
```python
.phosphate_subfactor(
   phosphate
)
```

---
Calculates the phosphate subfactor for a single value

**Arguments**

* **phosphate**  : the phosphate concentration in mmol/m³


**Returns**

The phosphate subfactor as a float

----


### ammonium_subfactor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L200)
```python
.ammonium_subfactor(
   ammonium
)
```

---
Calculates the ammonium subfactor for a single value

**Arguments**

* **ammonium**  : the ammonium concentration in mmol/m³


**Returns**

The ammonium subfactor as a float

----


### calculate_nutrient_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L212)
```python
.calculate_nutrient_factor(
   nitrate: pd.Series, ammonium: pd.Series, phosphate: pd.Series
)
```

---
Calculates the nutrient factor for a whole series
And returns the nutrient factor as a pandas series

**Arguments**

* **nitrate**  : the nitrate concentration in mmol/m³
* **ammonium**  : the ammonium concentration in mmol/m³
* **phosphate**  : the phosphate concentration in mmol/m³


**Returns**

* **nutrient_factor**  : The nutrient factor as a pd.Series
    nitrate_subfactor: The nitrate subfactor as a pd.Series
    ammonium_subfactor: The ammonium subfactor as a pd.Series
    phosphate_subfactor: The phosphate subfactor as a pd.Series
List of:

----


### salinity_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L253)
```python
.salinity_single_value(
   salinity: float
)
```

---
Calculates the salinity factor for a single salinity value based on an empirical model

**Arguments**

* **salinity**  : the salinity of the water


**Returns**

The salinity factor as a float

----


### calculate_salinity_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L277)
```python
.calculate_salinity_factor(
   salinity: pd.Series
)
```

---
Calculates the salinity factor for a whole dataframe

**Arguments**

* **salinity**  : the salinity of the water in ppt


**Returns**

The salinity factor as a pandas series
