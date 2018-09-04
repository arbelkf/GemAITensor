import pandas as pd

class Stocks():

    @classmethod
    def Get_Rsi(cls, df, n_days):
        n_days = int(n_days)
        d = df['close']

        df['closepm'] = (d + d.abs()) / 2
        df['closenm'] = (-d + d.abs()) / 2
        closepm_smma_column = 'closepm_{}_smma'.format(n_days)
        closenm_smma_column = 'closenm_{}_smma'.format(n_days)
        p_ema = df[closepm_smma_column]
        n_ema = df[closenm_smma_column]

        rs_column_name = 'rs_{}'.format(n_days)
        rsi_column_name = 'rsi_{}'.format(n_days)
        df[rs_column_name] = rs = p_ema / n_ema
        df[rsi_column_name] = 100 - 100 / (1.0 + rs)

        del df['closepm']
        del df['closenm']
        del df[closepm_smma_column]
        del df[closenm_smma_column]
        return df