import pytest

from delivery.calculations import calculate_distance_cost, calculate_size_cost, calculate_fragility_cost, \
    calculate_load_multiplier
from delivery.enums import Size, LoadMultiplier


@pytest.mark.parametrize("distance, expected", [
    (0.002, 50),
    (2, 50),
    (2.001, 100),
    (10, 100),
    (10.001, 200),
    (30, 200),
    (30.001, 300),
])
def test_calculate_distance_cost(distance, expected):
    assert calculate_distance_cost(distance) == expected


@pytest.mark.parametrize("distance, fragile", [(35, True), ])
def test_calculate_distance_cost_raises(distance, fragile):
    with pytest.raises(ValueError, match="Fragile items cannot be delivered for distances over 30 km."):
        calculate_distance_cost(distance, fragile)


@pytest.mark.parametrize("distance", [(-1), ])
def test_calculate_distance_cost_for_negative_number(distance):
    with pytest.raises(ValueError, match="Distance must be a non-negative number."):
        calculate_distance_cost(distance)


@pytest.mark.parametrize("distance", [0.001, ])
def test_calculate_distance_cost_for_negative_number(distance):
    with pytest.raises(ValueError, match=f"Item cannot be delivered to distance {distance}"):
        calculate_distance_cost(distance)


@pytest.mark.parametrize("size, expected", [(Size.BIG, 200), ])
def test_calculate_size_cost(size, expected):
    assert calculate_size_cost(size) == expected


@pytest.mark.parametrize("size", ['medium', ])
def test_calculate_size_cost_raises(size):
    with pytest.raises(ValueError, match="Value must be a member of Size."):
        calculate_size_cost(size)


@pytest.mark.parametrize("fragile, expected", [(False, 0), (True, 300), ])
def test_calculate_fragility_cost(fragile, expected):
    assert calculate_fragility_cost(fragile) == expected


@pytest.mark.parametrize("load_level, expected", [
    (LoadMultiplier.VERY_HIGH, 1.6),
    ('extreme', 1),
    (None, 1),
])
def test_calculate_load_multiplier(load_level, expected):
    assert calculate_load_multiplier(load_level) == expected
