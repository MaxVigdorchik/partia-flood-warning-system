"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
import numpy as np


def haversine(theta):
    """Computes the haversine function on input theta and returns the result"""
    return np.sin(theta / 2) * np.sin(theta / 2)


def spherical_distance(lat1, lat2, lon1, lon2):
    """Returns the distance between two points (latitude,longitude) on the surface of a sphere in km"""
    r = 6356.752
    h = haversine(lat2 - lat1) + np.cos(lat1) * \
        np.cos(lat2) * haversine(lon2 - lon1)
    return 2 * r * np.arcsin(np.sqrt(h))
