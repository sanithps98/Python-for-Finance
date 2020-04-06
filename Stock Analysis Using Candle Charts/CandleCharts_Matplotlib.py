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

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

START_DATE = dt.datetime(2010,1,1)
END_DATE = dt.datetime.now()

company_name = 'AMZN' # This is the ticker for Amazon

'''
data.DataReader uses the pandas_datareader package, looks for the stock ticker AMZN(Amazon) 
and gets the information from yahoo for the mentioned starting and ending date
 
'''
stock_data = data.DataReader(company_name,'yahoo',START_DATE,END_DATE) # stock_data contains stock pricing information for Amazon

stock_data = stock_data[['Open', 'High', 'Low', 'Close']]

stock_data.reset_index(inplace=True)
stock_data['Date'] = stock_data['Date'].map(mdates.date2num)
print(stock_data)


ax = plt.subplot()
candlestick_ohlc(ax, stock_data.values, width=5, colorup='g', colordown='r')
ax.set_axisbelow(True)
ax.set_title('Amazon Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_xlabel('Price')
ax.set_ylabel('Date')
ax.xaxis_date()
ax.grid(True)
plt.show()


