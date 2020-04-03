# This Python Script helps to find companies in the NASDAQ Exchange with the highest dividend yields

- [What is a Stock Exchange?](https://www.investopedia.com/articles/basics/04/092404.asp)
- [What is Dividend?](https://www.investopedia.com/terms/d/dividend.asp)
- [What is Dividend Yield?](https://www.investopedia.com/terms/d/dividendyield.asp)

**Dividend yield** is the ratio of a company annual dividend compared to its stock price. **High dividend stocks** are a great investment strategy for all investors who are looking to get an almost safe inflow of cash every year.

We are going to build a Python script to go through all the stocks in the Nasdaq exchange and compute the dividend yield for each of them. To find high dividends stocks, we are going to apply below **dividend yield formula**. Then, we will sort by the returned yield in order to find the best dividends stocks.

**Dividend Yield = Annual Dividend / Share Price**

1) Extract a list of [tickers](https://www.investopedia.com/ask/answers/12/what-is-a-stock-ticker.asp) for all stocks for which we are going to calculate the dividend yield. In our case, we are going to get all stocks of companies trading in Nasdaq and add them to a list call symbols:
