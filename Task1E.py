from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()
    print(rivers_by_station_number(stations, 10))
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System *** \n")

    # Run Task1D
    run()
