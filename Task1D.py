from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    
    # Build list of all rivers mentioned in list of stations
    rivers=rivers_with_station(stations)
    
    print("\nNumber of rivers with monitoring station:", len(rivers))
    print("\nFirst 10 rivers with stations:", rivers[:10])

    # Print all the names of all the stations on three specific rivers
    print("\nStations on River Aire:", stations_by_river(stations, "River Aire"))
    print("\nStations on River Cam:", stations_by_river(stations, "River Cam"))
    print("\nStations on River Thames:", stations_by_river(stations, "Thames"))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System *** \n")

    # Run Task1D
    run()
