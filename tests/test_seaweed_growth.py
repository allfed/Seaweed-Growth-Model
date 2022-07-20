"""
Tests the growth model
"""
import sys
from pathlib import Path
import pytest

# Add the source directory to the path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.seaweed_growth import growth_factor_combination
from src.seaweed_growth import calculate_illumination_factor
from src.seaweed_growth import calculate_temperature_factor
from src.seaweed_growth import calculate_nutrient_factor
from src.seaweed_growth import calculate_salinity_factor
from src.seaweed_growth import calculate_self_shading_factor


def test_growth_factor_combination():
    """
    Tests the growth_factor combination
    """
    # Test 1
    assert growth_factor_combination(1, 1, 1, 1, 1, 1) == 1
    # Test 2
    assert growth_factor_combination(1, 1, 1, 1, 1, 0) == 0
    # Test 3
    assert growth_factor_combination(1, 1, 1, 1, 1, 0.25) == 0.25
    # Test 4
    with pytest.raises(AssertionError):
        result = growth_factor_combination(1, 1, 1, 1, 1, -1) == -1
    # Test 5
    with pytest.raises(AssertionError):
        result = growth_factor_combination(1, 1, 1, 1, 1, 2) == 2

def test_calculate_illumination_factor():
    """
    Tests the calculate_illumination_factor function
    """
    # Test 1
    assert calculate_illumination_factor(25) == 1
    # Test 2
    assert calculate_illumination_factor(500) == 100/500
    # Test 3
    assert calculate_illumination_factor(5) == 5/21.9
    # Test 4: make sure everything stays between 0 and 1
    for illumination in range(0, 500):
        assert calculate_illumination_factor(illumination) <= 1
        assert calculate_illumination_factor(illumination) >= 0


def test_calculate_temperature_factor():
    """
    Tests the calculate_temperature_factor function
    """
    # Test 1: make sure everything stays between 0 and 1
    for temperature in range(0, 50):
        assert calculate_temperature_factor(temperature) <= 1
        assert calculate_temperature_factor(temperature) >= 0

    # Test 2: temperature between 24 and 30
    assert calculate_temperature_factor(25) == 1


def test_calculate_nutrient_factor():
    """
    Tests the calculate_nutrient_factor function
    """
    # Test 1: make sure everything stays between 0 and 1
    for nutrient in range(0, 500):
        assert calculate_nutrient_factor(nutrient, nutrient, nutrient) <= 1
        assert calculate_nutrient_factor(nutrient, nutrient, nutrient) >= 0


def test_calculate_salinity_factor():
    """
    Tests the calculate_salinity_factor function
    """
    # Test 1: make sure everything stays between 0 and 1
    for salinity in range(0, 100):
        assert calculate_salinity_factor(salinity) <= 1
        assert calculate_salinity_factor(salinity) >= 0
    # Test 2: salinity between 24 and 36
    assert calculate_salinity_factor(25) == 1


def test_calculate_self_shading_factor():
    """
    Tests the calculate_self_shading_factor function
    """
    # Test 1: make sure everything stays between 0 and 1
    for self_shading in range(0, 50):
        assert calculate_self_shading_factor(self_shading) <= 1
        assert calculate_self_shading_factor(self_shading) >= 0
    # Test 2: self_shading between 24 and 36
    assert calculate_self_shading_factor(0.3) == 1
    
