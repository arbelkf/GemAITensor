


from datetime import datetime
ts = int("1491226200")
ts2 = int("1504201440")

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.utcfromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S'))