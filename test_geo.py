import pytest
import floodsystem.geo


def test_haversine():
    assert floodsystem.geo.haversine(0) == 0
