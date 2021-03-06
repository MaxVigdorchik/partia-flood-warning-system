"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
import math


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:    {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   latest level:  {}".format(self.latest_level)

        return d

    def typical_range_consistent(self):
        """returns true if and only if the data in the station class meets certain consistency
        requirements including that typical highs are higher than lows and that data is available
        also checks if latest level is consistent to save a lot of other code
        """
        if self.typical_range is None:
            return False

        # the following if statement is probably not necessary as math.isnan
        # covers it, but it does no harm.

        if self.typical_range[0] is None or self.typical_range[1] is None:
            return False

        if math.isnan(self.typical_range[0]) or math.isnan(self.typical_range[1]):
            return False

        low, high = self.typical_range
        # using this phrasing to make it more clear how consistency is being
        # checked
        return not (high < low)

    def relative_water_level(self):
        """Returns the latest water level as a fraction of the typical range, and returns None if data 
        not available"""

        # use another method to only define a relative level if typical values
        # are consistent
        if self.typical_range_consistent():

            # the following raises an exception if latestlevel is None
            # AND IF ANYTHING ELSE GOES WRONG SUCH AS THE FUNCTION NOT WORKING.
            # try:
            try:
                relative_level = (self.latest_level - self.typical_range[0]) / (
                    self.typical_range[1] - self.typical_range[0])
            except:
                relative_level = None
        else:
            relative_level = None
        return relative_level

    def latest_level_consistent(self):
        """Function to deal with weird cases such as latest level being a list, 
        also just checks that update water levels went correctly for the latest level"""
        if self.latest_level is None:
            return False

        if not isinstance(self.latest_level, float):
            return False  # For the random stations that have a list as latest
            level

        return True


def inconsistent_typical_range_stations(stations):
    """Returns a list of all stations with inconsistent typical ranges"""
    return [s for s in stations if not s.typical_range_consistent()]
