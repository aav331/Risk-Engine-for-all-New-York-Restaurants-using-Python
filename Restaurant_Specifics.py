import pandas as pd
from yelpapi import YelpAPI
from nltk.corpus import stopwords
from textblob import TextBlob

def get_restaurant_specifics(Business_name):
    yelp_api = YelpAPI(api_key='KnfmV9riCNt_4Pl1iNFGwBZIQhr6Vh7baEqDzIae5LSLXEQX_JeKBQLK6vuSxbzAO43M5x9zyO8sc9HmNdN34kUEYEklUxlKshrALdyT7HVhEDBvYqjlmeKPZrdxW3Yx')
    search_results = yelp_api.search_query(term=Business_name, location='New York, NY')

    rating = []
    if search_results['businesses'][0]['name'] == Business_name:
            business_id = search_results['businesses'][0]['id']
            business_results = yelp_api.reviews_query(id=business_id)
            business_search = yelp_api.business_query(id=business_id)
            for review in business_results['reviews']:
                rating.append(str(review['text']))
    #print(business_search)
    df = pd.DataFrame({'Name':Business_name, 'Review':rating})

    df['Review'] = df['Review'].str.replace('[^\w\s]','')
    stop = stopwords.words('english')
    df['Review'] = df['Review'].str.lower()
    df['Review'] = df['Review'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    df['sentiment'] = df['Review'].apply(lambda x: TextBlob(x).sentiment[0])

    sent = 0
    count = 0
    for row in df.itertuples():
        sent = float(sent + float(row[3]))
        count = count + 1

    sentiment = float(sent/count)

    specifics = {'Name':Business_name,'Price': business_search['price'],
                           'Rating': business_search['rating'], 'Cuisine1': business_search['categories'][0]['title'],
                           'Cuisine2': business_search['categories'][1]['title'],
                           'Open_after_12am': business_search['hours'][0]['open'][0]['is_overnight'],
                           'Type_of_Services': [business_search['transactions']],
                           'Sentiment':sentiment}

    restaurant_specifics = pd.DataFrame(specifics, index=[0])
    return restaurant_specifics
