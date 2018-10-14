import pandas as pd
from Restaurant_Details import get_restaurant_details
from Restaurant_Specifics import get_restaurant_specifics
from Location_Risk import get_location_risk
from Liquor_License import get_liquor_details
from Natural_Hazard import get_natural_hazard_risks
from Property_Details import get_property_details

business_name = input("What is the name of your Restaurant?")
restaurant_details = get_restaurant_details(business_name)
restaurant_specifics = get_restaurant_specifics(business_name)
address = str(restaurant_details['Address'].item())
county = str(restaurant_details['City'].item())
state = str(restaurant_details['State'].item())
print(address)
location_risk = get_location_risk(address,county)
print(restaurant_details)
print(restaurant_specifics)
print(location_risk)
liquor_license = get_liquor_details(business_name)
print(liquor_license)
natural_hazard_risks = get_natural_hazard_risks(state, county)
print(natural_hazard_risks)
property_risks = get_property_details(address)
print(property_risks)

Restaurant_Details = pd.concat([restaurant_details,restaurant_specifics, location_risk, liquor_license, natural_hazard_risks, property_risks], axis=1)
Restaurant_Details.to_csv("Restaurant_Details_%s.csv" %business_name, index=False)