import numpy as np
import pytest

from src.processing.postprocessing import area_cap, area_grid_cell


def test_area_cap():
    """Integration and unit tests for area_cap function."""
    EARTH_RADIUS = 6371.0
    # INTEGRATION TESTS

    # area of a cap at the equator is half the area of the sphere
    assert area_cap(0) == 4 * np.pi * EARTH_RADIUS**2 / 2.0

    # area of a cap at the north pole is 0
    assert area_cap(90) == 0

    # area of a cap at the south pole is the whole sphere
    assert area_cap(-90) == 4 * np.pi * EARTH_RADIUS**2

    # UNIT TESTS

    # NaN returns NaN
    assert np.isnan(area_cap(np.nan))

    # Inf returns NaN
    assert np.isnan(area_cap(np.inf))


def test_area_grid_cell():
    """Integration, unit, and vector unit tests
    for the area_grid_cell function."""
    EARTH_RADIUS = 6371.0
    # -----------------------------------------------------

    # INTEGRATION TESTS

    # EQUATOR TEST
    # at the equator on side of the grid cell is one Earth circumference
    # divided by 360 degrees
    assert np.sqrt(area_grid_cell(0.0, 6371)) * 360.0 == pytest.approx(
        2 * np.pi * 6371.0, abs=1.0
    )

    # POLE TEST
    # at the poles, approximate the area of the cap as a circle with radius
    # = sin(0.5 deg) * radius of the Earth
    # then divide by 360 to get area of one grid cell

    approx_cell_area = np.pi * (np.sin(0.5 / 180 * np.pi) * EARTH_RADIUS) ** 2 / 360.0
    precise_cell_area = area_grid_cell(90.0, 6371)

    # approximation is good to 0.1 km^2
    assert approx_cell_area == pytest.approx(precise_cell_area, abs=0.1)

    # NEAR THE NORTH POLE TEST
    # same a before but with a grid cell centered at 89.5 degrees
    approx_cell_area = np.pi * (np.sin(1.0 / 180 * np.pi) * EARTH_RADIUS) ** 2 / 360.0
    precise_cell_area = area_grid_cell(89.5, 6371)

    # approximation is good to 0.1 km^2
    assert approx_cell_area == pytest.approx(precise_cell_area, abs=0.1)

    # NEAR THE SOUTH POLE TEST
    # same a before but with a grid cell centered at -89.5 degrees
    approx_cell_area = np.pi * (np.sin(1.0 / 180 * np.pi) * EARTH_RADIUS) ** 2 / 360.0
    precise_cell_area = area_grid_cell(-89.5, 6371)

    # approximation is good to 0.1 km^2
    assert approx_cell_area == pytest.approx(precise_cell_area, abs=0.1)

    # ------------------------------------------------------------

    # UNIT TESTS

    # test that values outside of the range [-90, 90] are invalid
    with pytest.raises(AssertionError):
        area_grid_cell(-100.0)

    with pytest.raises(AssertionError):
        area_grid_cell(100.0)

    # test that NaNs are invalid
    with pytest.raises(AssertionError):
        area_grid_cell(np.nan)

    # test that Infs are invalid
    with pytest.raises(AssertionError):
        area_grid_cell(np.inf)

    # ------------------------------------------------------------

    # VECTOR UNIT TESTS

    # test that you can pass an array of latitudes
    assert (
        area_grid_cell(np.array([0.0, 45.0, 90.0]))
        == np.array([area_grid_cell(0.0), area_grid_cell(45.0), area_grid_cell(90.0)])
    ).all()

    # test that you can pass a list of latitudes
    assert (
        area_grid_cell([0.0, 45.0, 90.0])
        == np.array([area_grid_cell(0.0), area_grid_cell(45.0), area_grid_cell(90.0)])
    ).all()

    # test that you can pass a tuple of latitudes
    assert (
        area_grid_cell((0.0, 45.0, 90.0))
        == np.array([area_grid_cell(0.0), area_grid_cell(45.0), area_grid_cell(90.0)])
    ).all()

    # test that if you pass one invalid latitude, the whole array is invalid
    with pytest.raises(AssertionError):
        area_grid_cell(np.array([0.0, 45.0, 100.0]))

    # test that if you pass one invalid latitude, the whole array is invalid
    with pytest.raises(AssertionError):
        area_grid_cell(np.array([0.0, 45.0, np.nan]))
