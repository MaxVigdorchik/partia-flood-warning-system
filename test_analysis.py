from floodsystem.analysis import polyfit, Bernstein
import numpy as np
import datetime
import pytest
from floodsystem.geo import spherical_distance, stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from hypothesis import given, assume
from hypothesis.strategies import floats, integers
from floodsystem.datafetcher import fetch_measure_levels
import math


@given(integers(min_value=1, max_value=20), integers(min_value=0, max_value=6))
def test_polyfit(dt, p):
    """Tests that results from the polyfit function are well behaved to some extent"""
    test_station = build_station_list()[0]
    dates, levels = fetch_measure_levels(
        test_station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)
