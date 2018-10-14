import requests
import json
import pandas as pd
import re

def get_liquor_details(business_name):
    business_name = business_name.upper()
    print(business_name)
    url = "https://data.ny.gov/resource/83cw-i36h.json?doing_business_as_dba=%s" % (business_name)
    result = requests.get(url)
    result_dict = json.loads(result.text)
    df = pd.DataFrame(result_dict)
    if df.empty:
        liquor = {'liquor_license': "No license"}
        liquor_data = pd.DataFrame(liquor, index =[0])
    else:
        liquor_data = df[
            ['doing_business_as_dba', 'license_effective_date', 'license_expiration_date', 'license_type_name']]
    print(liquor_data)
    return liquor_data
