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

# Calculating Garman-Klass Volatility and add to a new column
df['garman-klass-volatility'] = (((np.log(df['high']) - np.log(df['low']))**2)/2) - (2*(np.log(2))-1) * ((np.log(df['adj close']) - np.log(df['open']))**2)

# Calculating RSI (Relative Stock Index), using pandas_ta library
df['rsi'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=20))













