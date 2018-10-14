import pandas as pd
import pymysql
from yelpapi import YelpAPI

def get_restaurant_details(Business_name):
    db = pymysql.connect(host="localhost", user="root", password="linchpin@1", db="Linchpin_Coach")
    yelp_api = YelpAPI(api_key='KnfmV9riCNt_4Pl1iNFGwBZIQhr6Vh7baEqDzIae5LSLXEQX_JeKBQLK6vuSxbzAO43M5x9zyO8sc9HmNdN34kUEYEklUxlKshrALdyT7HVhEDBvYqjlmeKPZrdxW3Yx')
    Restaurant_Data = pd.read_csv("Restaurant_Data.csv")

    cur1 = db.cursor()
    cur2 = db.cursor()

    try:
        cur1.execute("""Select A.Address, A.City, A.State, A.Zip_code From Address_Data A 
                     Where A.Company_Name like "%{}%" """ .format(Business_name))
        Details = cur1.fetchall()

    except ValueError:
        Details = []
        search_results = yelp_api.search_query(term=Business_name, location='New York, NY')
        if search_results['businesses'][0]['name'] == Business_name:
            business_id = search_results['businesses'][0]['id']
            latitude = search_results['businesses']['coordinates'][0]['latitude']
            Details.append(search_results['businesses']['coordinates'][0]['longitude'])
            business_search = yelp_api.business_query(id=business_id)
            Details.append(business_search['location']['address1'])
            Details.append(business_search['location']['city'])
            Details.append(business_search['location']['state'])
            Details.append(business_search['location']['zip_code'])
            print(Details)


    for row in Details:
        Address = row[0]
        City = row[1]
        State = row[2]
        Zip_Code = row[3]


    try:
        cur2.execute("""Select A.Actual_Revenue, A.Number_of_Employees From Restaurant_Financial_Information A 
                         Where A.Restaurant_Name like "%{}%" AND A.Address like "%{}%" """ .format(Business_name, Address))
        Info = cur2.fetchall()
    except ValueError:
        Info = ["Unavailable", "Unavailable"]

    for rows in Info:
        Revenue = rows[0]
        Employees = rows[1]

    df = Restaurant_Data[Restaurant_Data['Company Name']==Business_name][
        ['Executive First Name', 'Executive Last Name', 'Years In Database', 'Square Footage', 'Credit Score Alpha']]
    Owner = str(df['Executive First Name'].item() + " " + df['Executive Last Name'].item())
    no_of_years = df['Years In Database'].item()
    sq_ft = df['Square Footage'].item()
    credit_score = df['Credit Score Alpha'].item()

    if df.index != 0:
        Detail = {'Restaurant Name': Business_name, 'Address': Address, 'City': City, 'State': State, 'Zip Code': Zip_Code,
                  'Owner Name': Owner, 'Years in Business': no_of_years, 'Square Footage': sq_ft,
                  'Credit Score': credit_score,'Revenue': Revenue, 'Number of Employees': Employees}
    else:
        Detail = {'Restaurant Name': Business_name, 'Address': Address, 'City': City, 'State': State, 'Zip Code': Zip_Code,
                  'Owner Name': "None", 'Years in Business': "None", 'Square Footage': "None", 'Credit Score': "None",
                  'Revenue': Revenue, 'Number of Employees': Employees}

    restaurant_details = pd.DataFrame(Detail, index=[0])
    return(restaurant_details)
