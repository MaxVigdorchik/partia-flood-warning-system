import dateutil.parser
import datetime
import numpy as np
from .stationdata import build_station_list
import matplotlib
import matplotlib.dates
import scipy as sp


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
