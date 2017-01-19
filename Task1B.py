from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    distance_list = stations_by_distance(
        stations, (52.2053, 0.1218))

    namelist = []
    for pair in distance_list:
        station, distance = pair
        namelist.append((station.name, distance))

    print(namelist[:10])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")

    # Run Task1B
    run()
