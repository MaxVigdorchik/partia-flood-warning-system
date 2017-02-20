"""Several tests for the plot module"""
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def test_plot_water_levels():
    """Checks that the plot_water_levels function throws no erros with several inputs"""

    stations=build_station_list()
    update_water_levels(stations)

    #choose a few random stations and test
    for N in [1, 10, 100]:
        station=stations[N]
        dt=10
        dates,levels=fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)
