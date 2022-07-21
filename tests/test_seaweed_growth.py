"""
Tests the growth model
"""
from re import A
import pandas as pd
import pytest

from src.seaweed_growth import growth_factor_combination
from src.seaweed_growth import growth_factor_combination_single_value
from src.seaweed_growth import calculate_illumination_factor
from src.seaweed_growth import illumination_single_value
from src.seaweed_growth import calculate_temperature_factor
from src.seaweed_growth import temperature_single_value
from src.seaweed_growth import calculate_nutrient_factor
from src.seaweed_growth import nutrient_single_value
from src.seaweed_growth import calculate_salinity_factor
from src.seaweed_growth import salinity_single_value


def create_test_dataframe_reasonable_values():
    """
    Creates a reasonable test dataframe and returns it
    """
    df = pd.DataFrame()
    df['illumination'] = [50, 55, 65, 70, 0, 10, 5]
    df['temperature'] = [5, 15, 5, 10, 0.25, -1, 2]
    df["nitrate"] = [5, 15, 5, 10, 0, 1, 2]
    df["phosphate"] = [5, 15, 5, 10, 0, 1, 2]
    df["ammonium"] = [5, 15, 5, 10, 0, 1, 2]
    df['salinity'] = [25, 45, 5, 0, 30, 10, 20]
    return df

def create_test_dataframe_non_reasonable_values():
    """
    Creates a unreasonable test dataframe and returns it
    """
    df = pd.DataFrame()
    df['illumination'] = [25, 500, 5, 500000000, 0.25, -1, 2]
    df['temperature'] = [25, 50, 5000000000, 0, 0.25, -1, 2]
    df["nitrate"] = [5, 15, 5000000, 10, 0.25, -1, 2]
    df["phosphate"] = [5, 15, 500000000000, 10, 0.25, -1, 2]
    df["ammonium"] = [5, 1500000, 5, 10, 0.25, -1, 2]
    df['salinity'] = [25, 5000, 5, 0, 0.25, -1, 2]
    return df


def test_growth_factor_combination_single_value():
    """
    This tests the growth_factor_combination_single_value function
    by providing it with reasonable and unreasonable values.
    """
    # Test 1
    assert growth_factor_combination_single_value(1, 1, 1, 1) == 1
    # Test 2
    assert growth_factor_combination_single_value(1, 1, 1, 0) == 0
    # Test 3
    assert growth_factor_combination_single_value(1, 1, 1, 0.25) == 0.25
    # Test 4
    with pytest.raises(AssertionError):
        result = growth_factor_combination_single_value(1, 1, 1, -1) == -1
    # Test 5
    with pytest.raises(AssertionError):
        result = growth_factor_combination_single_value(1, 1, 1, 2) == 2


def test_growth_factor_combination_reasonable_values():
    """
    tests the function growth_factor_combination using
    reasonable values. This should run without errors.
    """
    test_df = create_test_dataframe_reasonable_values()
    illumination_factor = calculate_illumination_factor(test_df["illumination"])
    temperature_factor = calculate_temperature_factor(test_df["temperature"])
    nutrient_factor = calculate_nutrient_factor(test_df["nitrate"], test_df["phosphate"], test_df["ammonium"])
    salinity_factor = calculate_salinity_factor(test_df["salinity"])
    factors_combined = growth_factor_combination(illumination_factor,
                    temperature_factor, nutrient_factor, salinity_factor)
    assert factors_combined is not None
    assert isinstance(factors_combined, pd.Series)
    assert factors_combined.min() >= 0
    assert factors_combined.max() <= 1


def test_illumination_single_value():
    """
    Tests the illumination_single_value function
    with reasonable values. This should run without errors.
    """
    # Test 1
    assert illumination_single_value(25) == 1
    # Test 2
    assert illumination_single_value(500) == 100/500
    # Test 3
    assert illumination_single_value(5) == 5/21.9
    # Test 4: make sure everything stays between 0 and 1
    for illumination in range(0, 500):
        assert illumination_single_value(illumination) <= 1
        assert illumination_single_value(illumination) >= 0


def test_calculate_illumination_factor_unreasonable_values():
    """
    Tests the calculate_illumination_factor function
    This should fail
    """
    with pytest.raises(AssertionError):
        illumination_factor = calculate_illumination_factor(
            create_test_dataframe_non_reasonable_values()["illumination"])


def test_temperature_single_value():
    """
    Tests the temperature_single_value function
    Just makes sure that it stays between 0 and 1
    """
    # Test 1: make sure everything stays between 0 and 1
    for temperature in range(0, 50):
        assert temperature_single_value(temperature) <= 1
        assert temperature_single_value(temperature) >= 0

    # Test 2: temperature between 24 and 30
    assert temperature_single_value(25.0) == 1


def test_calculate_temperature_factor_unreasonable_values():
    """
    Tests the calculate_temperature_factor function
    This should fail
    """
    with pytest.raises(AssertionError):
        temperature_factor = calculate_temperature_factor(
            create_test_dataframe_non_reasonable_values()["temperature"])


def test_nutrient_single_value():
    """
    Tests the nutrient_single_value function
    Just makes sure that it stays between 0 and 1
    """
    # Test 1: make sure everything stays between 0 and 1
    for nutrient in range(0, 500):
        assert nutrient_single_value(nutrient, nutrient, nutrient) <= 1
        assert nutrient_single_value(nutrient, nutrient, nutrient) >= 0

def test_calculate_nutrient_factor_unreasonable_values():
    """
    Tests the calculate_nutrient_factor function
    This should fail
    """
    with pytest.raises(AssertionError):
        nutrient_factor = calculate_nutrient_factor(
            create_test_dataframe_non_reasonable_values()["nitrate"],
            create_test_dataframe_non_reasonable_values()["phosphate"],
            create_test_dataframe_non_reasonable_values()["ammonium"])

def test_salinity_single_value():
    """
    Tests the salinity_single_value function
    Just makes sure that it stays between 0 and 1
    """
    # Test 1: make sure everything stays between 0 and 1
    for salinity in range(0, 50):
        assert salinity_single_value(salinity) <= 1
        assert salinity_single_value(salinity) >= 0
    # Test 2: salinity between 24 and 36
    assert salinity_single_value(25) == 1


def test_calculate_salinity_factor_unreasonable_values():
    """
    Tests the calculate_salinity_factor function
    This should fail
    """
    with pytest.raises(AssertionError):
        salinity_factor = calculate_salinity_factor(
            create_test_dataframe_non_reasonable_values()["salinity"])