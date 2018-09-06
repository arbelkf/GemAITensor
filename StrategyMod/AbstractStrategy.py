
import abc
import pandas as pd
import numpy as np
import definitions
from StatsMod.StatsUtils import Stocks

class AbstractStrategy(object , metaclass=abc.ABCMeta):


    def __init__(self, name="ProcessedStocks", hm_days = 7,
                    highestLimit =  0.02, lowestLimit = 0.02):
        self._hm_days = hm_days
        self._highestLimit = highestLimit
        self._lowestLimit = lowestLimit
        self._name = name


    @property
    def hm_days(self):
        return self._hm_days

    @property
    def Name(self):
        return self._name

    @property
    def HighestLimit(self):
        return self._highestLimit

    @property
    def LowestLimit(self):
        return self._lowestLimit

    @abc.abstractmethod
    def ExtractLabels(self, dfdata):
        raise NotImplementedError("Please Implement this method")

    @abc.abstractmethod
    def process_data_for_labels(self, dfdata):
        raise NotImplementedError("Please Implement this method")

    @abc.abstractmethod
    def buy_sell_hold(self,*args):
        raise NotImplementedError("Please Implement this method")

    # add indexes to the dataframe
    # ticker = name of the index
    # df - the datafarem to add the index to
    def AddRSI(self, ticker, df, cls = Stocks()):

        #df2 = pd.read_csv(definitions.IMPORTLocationFiles + '\{}.csv'.format(ticker))
        #df2.set_index('Date', inplace=True)
        #df2.rename(columns={'Adj Close': ticker}, inplace=True)
        #df2.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)
        #df = df.join(df2, how='inner')

        df = cls.Get_Rsi(df, 14)
        return df

    # collect data for specific ticker and pass to the ProcessTicker
    def ProcessSpecificTicker(self, ticker, skipPredict=False):
        print("Processing using {} clf {} high {} low {} hm {}".format(self._name, self.Clf_Name, self._highestLimit,
                                                                     self._lowestLimit, self._hm_days))
        self.buy_sell_hold()
