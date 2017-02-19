"""This module contains functions which create plots of river level data"""

import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """Takes an input of dates and water levels and plots both on a graph.
    Also shows the typical high and low for the station on the same graph.
    Does not show the graph."""

    print(levels)
    
    # Plot
    plt.plot(dates, levels, label="$water levels$")
    
    #add lines of typical high and low
    plt.plot([dates[-1], dates[0]], [station.typical_range[0], station.typical_range[0]], color='g', label="$typical low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1], station.typical_range[1]], color='r', label="$typical high$")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station: "+station.name)

    # Display stuff
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend(loc=2) #move labels to upper left
