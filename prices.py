from data import url, headers, core, accelerator
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# Grabs real time prices for coins within portfolio from CoinMarketCap aPI
# portfolio - dictionary with symbols and allocation percentages
def getPrices(portfolio):

    symbolString = ",".join(list(core.keys())) + "," + ",".join(list(accelerator.keys()))
    #print(symbolString)

    #keys = list((core | accelerator).keys())
    keys = list(portfolio.keys())
    #print(f"all keys: {keys}")


    parameters = {
        'symbol' : symbolString,
        'convert' : 'USD'
    }

    session = Session()
    session.headers.update(headers)

    prices = {}

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']

        for i in range(len(keys)):
            '''symbol = keys[i]
            print(symbol)
            print(type(symbol))'''
            
            coinPrice = data[keys[i]][0]['quote']['USD']['price']
            #print(f"{keys[i]} Price: {coinPrice}")
            prices[keys[i]] = coinPrice

        #for key in keys:
            #data = data[stikey][0]['quote']['USD']['price']
            #print(f"{key}: {data}")

        #pprint.pprint(data)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return prices