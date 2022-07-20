"""
Tests the growth model
"""
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



def test_growth_factor_combination_single_value():
    """
    Tests the growth_factor combination
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


def test_illumination_single_value():
    """
    Tests the illumination_single_value function
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


def test_temperature_single_value():
    """
    Tests the temperature_single_value function
    """
    # Test 1: make sure everything stays between 0 and 1
    for temperature in range(0, 50):
        assert temperature_single_value(temperature) <= 1
        assert temperature_single_value(temperature) >= 0

    # Test 2: temperature between 24 and 30
    assert temperature_single_value(25.0) == 1


def test_nutrient_single_value():
    """
    Tests the nutrient_single_value function
    """
    # Test 1: make sure everything stays between 0 and 1
    for nutrient in range(0, 500):
        assert nutrient_single_value(nutrient, nutrient, nutrient) <= 1
        assert nutrient_single_value(nutrient, nutrient, nutrient) >= 0


def test_salinity_single_value():
    """
    Tests the salinity_single_value function
    """
    # Test 1: make sure everything stays between 0 and 1
    for salinity in range(0, 100):
        assert salinity_single_value(salinity) <= 1
        assert salinity_single_value(salinity) >= 0
    # Test 2: salinity between 24 and 36
    assert salinity_single_value(25) == 1


    
