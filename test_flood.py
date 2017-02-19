import pytest
import floodsystem.flood
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    stations=build_station_list()
    update_water_levels(stations)
    for tol in [0.2, 0.5, 1, 2]:
        flooded_stations=stations_level_over_threshold(stations, tol)
        assert len(flooded_stations)<=len(stations)
        assert flooded_stations[0][1]>tol
        assert flooded_stations[-1][1]>tol

def test_stations_highest_rel_level():
    stations=build_station_list()
    update_water_levels(stations)
    for N in [1, 10, 500]:
        flooded_stations=stations_highest_rel_level(stations, N)
        assert len(flooded_stations)==N
        assert flooded_stations[0][1]>=flooded_stations[-1][1]
        
