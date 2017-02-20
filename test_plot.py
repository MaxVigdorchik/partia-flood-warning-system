"""Several tests for the plot module"""
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from hypothesis import given, assume
import datetime
from hypothesis.strategies import floats, integers


def test_plot_water_levels():
    """Checks that the plot_water_levels function throws no erros with several inputs"""

    stations = build_station_list()
    update_water_levels(stations)

    # choose a few random stations and test
    for N in [1, 10, 100]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


@given(integers(min_value=1, max_value=20))
def test_plot_water_level_with_fit(p):
    stations = build_station_list()
    update_water_levels(stations)

    # choose a few arbitrary stations and test
    for N in [1, 10, 100]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)
