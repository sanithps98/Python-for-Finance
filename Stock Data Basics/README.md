# BASICS OF STOCK DATA

Quantitative Analysts who believe in Trading need access to Stock Price and Volume so that they can compute a combination of Technical Indicators (Eg: SMA, BBP, MACD etc) for strategy. This data is available on many platforms such as IEX, Quandl via REST APIS.

Pandas is one of the most popular tools for trading strategy development because Pandas has a wide variety of utilities for data collection, manipulation and analysis, etc. It contains subpackage called pandas_datareader whichprovides a consistent simple API to collect data from these platforms and create a dataframe.

Using the pandas datareader to get data about stocks and securities. Using the Yahoo Finance API because the Google Finance API has been deprecated. This video covers getting data about a stock, getting basic statistics such as the short rolling mean and the 200-day rolling mean and then creating a graph with the data with matplotlib's pyplot.


- Open - When the stock market opens in the morning for trading, what was the price of one share?
- High - over the course of the trading day, what was the highest value for that day?
- Low - over the course of the trading day, what was the lowest value for that day?
- Close - When the trading day was over, what was the final price?
- Volume - For that day, how many shares were traded?
- Adj Close - This one is slightly more complicated, but, over time, companies may decide to do something called a stock split. For example, Apple did one once their stock price exceeded $1000. Since in most cases, people cannot buy fractions of shares, a stock price of $1,000 is fairly limiting to investors. Companies can do a stock split where they say every share is now 2 shares, and the price is half. Anyone who had 1 share of Apple for $1,000, after a split where Apple doubled the shares, they would have 2 shares of Apple (AAPL), each worth $500. Adj Close is helpful, since it accounts for future stock splits, and gives the relative price to splits. For this reason, the adjusted prices are the prices you're most likely to be dealing with.
