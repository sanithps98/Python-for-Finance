import pandas as pd
import requests
import json

my_apikey = 'TYPE YOUR API KEY'
tickers = requests.get(f'https://fmpcloud.io/api/v3/symbol/available-nasdaq?apikey={my_apikey}')
tickers = tickers.json()

#tickers = open('tickers.json')
#tickers = json.load(tickers)

symbols = []
for ticker in tickers:
    symbols.append(ticker['symbol'])
  
DivYield = {}

for company in symbols_short:
  try:
    companydata = requests.get(f'https://fmpcloud.io/api/v3/profile/{company}?apikey={my_apikey}')
    companydata = companydata.json()
    latest_Annual_Dividend = companydata[0]['lastDiv']
    price = companydata[0]['price']
    market_Capitalization = companydata[0]['mktCap']
    name = companydata[0]['companyName']
    exchange = companydata[0]['exchange']

    dividend_Yield= latest_Annual_Dividend/price
    DivYield[company] = {}
    DivYield[company]['Dividend_Yield'] = dividend_Yield
    DivYield[company]['latest_Price'] = price
    DivYield[company]['latest_Dividend'] = latest_Annual_Dividend
    DivYield[company]['market_Capit_in_M'] = market_Capitalization/1000000
    DivYield[company]['company_Name'] = name
    DivYield[company]['exchange'] = exchange
  except:
    pass

print(DivYield)

DivYield_dataframe = pd.DataFrame.from_dict(DivYield, orient='index')
DivYield_dataframe = DivYield_dataframe.sort_values(['Dividend_Yield'], ascending=[False])

print(DivYield_dataframe)
