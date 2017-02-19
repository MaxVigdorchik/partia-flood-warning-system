from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt

def run():
    """Requirements for Task 2E"""

    N=6
    dt=10

    stations=build_station_list()
    update_water_levels(stations)
    flooded_stations_tuples=stations_highest_rel_level(stations, N)

    #the following essentially converts the list of tuples into a list of stations.
    #This is necessary as we need the measure_id
    flooded_stations=[]
    for station in stations:
        for flooded_station in flooded_stations_tuples:
            if flooded_station[0]==station.name:
                flooded_stations.append(station)
                
    print(flooded_stations)
    for station in flooded_stations:
        dates,levels=fetch_measure_levels(station.measure_id, timedelta(days=dt))
        plot_water_levels(station, dates,levels)
        plt.show()
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System *** \n")

    # Run Task2E
    run()
