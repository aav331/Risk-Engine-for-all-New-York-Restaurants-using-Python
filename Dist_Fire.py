import json
import requests
import pandas as pd
import numpy as np
import geopy.distance

def get_fire_station_distance(rest):
    fire_station = pd.read_csv('FDNY_Firehouse_Listing.csv')
    fire_station = fire_station.dropna(subset=['Latitude', 'Longitude'])
    res = [np.float(rest['Latitude']), np.float(rest['Longitude'])]
    dist = []
    for r in fire_station.index.values:
        f = fire_station.loc[r, 'Latitude':'Longitude']
        d = geopy.distance.distance(f, res).km * 1000
        dist.append(d)
    minimum_distance_to_fire_station = min(dist)
#    print("Distance to fire station is:", minimum_distance_to_fire_station)
    return (round(minimum_distance_to_fire_station,2))
