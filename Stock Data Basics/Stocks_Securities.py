#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sanithps98
"""
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt

style.use('ggplot')

START_DATE = dt.datetime(2020,1,1)
END_DATE = dt.datetime.now()

company_name = 'AMZN' # This is the ticker for Amazon

'''
data.DataReader uses the pandas_datareader package, looks for the stock ticker AMZN(Amazon) 
and gets the information from yahoo for the mentioned starting and ending date
 
'''

stock_data = data.DataReader(company_name,'yahoo',START_DATE,END_DATE) # stock_data contains stock pricing information for Amazon
print(stock_data)

Open = stock_data['Open']
Close = stock_data['Close']
High = stock_data['High']
Low = stock_data['Low']
Volume = stock_data['Volume']
Adj_Close = stock_data['Adj Close']

plt.figure(figsize=(8,8))
plt.plot(Open,label = 'Opening Price')
plt.plot(Close,label = 'Closing Price')
plt.xlabel('Date')
plt.ylabel('Opening and Closing Price')
plt.legend()
    
plt.show()

plt.figure(figsize=(8,8))
plt.plot(High,label = "Today's High")
plt.plot(Low,label = "Today's Low")
plt.xlabel('Date')
plt.ylabel('High and Low Price')
plt.legend()

plt.show()

fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212,sharex=ax1)
ax1.plot(Adj_Close)
ax1.set_ylabel("Adjusted Closing Price")
ax2.bar(stock_data.index,Volume)
ax2.set_ylabel("Volume")
plt.show()
