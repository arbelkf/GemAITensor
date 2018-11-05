# Auther : Kfir Arbel
# date : 6.8.2018
# Main Class

# Import Module - imports all or specific - stock or indexes
# StrategyModule - diffrent strategies to decide about the labels
# GemAIModule - runs diffrent kinds of prediction procedures
from ImportMod.Import import ImportUtil
from GemAITensorMod.TensorStrategy import TensorStrategy
from StatsMod.StatsUtils import Stocks
import sys
import logging

print("Write \"import\" - to import all tickers and indexes")
print("Write \"indi all\" - to import all tickers")
print("Write \"indi ticker\" - to import specific ticker")
print("Write \"chk ticker\" - to machine learn a specific ticker")
str = sys.stdin.readline()
#while(str != "END\n"):
try:
    strparam = str.split()
    if (strparam[0] == "import"):
        cls = ImportUtil()
        cls.GetAllSymbols()
        cls.Get_indexes()
        print("END")
    if (strparam[0] == "indi"):
        ticker = strparam[1]
        cls = Stocks()
        if (ticker == 'all'):
            cls.GetAllTickersIndicators()
        else:
            cls.Get_All_Indicators(ticker)
        print("END")
    if (strparam[0] == "chk"):
        ticker = strparam[1]
        cls = TensorStrategy()
        cls.RunPrediction(ticker)
except Exception as inst:
    msg = "args:", inst.args[0]
    print(msg)
    logging.error(msg)
    #str = sys.stdin.readline()
