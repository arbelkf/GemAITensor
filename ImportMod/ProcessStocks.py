# Auther : Kfir Arbel
# date : 6.8.2018
# ProcessStocks Class

import pandas as pd
import numpy as np
import stockstats
import os
import sys
import pickle
import definitions

class ProcessStocks:
    #'close_10.0_le_5_c' 'cr-ma2_xu_cr-ma1_20_c'
    _indexesList = ['^DJI', '^GDAXI', '^HSI', '^FCHI', '^GSPC', '^IXIC', '^N225', '^RUT', '^TYX']
    _indicators = ['volume_delta', 'open_-2_r', 'cr', 'cr-ma1', 'cr-ma2', 'cr-ma3', 'volume_-3,2,-1_max',
                        'volume_-3~1_min',
                        'kdjk', 'kdjd', 'kdjj', 'open_2_sma', 'macd', 'macds', 'macdh', 'boll', 'boll_ub', 'boll_lb',
                        'rsi_6', 'rsi_12', 'wr_10', 'wr_6', 'cci',
                        'cci_20', 'tr',
                        'atr', 'dma', 'pdi', 'mdi', 'dx', 'adx', 'adxr', 'trix', 'trix_9_sma', 'vr', 'vr_6_sma']


    def ProcessAll(self):
        data = pd.read_csv(definitions.NDXfile)
        tickers = data['ticker']
        for ticker in tickers[:]:
            sys.stdout.write('.')
            filename = '\\{}.csv'.format(ticker)
            self.ProcessStock(ticker)

    def ProcessStock(self, ticker):
        try:
            filename = "{}\{}.csv".format(definitions.ImportEndDayLocation , ticker)
            if (os.path.exists(filename)):
                print("Proccessing {}".format(ticker))
            else:
                print("Skipping {}".format(ticker))
                return
            df = pd.read_csv(filename)
            df.set_index('Date', inplace=True)
            hm_days = 15

            stock = stockstats.StockDataFrame.retype(df)
            for indicator in self._indicators:
                df['{}'.format(indicator)] = stock['{}'.format(indicator)]



            for index in self._indexesList:
                df = self.AddIndex("Indexes", index, df)


            df.dropna(inplace=True)
            destinationfilename = "{}\{}.csv".format(definitions.ImportEndDayProcessedLocation , ticker)
            df.to_csv(destinationfilename)
        except ValueError  as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)  # __str__ allows args to be printed directly,
            print("args:", inst.args[0])

    def AddIndex(self, filePathIndexes, ticker, df):
        filename = "{}\{}.csv".format(definitions.IndexesLocation, ticker)
        df2 = pd.read_csv(filename)
        df2.set_index('Date', inplace=True)
        df2.rename(columns={'Adj Close': ticker}, inplace=True)
        df2.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)
        df = df.join(df2, how='outer')

        df[ticker] = df[ticker].pct_change()
        df = df.replace([np.inf, -np.inf], 0)
        df.fillna(0, inplace=True)
        return df

process = ProcessStocks()
process.ProcessAll()
print("END")