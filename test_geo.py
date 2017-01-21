import pytest
import floodsystem.geo
from floodsystem.geo import spherical_distance, stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number
import numpy as np
from floodsystem.stationdata import build_station_list
from hypothesis import given, assume
from hypothesis.strategies import floats
import math


def test_haversine():
    """Unit tests for haversine"""
    assert floodsystem.geo.haversine(0) == 0
    assert round(floodsystem.geo.haversine(np.pi), 8) == 1


def test_spherical_distance():
    """Tests properties of distance like distance from point to itself is 0"""
    assert spherical_distance((25, 25), (25, 25)) == 0
    assert spherical_distance(
        (1, 2), (2, 1)) == spherical_distance((2, 1), (1, 2))


def test_stations_by_distance():
    """Ensures that stations are sorted correctly by distance"""
    stations = build_station_list()
    mylist = stations_by_distance(stations, (0, 0))

    for i in range(2, len(stations)):
        # Not sure if python allows double indexing so I do this
        station1, distance1 = mylist[i]
        station2, distance2 = mylist[i - 1]
        assert distance2 <= distance1


@given(floats(), floats(min_value=-90, max_value=90), floats(min_value=-180, max_value=180))
def test_stations_within_radius(r, lat, lon):
    """Tests a few edge cases (e.g. radius 0 or empty station list) for the stations within radius
    function. Also ensures randomly generated radii are obeyed by the results"""
    assume(not (math.isnan(r) or math.isnan(lat) or math.isnan(lon)))

    stations = build_station_list()
    assert stations_within_radius([], (25, 25), 10) == []
    assert stations_within_radius(stations, (50, 0), 0) == []
    for s in stations_within_radius(stations, (lat, lon), r):
        assert spherical_distance(s.coord, (lat, lon)) <= r

def test_rivers_with_station():
    """Tests that the function has at least 800 rivers inc. Thames"""
    stations = build_station_list()
    rivers=rivers_with_station(stations)
    assert len(rivers)>=800 #number of rivers with station should be 843 as of 21/01/2017 but this may change so check it is above 800
    assert "Thames" in rivers

def test_stations_by_river():
    """Check that certain stations are produced in the list for certain rivers"""
    stations = build_station_list()
    assert "Armley" in stations_by_river(stations, "River Aire")
    assert "Benson Lock" in stations_by_river(stations, "Thames")
    
def test_rivers_by_station_number():
    """Tests the length of a few outputs and checks order of rivers"""
    stations = build_station_list()
    #the length can be greater than the value of N if the next rivers have the same number of stations
    assert len(rivers_by_station_number(stations, 1))>=1
    assert len(rivers_by_station_number(stations, 10))>=10
    assert len(rivers_by_station_number(stations, 30))>=30
    biggest_river=rivers_by_station_number(stations, 1)
    assert biggest_river[0][0]=="Thames"
