# This Python Script helps to find companies in the NASDAQ Exchange with the highest dividend yields

- [What is a Stock Exchange?](https://www.investopedia.com/articles/basics/04/092404.asp)
- [What is Dividend?](https://www.investopedia.com/terms/d/dividend.asp)
- [What is Dividend Yield?](https://www.investopedia.com/terms/d/dividendyield.asp)

**Dividend yield** is the ratio of a company annual dividend compared to its stock price. **High dividend stocks** are a great investment strategy for all investors who are looking to get an almost safe inflow of cash every year.

We are going to build a Python script to go through all the stocks in the Nasdaq exchange and compute the dividend yield for each of them. To find high dividends stocks, we are going to apply below **dividend yield formula**. Then, we will sort by the returned yield in order to find the best dividends stocks.

**Dividend Yield = Annual Dividend / Share Price**

A **financial API** called [fmpcloud](https://fmpcloud.io/) offers a few free calls per day upon registration. After Registration, login in to your fmp account and get your API Key from the Documentation Section. Since we are dealing with NASDAQ, copy the link of NASDAQ available from
the Available Market and tickers sub-section.

1) Extract a list of [tickers](https://www.investopedia.com/ask/answers/12/what-is-a-stock-ticker.asp) for all stocks for which we are going to calculate the dividend yield. In our case, we are going to get all stocks of companies trading in Nasdaq and add them to a list called symbols:


2) After collecting the list of stocks trading in NASDAQ, loop through each of them and make a http request to the API end point to retrieve [company financial information](https://fmpcloud.io/api/v3/profile/AAPL?apikey=demo).

Parse the response to extract the details such as last annual dividend, price, market capitalisation, company name and exchange name. Then calculate the Dividend Yield and add all these variables to a Python Dictionary called **DivYield**

3) Finally having all data extracted from the API. Now present the results in a nice Pandas DataFrame and sort the Dividend Yield values in ascending order to have high dividend stocks at the top.

Dividend yield is a backward looking measure ie It looks at the last year annual dividend. This does not actually mean that the company will keep the same dividend amount during next years specially if they are having financial troubles.

We have analysed all stocks in Nasdaq. Feel free to repeat the task with other exchanges such as the New York Stock Exchange (NYSE).
