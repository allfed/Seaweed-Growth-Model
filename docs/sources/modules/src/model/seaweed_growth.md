#


### growth_factor_combination_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L22)
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
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L60)
```python
.growth_factor_combination(
   illumination_factor: pd.Series, temperature_factor: pd.Series,
   nutrient_factor: pd.Series, salinity_factor: pd.Series
)
```

---
Calculates the actual production rate of the seaweed for a whole dataframe
And returns it as a pandas series

----


### illumination_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L93)
```python
.illumination_single_value(
   illumination: float
)
```

---
Calculates the illumination factor for a single value

**Arguments**

* **illumination**  : the illumination of the algae in W/m²


**Returns**

The illumination factor

----


### calculate_illumination_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L117)
```python
.calculate_illumination_factor(
   illumination: pd.Series
)
```

---
Calculates the illumination factor for a whole series

----


### temperature_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L124)
```python
.temperature_single_value(
   temperature: float
)
```

---
Calculates the temperature factor

**Arguments**

* **temperature**  : the temperature of the water in °C


**Returns**

The temperature factor as a float

----


### calculate_temperature_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L150)
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


### nutrient_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L162)
```python
.nutrient_single_value(
   nitrate: float, ammonium: float, phosphate: float
)
```

---
Calculates the nutrient factor, which is the minimum of the
three nutrients nitrate, ammonium and phosphate for a single value

**Arguments**

* **nitrate**  : the nitrate concentration in mmol/m³
* **ammonium**  : the ammonium concentration in mmol/m³
* **phosphate**  : the phosphate concentration in mmol/m³


**Returns**

The nutrient factor as a float

----


### calculate_nutrient_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L198)
```python
.calculate_nutrient_factor(
   nitrate: pd.Series, ammonium: pd.Series, phosphate: pd.Series
)
```

---
Calculates the nutrient factor for a whole series
And returns the nutrient factor as a pandas series

----


### salinity_single_value
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L215)
```python
.salinity_single_value(
   salinity: float
)
```

---
Calculates the salinity factor for a single salinity value

----


### calculate_salinity_factor
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/src/model/seaweed_growth.py/#L235)
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
