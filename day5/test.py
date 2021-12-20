import yfinance as yf
import pandas as pd
import numpy as np

class QuantGaloreData:
    def __init__(self):
        self.ticker = yf.Tickers('BTC-USD')
        self.data = yf.download(tickers=('BTC-USD'),period='1y',interval='1d',group_by='ticker',auto_adjust=True,prepost=False)
        self.df = pd.DataFrame(self.data)
        print(self.df.tail(1))

    def find_z(self):
        mean = self.df['Close'].mean()
        z_from_mean = (self.df['Close'].tail(1) - mean) / np.std(self.df['Close'])
        print("BTC-USD",self.df['Close'].tail(1),z_from_mean)

QGD = QuantGaloreData()
QGD.find_z()