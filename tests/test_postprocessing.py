import pandas as pd
import pytest

from src.utilities import weighted_quantile


def test_weighted_quantile():
    """
    Tests the weighted quantile function
    """
    # Generate two pandas series with 5 values each
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([0.5, 1.5, 2, 0.5, 1])
    # calculate the weighted quantile
    assert weighted_quantile(s1, s2, 0.5) == 3

    # Generate two pandas series with 5 values each
    s3 = pd.Series([1, 2, 9, 3.2, 4])
    s4 = pd.Series([0.0, 0.5, 1.0, 0.3, 0.5])

    # calculate the weighted quantile
    assert weighted_quantile(s3, s4, 0.1) == 2
    assert weighted_quantile(s3, s4, 0.9) == 9

    # make sure it fails with wrong input
    with pytest.raises(AssertionError):
        weighted_quantile(s3, s4, 1.1)
    with pytest.raises(AssertionError):
        weighted_quantile(s3, s4, -0.1)
    with pytest.raises(AssertionError):
        weighted_quantile(s3, s4, "a")
    with pytest.raises(AssertionError):
        weighted_quantile([0, 1], s4, 0)
    with pytest.raises(AssertionError):
        weighted_quantile(s1, s2.iloc[2:], 0)
