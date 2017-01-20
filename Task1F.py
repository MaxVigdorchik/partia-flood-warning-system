from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    # Construct a list of stations with inconsistent highs and/or lows
    inconsistent = [
        s.name for s in inconsistent_typical_range_stations(stations)]

    print(sorted(inconsistent))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System *** \n")

    # Run Task1C
    run()
