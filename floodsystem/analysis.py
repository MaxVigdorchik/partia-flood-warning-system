import dateutil.parser
import datetime
import floodsystem.flood
import floodsystem.geo
import numpy as np
from .stationdata import build_station_list, update_water_levels
from .datafetcher import fetch_measure_levels
from .utils import sorted_by_key
from .station import inconsistent_typical_range_stations
from .flood import stations_level_over_threshold
import matplotlib
import matplotlib.dates
import scipy as sp
import scipy.misc


def issue_warnings(stations, p=1, dt=10):
    """Returns a list of all stations alongside an assesment of their flood warning risk
    based on their current and historical water levels. Uses a polynomial of degree p for estimation
    with a history of dt days. The return value is given as (station, risk_value, risk) where risk
    is a string with "low","moderate", etc. and risk_value is a semi-arbitrary number assigned to
    represent risk, based on the current level, it's derivative, and second derivative"""

    # TODO: Future addition could use some form of machine learning to
    # generate risk_value

    # I messed up writing this code confusing pass with continue, so a lot of
    # it is totally unecessary but I am not sure what parts.

    # Define (low, moderate, high, severe) risk values
    def risk_definition(risk):
        """Helper Function to define what different risks mean"""
        boundaries = (0, 0.8, 1.5, 2)
        if risk is None:
            return "unknown"
        if risk < boundaries[1]:
            return "low"
        if risk < boundaries[2]:
            return "moderate"
        if risk < boundaries[3]:
            return "high"
        return "severe"

    # Defines how much derivatives of the level matter
    dweight, d2weight = (0.5, 0.25)

    stations_by_risk = []
    # store maximum risk of each river for benefit of inconsistent stations
    risk_of_rivers = {}
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    unsafe_stations = stations_level_over_threshold(
        stations, 0.8)  # Tol is for moderate risk stations or higher

    for s in stations:
        if s.relative_water_level() is None:  # Avoid Pesky nonetypes always appearing
            continue
        if s in inconsistent_stations:
            continue
        if (s not in unsafe_stations):
            stations_by_risk.append(
                (s, s.relative_water_level(), risk_definition(s.relative_water_level())))
            continue  # save time computing fairly safe stations

        dates, levels = fetch_measure_levels(
            s.measure_id, dt=datetime.timedelta(days=dt))
        times = matplotlib.dates.date2num(dates)
        # So simple operations can be done on the list
        try:
            levels = np.array(levels)
            levels = (levels - s.typical_range[0]) / (
                s.typical_range[1] - s.typical_range[0])
        except (TypeError, ValueError):  # For the random list in relative levels that appears
            inconsistent_stations.append(s)
            continue

        # Converts the levels to relative levels before polynomial fitting
        # since the values are more useful as relative levels.

        # f is a function representing water levels over time, and its
        # derivatives are computed. The rest are other useful values
        try:
            f, offset = polyfit(dates, levels, p)
            latest_time = times[-1] - offset
        # in case of weird empty arrays, shouldnt be happening
        except (IndexError, ValueError, TypeError):
            inconsistent_stations.append(s)  # make sure to consider it later
            continue
        df = f.deriv()
        d2f = f.deriv(2)

        risk_value = f(latest_time)
        risk_value += df(latest_time) * dweight
        risk_value += d2f(latest_time) * d2weight
        stations_by_risk.append(
            (s, risk_value, risk_definition(risk_value)))

        if risk_value is None:  # Some weird stuff is happening with risk_value
            inconsistent_stations.append(s)
            continue

        if (not s.river in risk_of_rivers.keys()) or (risk_value > risk_of_rivers[s.river]):
            risk_of_rivers[s.river] = risk_value

        print(risk_value)

    for s in inconsistent_stations:
        if s.river in risk_of_rivers.keys():
            stations_by_risk.append(
                (s, risk_of_rivers[s.river], risk_definition(risk_of_rivers[s.river])))
        else:
            stations_by_risk.append((s, 0, risk_definition(0)))

    return sorted_by_key(stations_by_risk, 1, reverse=True)


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


# The following function is a remnant of an idea to do Bernstein polynomial regression.
# def Bernstein(i, n):
#    """Returns the ith basis Bernstein polynomial of degree n"""
#    c = sp.special.binom(n, i)
#
#    def f(x):
#        return c * (x**i) * ((1 - x)**(n - i))
#
#    return f
