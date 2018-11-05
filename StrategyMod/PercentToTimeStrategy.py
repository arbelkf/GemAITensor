import abc
from .AbstractStrategy import AbstractStrategy
from StrategyMod import Context
import pandas as pd
import definitions
from sklearn import preprocessing

class PercentToTimeStrategy(AbstractStrategy):

    def AddPastValues(self, dfdata):
        hm_days = self.Hm_days
        for i in range(1, hm_days + 1):
            dfdata['Rev_{}d'.format(i)] = (dfdata['adj close'].shift(i) - dfdata['adj close'].shift(i-1)) / dfdata['adj close'].shift(i-1)

        return dfdata


    def ExtractLabels(self, dfdata):
        #print(df.iloc[-1:])
        #dfdata = self.AddPastValues(dfdata)

        del dfdata['Date']
        del dfdata['open']
        del dfdata['high']
        del dfdata['low']
        del dfdata['close']
        del dfdata['volume']

        dfdata.rename(columns={'adj close': 'target'}, inplace=True)
        dfdata['target'] = dfdata['target'].shift(-1)

        #dfdata = preprocessing.StandardScaler().fit_transform(dfdata)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(definitions.TempExcelFile , engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        dfdata.to_excel(writer, sheet_name='Sheet1')

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


        #del dfdata['adj close']


        # drop the last row - cause the is no y there and it anyhow save for prediction
        #dfdata = dfdata.drop(dfdata.index[len(dfdata) - 1])
        return dfdata
