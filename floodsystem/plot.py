"""This module contains functions which create plots of river level data"""

import matplotlib.pyplot as plt
import dateutil.parser
import datetime
import numpy as np
from .stationdata import build_station_list
from .analysis import polyfit
import floodsystem.geo
import matplotlib
import scipy as sp


def plot_water_levels(station, dates, levels):
    """Takes an input of dates and water levels and plots both on a graph.
    Also shows the typical high and low for the station on the same graph.
    Does not show the graph."""

    # Plot
    plt.plot(dates, levels, label="$water levels$")

    # add lines of typical high and low
    plt.plot([dates[-1], dates[0]], [station.typical_range[0],
                                     station.typical_range[0]], color='g', label="$typical low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1],
                                     station.typical_range[1]], color='r', label="$typical high$")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: " + station.name)

    # Display stuff
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend(loc=2)  # move labels to upper left


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the historical water levels of station given by dates and levels.
    It then plots those levels along with a polynomial best fit of degree
    p which can then be used to estimate future water levels"""
    plot_water_levels(station, dates, levels)
    best_fit, offset = polyfit(dates, levels, p)

    x = matplotlib.dates.date2num(dates)
    y = best_fit(x - offset)
    plt.plot(dates, y, label="$Best Fit$")
    plt.legend(loc=2)
