#kfir
import os
import datetime as dt

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NDXfile = os.path.join(ROOT_DIR, 'ImportMod\\ndx.csv')
IMPORTLocationFiles = os.path.join(ROOT_DIR, "ImportMod\\Imported")
IndicatorLocationFiles = os.path.join(ROOT_DIR, "ImportMod\\Indicators")
IndicatorEndDayLocation = os.path.join(ROOT_DIR, 'ImportMod\\EndDayIndicators')
IndexesLocation = os.path.join(ROOT_DIR, 'ImportMod\\Indexes')
ImportEndDayStartDate = dt.datetime(1995, 1, 1)
ImportEndDayEndDate = dt.datetime(2018, 10, 30)
ImportEndDayLocation = os.path.join(ROOT_DIR, 'ImportMod\\ImportEndDay')
ImportEndDayProcessedLocation = os.path.join(ROOT_DIR, 'ImportMod\\ImportedEndDayIndicators')
TempExcelFile = os.path.join(ROOT_DIR, 'pdsimple.xlsx')
IndexesList = ['^DJI','^GDAXI','^HSI','^FCHI','^GSPC','^IXIC', '^N225','^RUT', '^TYX']
