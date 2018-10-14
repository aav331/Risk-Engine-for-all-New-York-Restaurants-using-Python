import pandas as pd

def get_natural_hazard_risks(state,county):
    hazard_risk = pd.read_csv("Hazard_Risk.csv")
    eq_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].EQ_risk.item()
    fire_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].Fire_risk.item()
    hurricane_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].Hurricane_risk.item()
    storm_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].Storm_risk.item()
    tornado_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].Tornado_risk.item()
    flood_risk = hazard_risk[(hazard_risk['StateAB']==state) & (hazard_risk['County']==county)].Flood_risk.item()
    
    natural_risk_factors = {'Earthquake_Risk': eq_risk, 'Fire_Risk': fire_risk, 'Hurricane_Risk': hurricane_risk,
                            'Storm_Risk': storm_risk, 'Tornado_Risk': tornado_risk, 'Flood_Risk': flood_risk}

    natural_hazard_risk = pd.DataFrame(natural_risk_factors, index=[0])

    return natural_hazard_risk