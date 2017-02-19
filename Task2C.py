from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    N=10

    # build list of stations with level over tol
    flooded_stations=stations_highest_rel_level(stations,N)
    
    # print the list
    for station in flooded_stations:
        print(station[0], station[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System *** \n")

    # Run Task2C
    run()

