from StrategyMod import PercentToTimeStrategy
from StrategyMod import Context

class Predictor(object):

    def __init__(self):
        print("Start...")
        self._StrategyList = []
        strategy = PercentToTimeStrategy.PercentForPeriodStrategy(isIndicatorLongList=False,
                                                                  highestLimit=0.02, lowestLimit=0.02, hm_days=7,
                                                                  name="ProcessedStocks")
        self._strategyList.append(strategy)
        cls = PercentToTimeStrategy()

    def DoStrategy(self, strategy, ticker):
        context = Context(strategy)
        acc, confusionmatrix, final = context.ProcessSpecificTicker(ticker)
        return acc, confusionmatrix, final

        # find accuuracy & predict for specific ticker

    def PredictTicker(self, ticker):

        try:
            print("Processing:{}".format(ticker))


            # interate all the strategies in the array
            for str in self._StrategyList:
                self.DoStrategy(str,ticker)


cls = Predictor()
cls.PredictTicker('AAPL')