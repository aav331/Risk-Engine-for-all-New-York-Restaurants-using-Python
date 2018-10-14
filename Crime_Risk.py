import numpy as np
import pandas as pd

def get_crime_risk(county):
    crime = pd.read_csv('Index__Violent__Property__and_Firearm_Rates_By_County__Beginning_1990.csv')
    crimerate = crime[crime.Year == 2017][['County', 'Violent Rate', 'Property Rate']]
    crimerate['linchpin Rate'] = 1/3*crimerate['Violent Rate'] + 2/3*crimerate['Property Rate']
    crimerate = crimerate.sort_values(by = ['linchpin Rate'])
    crimerate = crimerate.reset_index(drop=True)
    low = np.nanmin(crimerate[['linchpin Rate']])
    high = np.nanmax(crimerate[['linchpin Rate']])
    diff = high - low
    gap = diff/10
    level=[]

    for i in range(10):
        count=crimerate[(crimerate['linchpin Rate'] >= (low+gap*i)) & (crimerate['linchpin Rate'] <= (low + gap*(i+1)))]['County'].count()
        level.extend(np.repeat(i+1, count))
    crimerate['CrimeLevel'] = level
    crime_risk = crimerate[crimerate['County']== county]
    crime_score = crime_risk['CrimeLevel'].item()
#    print("Crime risk is", crime_score)
    return crime_score
