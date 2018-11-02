import definitions
import os, sys
import pandas as pd
import pandas_datareader as web
import logging

class ImportUtil(object):

    def take_first(self, array_like):
        return array_like[0]


    def take_last(self, array_like):
        return array_like[-1]


    def GetTickers(self, tickers, filepath):

        for ticker in tickers[:]:
            sys.stdout.write('.')
            filename = filepath +'/{}.csv'.format(ticker)

            if not os.path.exists(filename):
                try:
                    df = web.DataReader(ticker, 'yahoo', definitions.ImportEndDayStartDate , definitions.ImportEndDayEndDate)
                    df.to_csv(filename)

                    msg = "Getting {}".format(ticker)
                    print(msg)
                    #logging.Info(msg)
                except Exception as inst:
                    msg = "cant find {} ".format(ticker) + "args:", inst.args[0]
                    print(msg)
                    logging.error(msg)

    def get_ndx_data_from_yahoo(self):

        data = pd.read_csv(definitions.NDXfile)
        tickers = data['ticker']
        filepath = definitions.ImportEndDayLocation
        if not os.path.exists(filepath):
                os.makedirs(filepath)

        self.GetTickers(tickers, filepath)

    def get_indexes(self):

        tickers = definitions.IndexesList
        self.GetTickers(tickers, definitions.IndexesLocation)

cls = ImportUtil()
cls.get_indexes()