import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt


def run():
    """Requirements for Task 2F"""
    DT = 2
    N = 5
    p = 4

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # Get the station objects out of the list of names
    risky_station_tuple = stations_highest_rel_level(stations, N)
    risky_stations = [s for s in stations for name, level in risky_station_tuple
                      if s.name == name]

    for station in risky_stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=DT))
        if len(dates) == 0 or len(levels) == 0:
            continue  # Deal with empty lists appearing
        plot_water_level_with_fit(station, dates, levels, p)
        plt.show()

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System *** \n")

    # Run Task2F
    run()
