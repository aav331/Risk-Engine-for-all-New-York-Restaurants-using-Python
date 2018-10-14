import pandas as pd
import numpy as np
import geopy.distance

def get_dist_to_hospital(rest):
    hospitals = pd.read_csv("Map_of_NYC_Health_and_Hospitals_withLongLat.csv")
    acute = hospitals.loc[hospitals['Facility Type'] == 'Acute Care Hospital']
    res = [np.float(rest['Latitude']), np.float(rest['Longitude'])]
    dist = []
    for r in acute.index.values:
        f = acute.loc[r, 'LATITUDE':'LONGITUDE']
        d = geopy.distance.distance(f, res).km * 1000
        dist.append(d)
    hospital_distance_from_restaurant = min(dist)
    print(round(hospital_distance_from_restaurant, 2))
    return (round(hospital_distance_from_restaurant, 2))