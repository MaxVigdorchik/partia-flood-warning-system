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
    of centre
    """
    distances = stations_by_distance(stations, centre)
    return [station_list for station_list, distance in distances if distance < r]

def rivers_with_station(stations):
    """Takes a list of stations and returns a set of all the rivers
    in alphabetic order upon which those stations are located"""
    rivers=set()
    for station in stations:
        rivers.add(station.river)
    rivers=sorted(rivers)
    return rivers

def stations_by_river(stations, river):
    """Takes a list of stations and returns a list of all the station names
    on a specific river in alphabetic order"""
    station_names=[]
    for station in stations:
        if station.river==river:
            station_names.append(station.name)
    station_names=sorted(station_names)
    return station_names

def rivers_by_station_number(stations, N):
    """Take a list of stations and return the N rivers with the most stations upon
    them, in the form of a list of tuples in descending order"""

    #use another function in geo to build list of non-repeated rivers
    rivers=rivers_with_station(stations)

    #initialise list
    rivers_with_count=[]

    for river in rivers:
        count=0
        for station in stations:
            if station.river==river:
                count+=1
                
        #now that the number of times the river appears in the station list has been determined, the river can be appended
        rivers_with_count.append((river, count))

    #sort list according to number of rivers
    rivers_with_count=sorted(rivers_with_count, key=lambda x: x[1], reverse=True)

    #if the next river has the same number of stations, N must be increased to include this river
    while rivers_with_count[N-1][1]==rivers_with_count[N][1]:
        N+=1
        
    return rivers_with_count[:N]
                
        

































    
        
