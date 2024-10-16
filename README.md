# Portfolio-analysis
This project is my attempt on applying what I learned from auditing an Intro to Financial Engineering. 
This project will analyze the SP500 stocks, calculate features and indictors for each stock, "contine" and produce an ideal portfolio.

## Data Processing - 
The list of the SP500 stock was imported from the following webpage: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

The symbols were then extracted and put into a list. The list was used to import all the data for the stocks from yfinance.

A dataframe with all the data for each stock with made and munipulated for our use. 

### Calculating Features and Stock Indictors - 
Using all the data, the following features and indictors were used: 
* Garman-Klass Volatility 
* RSI 
* MACD
* Dollar Volume 

All of these were caluclated for use stock and added to the data frame

### Evaluting to Get Top 10 Stock - 
With the new dataframe, that includes the features and stock indictors, we will evaluate the top 10 stocks for each month.
For Garman-Klass volatility, RSI and MACD, we will return the top values for the month. For the dollar volume, we will find the average dollar volume for the month.
The NaN values will also be dropped and a new variable is made with the new data. After that, we will find the 5 year rolling average for each stock and then using the dollar volume I will find the top 10 liquid stocks for each month.

### Exporting to CVS
The data is this exported to a .csv file to use for portfolio anaysis

## Porfolio Analysis

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

MACD (Moving average convergence/divergence) - https://www.investopedia.com/terms/m/macd.asp#:~:text=Key%20Takeaways-,Moving%20average%20convergence%2Fdivergence%20(MACD)%20is%20a%20technical%20indicator,from%20the%2012%2Dperiod%20EMA.

Dollar Volume - https://help.tc2000.com/m/69404/l/745295-dollar-volume#

Data processing - https://www.youtube.com/watch?v=9Y3yaoi9rUQ













