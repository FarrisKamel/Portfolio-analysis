# This code was influenced by the following youtube video. https://www.youtube.com/watch?v=9Y3yaoi9rUQ 
# This video helpped me prepare the data for portfolio analysis 

from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import pandas as pd 
import numpy as np
import datetime as dt 
import yfinance as yf
import pandas_ta
import warnings
warnings.filterwarnings('ignore')


##### Setting up the data
#Get all the snp500 stock list from wiki
snp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
# Get all the symbols and replace the . with a - to use with yfinance
snp500['Symbol'] = snp500['Symbol'].str.replace('.','-')
symbols_list = snp500['Symbol'].unique().tolist()

# Get from up to this data from 8 year
end_date = '2024-10-27'
start_date = pd.to_datetime(end_date)-pd.DateOffset(365*8)

#Download the data from yfinance 
df = yf.download(tickers = symbols_list, start=start_date, end=end_date)
# change dataframe structure to make it multy index 
df = df.stack() 
df.index.names = ['date', 'ticker']
df.columns = df.columns.str.lower()
#print(df)

##### Now we will calculate features and technical indicators for each stock

# Function used to calculate macd
def computeMacD(close_price):
    # Check if we have a value to work with, if not return none
    if close_price.empty or close_price.isnull().any():
        return None
    # We will use to pandas_ta function in order to compute the macd
    macd = pandas_ta.macd(close=close_price, length=20).iloc[:,0]
    # Normalize the final result before adding it back
    return macd.sub(macd.mean()).div(macd.std())

# Calculating Garman-Klass Volatility and add to a new column
df['garman-klass-volatility'] = (((np.log(df['high']) - np.log(df['low']))**2)/2) - (2*(np.log(2))-1) * ((np.log(df['adj close']) - np.log(df['open']))**2)

# Calculating RSI (Relative Stock Index), using pandas_ta library
df['rsi'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=20))

# Calculting the MACD
df['macd'] = df.groupby(level=1, group_keys=False)['adj close'].apply(computeMacD)
#print(df)

# Calculting the Dollar volume for each stock / 1e6 
df['dollar_volume'] = (df['adj close']*df['volume'])/1000000
#print(df)

##### Now we will filter out the top 10 stocks for each month

# The the indictors only. We can do this be making a new list of only the indictors
indicators = [c for c in df.columns.unique(0) if c not in ['dollar_volume', 'volume', 'open', 'high', 'low', 'close']]
#print(indicators) # Error checking 

# Get the last val after getting the mean of the stock indicators
data = pd.concat([df.unstack('ticker')['dollar_volume'].resample('M').mean().stack('ticker').to_frame('dollar_volume'),df.unstack()[indicators].resample('M').last().stack('ticker')], axis=1).dropna()

# Find the average of the dollar amount. First unstack to get the day values
data['dollar_volume'] = df.unstack('ticker')['dollar_volume'].resample('M').mean().stack().to_frame('dollar_volume').dropna()

# Find 5 year rolling average for dollar-volume for eacn stock
data['dollar_volume'] = (data['dollar_volume'].unstack('ticker').rolling(5*12).mean().stack())

# add a rank column that ranks the stocks and return the top 10
data['dollar_volume_rank'] = (data.groupby('date')['dollar_volume'].rank(ascending=False))

# Here we have the top 10 stock ranked by dollar volume with all the stock indicatior.
data = data[data['dollar_volume_rank']<11].drop(['dollar_volume', 'dollar_volume_rank'], axis=1)

# Export data to csv file to use for portfolio analysis
data.to_csv("output_data.csv")

















