"""
Tests the growth model
"""
import sys
from pathlib import Path
import pytest

# Add the source directory to the path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.growth_model import growth_factor_combination

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

