# Portfolio-analysis
This project is my attempt on applying what I learned from auditing an Intro to Financial Engineering. 
This project will analyze the SP500 stocks, calculate features and indictors for each stock, "contine" and produce an ideal portfolio.

## The Process 
#### Data Processing - 
The list of the SP500 stock was imported from the following webpage: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

The symbols were then extracted and put into a list. The list was used to import all the data for the stocks from yfinance.

A dataframe with all the data for each stock with made and munipulated for our use. 

#### Calculating Features and Stock Indictors - 
Using all the data, the following features and indictors were used: 
* Garman-Klass Volatility 
* RSI 
* ATR
* MACD
* Dollar Volume 

All of these were caluclated for use stock and added to the data frame

#### 

## Packages Needed
* pandas
* numpy 
* matplotlib
* statsmodels
* pandas_datareader
* datatime
* yfinance
* sklearn
* PyPorfolioOpt


## References
Garman-Klass Volatility - https://portfoliooptimizer.io/blog/range-based-volatility-estimators-overview-and-examples-of-usage/
RSI (Relative Stock Index) - https://www.investopedia.com/terms/r/rsi.asp









