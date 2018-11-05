
'''
    Interface

    def ExtractLabels(self, dfdata):
    def process_data_for_labels(self, dfdata):
    def buy_sell_hold(self,*args):
    def ProcessSpecificTicker(self, ticker, skipPredict=False):


'''

import abc
import pandas as pd
import numpy as np
import sys
import definitions
from Utils import DataFrameUtils
from StatsMod.StatsUtils import Stocks
from sklearn import preprocessing
import os

class AbstractStrategy(object , metaclass=abc.ABCMeta):


    def __init__(self, name="ProcessedStocks", hm_days = 7,
                    highestLimit =  0.02, lowestLimit = 0.02):
        self._name = name

        self._hm_days = hm_days
        self._highestLimit = highestLimit
        self._lowestLimit = lowestLimit


    @property
    def Name(self):
        return self._name

    @abc.abstractmethod
    def AddPastValues(self, dfdata):
        raise NotImplementedError("Please Implement this method")




    # process ticker
    # extract labels
    # calculate accuracy and make prediction
    def ProcessSpecificTicker(self, df):
        try:
            df = self.ExtractLabels(df)
            #df = preprocessing.StandardScaler().fit_transform(df)
            return df

        except ValueError:
            print("Unexpected error:", sys.exc_info()[0])
            return None,None, None
