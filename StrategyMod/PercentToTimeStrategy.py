import abc
from .AbstractStrategy import AbstractStrategy
from StrategyMod import Context


class PercentToTimeStrategy(AbstractStrategy):

    def AddPastValues(self, dfdata):
        hm_days = self.Hm_days
        for i in range(1, hm_days + 1):
            dfdata['Rev_{}d'.format(i)] = (dfdata['adj close'].shift(i) - dfdata['adj close'].shift(i-1)) / dfdata['adj close'].shift(i-1)

        return dfdata


    def ExtractLabels(self, dfdata):
        #print(df.iloc[-1:])
        dfdata = self.AddPastValues(dfdata)


        dfdata['target'] = dfdata['target'].shift(-1)


        del dfdata['adj close']


        # drop the last row - cause the is no y there and it anyhow save for prediction
        dfdata = dfdata.drop(dfdata.index[len(dfdata) - 1])
        return dfdata
