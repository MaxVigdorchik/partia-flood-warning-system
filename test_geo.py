import pytest
import floodsystem.geo
import numpy as np
from floodsystem.stationdata import build_station_list


def test_haversine():
    """Unit tests for haversine"""
    assert floodsystem.geo.haversine(0) == 0
    assert round(floodsystem.geo.haversine(np.pi), 8) == 1


def test_stations_by_distance():
    """Ensures that stations are sorted correctly by distance"""
    stations = build_station_list()
    mylist = floodsystem.geo.stations_by_distance(stations, (0, 0))

    for i in range(2, len(stations)):
        # Not sure if python allows double indexing so I do this
        station1, distance1 = mylist[i]
        station2, distance2 = mylist[i - 1]
        assert distance1 >= distance2
