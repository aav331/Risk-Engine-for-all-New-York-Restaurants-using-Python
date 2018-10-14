import re
import pandas as pd

def get_property_details(addr):
    MN = pd.read_csv('MN_18v1.csv')
    addr = addr.replace('W ', 'West ')
    addr = addr.replace('E ', 'East ')
    addr = addr.replace('St', 'Street ')
    addr = re.sub('Ave($|\s)', 'Avenue ', addr)
    addr = addr.replace('Pl ', 'Place ')
    addr = addr.replace('Rd ', 'Road ')
    addr = re.sub('(\s?)# .*', '', addr)
    #addr = addr.replace('1st', '1')
    #addr = addr.replace('2nd', '2')
    #addr = addr.replace('3rd', '3')
    #addr = addr.replace('4th', '4')
    #addr = addr.replace('5th', '5')
    #addr = addr.replace('6th', '6')
    #addr = addr.replace('7th', '7')
    #addr = addr.replace('8th', '8')
    #addr = addr.replace('9th', '9')
    #addr = addr.replace('0th', '0')
    addr = addr.upper()

    print(addr)

    property_df = MN[MN['OwnerName'].str.contains(addr, na=False)][
        ['Address', 'ZipCode', 'ZoneDist1', 'BldgClass', 'LandUse', 'OwnerType', 'OwnerName', 'BldgArea', 'ComArea',
         'ResArea', 'NumFloors', 'LotFront', 'LotType', 'BsmtCode', 'AssessTot', 'YearBuilt', 'YearAlter1',
         'YearAlter2']]
    property_df = property_df.reset_index()
    return property_df