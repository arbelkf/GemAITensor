import requests
import numpy as np
import pandas as pd
import arrow
import datetime
import definitions
import os
import logging

#remark

class ImportUtil():
    def GetQuoteDataForSymbol(self, symbol='SBIN.NS', data_range='1d', data_interval='1m'):
        res = requests.get(
            'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={data_range}&interval={data_interval}'.format(
                **locals()))
        data = res.json()
        if (data['chart']['result'] == None):
            return pd.DataFrame()
        body = data['chart']['result'][0]
        dt = datetime.datetime
        dt = pd.Series(map(lambda x: arrow.get(x).to('Asia/Calcutta').datetime.replace(tzinfo=None), body['timestamp']),
                       name='Datetime')
        df = pd.DataFrame(body['indicators']['quote'][0], index=dt)
        dg = pd.DataFrame(body['timestamp'])
        df = df.loc[:, ('open', 'high', 'low', 'close', 'volume')]
        df.dropna(inplace=True)  # removing NaN rows
        df.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']  # Renaming columns in pandas

        return df

    def GetAllSymbols(self):
        data = pd.read_csv(definitions.NDXfile)
        tickers = data['ticker']
        for ticker in tickers[:]:
            try:
                df = self.GetQuoteDataForSymbol(ticker, '1d', '1m')
                if (df.size > 1):
                    filename = definitions.IMPORTLocationFiles + '/{}.csv'.format(ticker)
                    df.to_csv(filename)
                    print('.')

            except Exception as inst:
                msg = "cant find {} ".format(ticker) + "args:", inst.args[0]
                print(msg)
                logging.error(msg)
#cls = ImportUtil()
#cls.GetAllSymbols('AAPL', '1d', '1m')
#cls.GetAllSymbols()
#print('END')
