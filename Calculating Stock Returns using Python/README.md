# How to calculate stock returns in Python

One of the most important tasks in financial markets is to analyze historical returns on various
 nvestments.


A stock's   sted closing price gives you all the information you need to keep an eye on your stock. You can use unadjusted closing prices to calculate returns, but adjusted closing prices save you some
time and effort.






https://www.investopedia.com/ask/answers/06/adjustedclosingprice.asp


The adjusted closing price of a stock takes into account dividend payments, splits and other factor which directly influence overall return. Comparing the adjusted closing prices for a single stock over a specific duration of time will allow you to identify its return.


In today's fast-paced financial environment, adjusted closing prices are an excellent tool for capturing an informative snapshot of the day's activity which can help you refine your strategies over the short term.



The pct_change() function is used to get percentage change between the current and a prior element.

Computes the percentage change from the immediately previous row by default. This is useful in comparing the percentage of change in a time series of elements.

https://www.w3resource.com/pandas/series/series-pct_change.php


Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.

To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point. The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data. 
