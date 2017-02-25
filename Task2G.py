import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import issue_warnings
import matplotlib.pyplot as plt


def run():
    """Requirements for Task 2G"""
    DT = 2
    N = 5
    p = 4

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    stations_by_risk = issue_warnings(stations)

    for s, riskv, risk in stations_by_risk:
        print((s.name, riskv, risk), "\n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System *** \n")

    # Run Task2G
    run()
