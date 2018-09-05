import pandas as pd
import numpy as np
from StatsMod import Indicators
import definitions

class Stocks():

    @classmethod
    def Get_All_Indicators(self, ticker):
        filenameInput = definitions.IMPORTLocationFiles + '\{}.csv'.format(ticker)
        df = pd.read_csv(filenameInput)
        indi = Indicators.Indicators()
        df['rsi'] = indi.rsiFunc(df['CLOSE'], 14)
        filenameOutput = definitions.IndicatorLocationFiles + '\{}.csv'.format(ticker)
        df.to_csv(filenameOutput)
        return df

    # clean the dataframe from np.infinity, -np.infinity and drop all NAN
    def CleanDF(self, dfdata):
        dfdata.fillna(0, inplace=True)
        dfdata = dfdata.replace([np.inf, -np.inf], np.nan)
        dfdata.dropna(how='all', inplace=True)
        return dfdata

try:
    cls = Stocks()
    cls.Get_All_Indicators('AAPL')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    print("args:", inst.args[0])
