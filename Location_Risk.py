import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import geopy.distance
from Crime_Risk import get_crime_risk
from Dist_Fire import get_fire_station_distance
from Dist_Hospital import get_dist_to_hospital
from Dist_Hydrant import get_dist_to_hydrants


def get_location_risk(address,county):
    restaurant_data = pd.read_csv("Restaurant_Data.csv")
    rest = restaurant_data.loc[restaurant_data['Address'] == address]
    location_risk ={}
    print(rest)
    crime_risk = get_crime_risk(county)
    dist_to_fire_station = get_fire_station_distance(rest)
    dist_to_hospital = get_dist_to_hospital(rest)
    dist_to_hydrants = get_dist_to_hydrants(rest)
    location = {'Crime Risk': crime_risk, 'Distance to the nearest hospital': dist_to_hospital,
                     'Distance to the nearest Fire Station': dist_to_fire_station,
                     'Distance of the nearest Hydrant': dist_to_hydrants}
    location_risk = pd.DataFrame(location, index=[0])
    return location_risk
