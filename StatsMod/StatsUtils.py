import pandas as pd
import numpy as np
from StatsMod import Indicators
import definitions
import logging

class Stocks():
    @classmethod
    def GetAllTickersIndicators(self):
        data = pd.read_csv(definitions.NDXfile)
        tickers = data['ticker']
        for ticker in tickers[:]:
            try:
                df = self.Get_All_Indicators(ticker)
                print('.')

            except Exception as inst:
                msg = "cant find {} ".format(ticker) + "args:", inst.args[0]
                print(msg)
                logging.error(msg)
    @classmethod
    def Get_All_Indicators(self, ticker):
        filenameInput = definitions.IMPORTLocationFiles + '\{}.csv'.format(ticker)
        df = pd.read_csv(filenameInput)
        indi = Indicators.Indicators()
        close = df['CLOSE']
        df['return'] = indi.CompReturn(close)
        df['rsi'] = indi.CompRSI(close, 14)
        emaslow, emafast, macd = indi.CompMACD(close)
        df['macd'] = macd
        df['emaslow'] = emaslow
        df['emafast'] = emafast
        df = df.rename(columns={0: 'index'})
        df = df.drop(['Datetime'], 1)
        df = df.drop(['OPEN'], 1)
        df = df.drop(['HIGH'], 1)
        df = df.drop(['LOW'], 1)
        df = df.drop(['VOLUME'], 1)
        df = df.drop(['CLOSE'], 1)
        filenameOutput = definitions.IndicatorLocationFiles + '\{}.csv'.format(ticker)
        df = self.CleanDF(df)
        df.to_csv(filenameOutput)
        return df

    # clean the dataframe from np.infinity, -np.infinity and drop all NAN
    @classmethod
    def CleanDF(self, dfdata):
        dfdata.fillna(0, inplace=True)
        dfdata = dfdata.replace([np.inf, -np.inf], np.nan)
        dfdata.dropna(how='all', inplace=True)
        return dfdata

try:
    cls = Stocks()
    cls.Get_All_Indicators('AAPL')
    print('END')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    print("args:", inst.args[0])
