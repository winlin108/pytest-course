from scripts.chp2.video4.mapmaker_challenge import Point, Map
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp.value) == "Invalid latitude, longitude combination."


def test_invalid_point_name():
    with pytest.raises(TypeError) as exp:
        Point(12345, 70.6937, 89.44406)
    assert str(exp.value) == "Invalid name. Name must be string."


def test_map_point_added():
    p1 = Point("Dakar", 14.7167, 17.4677)
    m1 = Map("Africa", [p1])
    assert m1.get_points() == [p1]


