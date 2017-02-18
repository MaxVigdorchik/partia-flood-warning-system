import dateutil.parser
import datetime
import numpy as np
from .stationdata import build_station_list
from .analsys import polyfit
import geo
import matplotlib
import scipy as sp
import matplotlib.pyplot as plt


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the historical water levels of station given by dates and levels.
    It then plots those levels along with a polynomial best fit of degree
    p which can then be used to estimate future water levels"""
    plot_water_levels(station, dates, levels)
    best_fit, offset = polyfit(dates, levels, p)

    x = matplotlib.dates.date2num(dates)
    y = best_fit(x - offset)
    plt.plot(dates, y)
    plt.title('Station Levels Best Fit')
