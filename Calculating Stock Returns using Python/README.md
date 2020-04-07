# How to calculate stock returns in Python

One of the most important tasks in financial markets is to analyze historical returns on various
investments.

For the Stock Basics you can refer : [https://github.com/sanithps98/Python-for-Finance/tree/master/Stock%20Data%20Basics](https://github.com/sanithps98/Python-for-Finance/tree/master/Stock%20Data%20Basics)

A stock's [**adjusted closing price**](https://www.investopedia.com/ask/answer/06/adjustedclosingprice.asp) gives you all the information you need to keep an eye on your stock.You can use unadjusted closing prices to calculate returns, but adjusted closing prices save you some time and effort.

The adjusted closing price of a stock takes into account dividend payments, splits and other factor which directly influence overall return. Comparing the adjusted closing prices for a single stock over a specific duration of time will allow you to identify its return.

In today's fast-paced financial environment, adjusted closing prices are an excellent tool for capturing an informative snapshot of the day's activity which can help you refine your strategies over the short term.


We are going to calculate the stock returns using Python and it is explained in detail in the Jupyter Notebook

### **Things to know **

- [**pct_change()**](https://www.w3resource.com/pandas/series/series-pct_change.php) : It is used to get percentage change between the current and a prior element.
It computes the percentage change from the immediately previous row by default. This is useful in comparing the percentage of change in a time series of elements.

- **Mean** :

- **Rolling means (or moving averages)** : They are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.

To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. 
For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point.


- [**tandrd Deviation**]: A cumulative return on an investment is the aggregate amount that the investment has gained or lost over time, independent of the period of time involved.

- **Standard Deviation** :

- **Correlation** :

- **Covariance** :
