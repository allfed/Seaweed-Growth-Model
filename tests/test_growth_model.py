"""
Tests the growth model
"""

from growth_model import growth_factor_combination


def test_growth_factor_combination():
    """
    Tests the growth_factor combination
    """
    # Test 1
    assert growth_factor_combination(1, 1, 1, 1, 1, 1) == 1
    # Test 2
    assert growth_factor_combination(1, 1, 1, 1, 1, 0) == 0
    # Test 3
    assert growth_factor_combination(1, 1, 1, 1, 0, 1) == 0
    # Test 4
    assert growth_factor_combination(1, 1, 1, 0, 1, 1) == 0
    # Test 5
    assert growth_factor_combination(1, 1, 0, 1, 1, 1) == 0
    # Test 6
    assert growth_factor_combination(1, 0, 1, 1, 1, 1) == 0
    # Test 7
    assert growth_factor_combination(0, 1, 1, 1, 1, 1) == 0
    
    # Test 8
    assert growth_factor_combination(1, 1, 1, 1, 1, 0.5) == 0.5
    # Test 9
    assert growth_factor_combination(1, 1, 1, 1, 0.5, 1) == 0.5
    # Test 10
    assert growth_factor_combination(1, 1, 1, 0.5, 1, 1) == 0.5
    # Test 11
    assert growth_factor_combination(1, 1, 0.5, 1, 1, 1) == 0.5
    # Test 12
    assert growth_factor_combination(1, 0.5, 1, 1, 1, 1) == 0.5
    # Test 13
    assert growth_factor_combination(0.5, 1, 1, 1, 1, 1) == 0.5
    
    # Test 14
    assert growth_factor_combination(1, 1, 1, 1, 1, 0.25) == 0.25
    # Test 15
    assert growth_factor_combination(1, 1, 1, 1, 0.25, 1) == 0.25
    # Test 16
    assert growth_factor_combination(1, 1, 1, 0.25, 1, 1) == 0.25
    # Test 17
    assert growth_factor_combination(1, 1, 0.25, 1, 1, 1) == 0.25
    # Test 18
    assert growth_factor_combination(1, 0.25, 1, 1, 1, 1) == 0.25
    # Test 19
    assert growth_factor_combination(0.25, 1, 1, 1, 1, 1) == 0.25
    
    # Test 20
    assert growth_factor_combination(1, 1, 1, 1, 1, 0.125) == 0.125
    # Test 21
    assert growth_factor_combination(1, 1, 1, 1, 0.125, 1) == 0.125
    # Test 22
    assert growth_factor_combination(1, 1, 1, 0.125, 1, 1) == 0.125