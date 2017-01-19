from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    # Find distances of all stations from Cambridge
    close_stations = stations_within_radius(
        stations, (52.2053, 0.1218), 10)

    namelist = [station.name
                for station in close_stations]

    namelist = sorted(namelist)

    print(namelist)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System *** \n")

    # Run Task1C
    run()
