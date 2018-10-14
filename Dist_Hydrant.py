import pandas as pd
import numpy as np
import geopy.distance

def get_dist_to_hydrants(rest):
    Hydrants = pd.read_csv("Hydrants.csv")
    res_lat = np.float(rest['Latitude'])
    res_lon = np.float(rest['Longitude'])
    hy1 = Hydrants.loc[(Hydrants['LATITUDE'] <= (res_lat + 0.000227))
                       & (Hydrants['LATITUDE'] >= (res_lat - 0.000227))
                       & (Hydrants['LONGITUDE'] <= (res_lon + 0.000227))
                       & (Hydrants['LONGITUDE'] >= (res_lon - 0.000227))]
    if hy1.empty:
        hy2 = Hydrants.loc[(Hydrants['LATITUDE'] <= (res_lat + 0.0004545))
                           & (Hydrants['LATITUDE'] >= (res_lat - 0.0004545))
                           & (Hydrants['LONGITUDE'] <= (res_lon + 0.0004545))
                           & (Hydrants['LONGITUDE'] >= (res_lon - 0.0004545))]
        if hy2.empty:
            dist = '>=50'
        else:
            dist = '25-50'
    else:
        dist = '<=25'
    min_dist_to_hydrant = dist + 'm'
#    print("Distance to fire Hydrant is:", min_dist_to_hydrant)
    return min_dist_to_hydrant

