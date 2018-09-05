import pandas as pd
import numpy as np
from .Indicators import Indicators
import definitions

class Stocks():

    @classmethod
    def Get_All_Indicators(self, ticker):
        filenameInput = definitions.IMPORTLocationFiles + '\{}.csv'.format(ticker)
        df = pd.read_csv(filenameInput)
        cls = Indicators()
        df = cls.Get_Rsi(df, 14)
        filenameOutput = definitions.IndicatorLocationFiles + '\{}.csv'.format(ticker)
        df.to_csv(filenameOutput)
        return df

    # clean the dataframe from np.infinity, -np.infinity and drop all NAN
    def CleanDF(self, dfdata):
        dfdata.fillna(0, inplace=True)
        dfdata = dfdata.replace([np.inf, -np.inf], np.nan)
        dfdata.dropna(how='all', inplace=True)
        return dfdata


cls = Stocks()
cls.Get_All_Indicators('AAPL')