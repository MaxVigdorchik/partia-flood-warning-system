from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime


def run():
    """Requirements for Task 2E"""

    N = 6
    dt = 10

    stations = build_station_list()
    update_water_levels(stations)

    # build list of tuples of looded stations
    flooded_stations_tuples = stations_highest_rel_level(stations, N)

    # the following essentially converts the list of tuples into a list of stations.
    # This is necessary as we need the measure_id
    flooded_stations = []
    for station_tuple in flooded_stations_tuples:
        for station in stations:
            if station.name == station_tuple[0]:
                flooded_stations.append(station)
                break

    print(flooded_stations)

    # plot data for each station
    for station in flooded_stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)
        plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System *** \n")

    # Run Task2E
    run()
