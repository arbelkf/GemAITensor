
import abc

class AbstractStrategy(object , metaclass=abc.ABCMeta):


    def __init__(self, name="ProcessedStocks", isIndicatorLongList = True, hm_days = 7):
        if (isIndicatorLongList == False):
            self._indicators = ['atr', 'boll', 'boll_ub','boll_lb','open_2_sma','cr-ma3', 'volume_-3~1_min',
                                'vr_6_sma','cr-ma2','trix_9_sma','volume_-3,2,-1_max','vr',
                                'macds','adxr','cr-ma1','dma']

        else:
            self._indicators = ['volume_delta', 'open_-2_r', 'cr', 'cr-ma1', 'cr-ma2', 'cr-ma3', 'volume_-3,2,-1_max', 'volume_-3~1_min',
                      'kdjk', 'kdjd', 'kdjj', 'open_2_sma', 'macd', 'macds', 'macdh', 'boll', 'boll_ub', 'boll_lb',
                      'close_10.0_le_5_c', 'cr-ma2_xu_cr-ma1_20_c', 'rsi_6', 'rsi_12', 'wr_10', 'wr_6', 'cci', 'cci_20', 'tr',
                      'atr', 'dma', 'pdi', 'mdi', 'dx', 'adx', 'adxr', 'trix', 'trix_9_sma', 'vr', 'vr_6_sma']
        self._hm_days = hm_days


    @property
    def Indicators(self):
        return self._indicators

    @property
    def hm_days(self):
        return self._hm_days
