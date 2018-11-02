import pandas as pd
apikey = 'ccea31da69ac8112da76adbe03b27e0e'


def construct_barChart_url(sym, start_date, freq, api_key=apikey):
    '''Function to construct barchart api url'''

    url = 'http://marketdata.websol.barchart.com/getHistory.csv?' + \
          'key={}&symbol={}&type={}&startDate={}'.format(api_key, sym, freq, start_date)

    return url


start = '20150831000000'
freq = 'minutes'
prices = {}
try:

    api_url = construct_barChart_url('GOOG', start, freq, api_key=apikey)
    csvfile = pd.read_csv(api_url, parse_dates=['timestamp'])
    csvfile.set_index('timestamp', inplace=True)
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    csvfile.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
except Exception as inst:
    msg = "args:", inst.args[0]
    print(msg)




