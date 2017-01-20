"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from .stationdata import build_station_list
import numpy as np


def haversine(theta):
    """Computes the haversine function on input theta and returns the result"""
    return np.sin(theta / 2) * np.sin(theta / 2)


def spherical_distance(p1, p2):  # gotta convert to radians
    """Returns the distance between two points (latitude,longitude) on the surface of a sphere in km"""
    r = 6356.752
    h = haversine((p2[0] - p1[0]) * np.pi / 180) + np.cos(p1[0] * np.pi / 180) * \
        np.cos(p2[0] * np.pi / 180) * haversine((p2[1] - p1[1]) * np.pi / 180)
    return 2 * r * np.arcsin(np.sqrt(h))


def stations_by_distance(stations, p):
    """Takes a list of stations and a point and returns a list of tuples
    (station, distance) where distance is there spherical distance of that station
    to p
    """
    result = []
    for station in stations:
        distance = spherical_distance(station.coord, p)
        result.append((station, distance))

    return sorted_by_key(result, 1)


def stations_within_radius(stations, centre, r):
    """ Takes a list of stations, a location, and a radius and returns
    in no specific order a list of all of the stations within r
    of centre. Latitudes and Longitudes are assumed to be valid as a precondition.
    """
    distances = stations_by_distance(stations, centre)
    return [station_list for station_list, distance in distances if distance < r]
