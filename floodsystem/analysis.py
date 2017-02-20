import dateutil.parser
import datetime
import numpy as np
from .stationdata import build_station_list, update_water_levels
from .datafetcher import fetch_measure_levels
import matplotlib
import matplotlib.dates
import scipy as sp
import scipy.misc


def issue_warnings(p=4, dt=10):
    """Returns a list of all stations alongside an assesment of their flood warning risk 
    based on their current and historical water levels. Uses a polynomial of degree p for estimation
    with a history of dt days."""
    stations = build_station_list()
    update_water_levels(stations)
    stations_by_risk = []

    for s in stations:
        if not s.typical_range_consistent():
            pass

        dates, levels = fetch_measure_levels(
            s.measure_id, dt=datetime.timedelta(days=dt))
        times = matplotlib.date.date2num(dates)
        # f is a function representing water levels over time, and its
        # derivatives are computed.
        f, offset = polyfit(dates, levels, p)
        df = f.deriv()
        d2f = f.deriv(2)
        rel_level = s.relative_water_level()
        # TODO: Use the derivatives to score each stations risk, and then
        # assign a severity either based on absolute values or relative to
        # other stations.


def polyfit(dates, levels, p):
    """Returns a polynomial of degree p representing the best fit for a function
    f(dates) = levels. It offsets dates such that the minimum value of the domain
    is equal to 0 to prevent floating point errors. The offset is returned alongside
    the polynomial as (polynomial,offset)."""
    times = matplotlib.dates.date2num(dates)
    d0 = np.min(times)
    times = times - d0
    poly = np.poly1d(np.polyfit(times, levels, p))

    return poly, d0


def Bernstein(i, n):
    """Returns the ith basis Bernstein polynomial of degree n"""
    c = sp.special.binom(n, i)

    def f(x):
        return c * (x**i) * ((1 - x)**(n - i))

    return f
