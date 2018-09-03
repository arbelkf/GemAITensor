# Auther : Kfir Arbel
# date : 6.8.2018
# Main Class

# Import Module - imports all or specific - stock or indexes
# StrategyModule - diffrent strategies to decide about the labels
# GemAIModule - runs diffrent kinds of prediction procedures
from ImportMod.Import import ImportUtil
from GemAITensorMod.TensorStrategy import TensorStrategy
import sys
import logging

print("Write \"import\" - to import all tickers")
str = sys.stdin.readline()
while(str != "END\n"):
    try:
        strparam = str.split()
        if (strparam[0] == "import"):
            cls = ImportUtil()
            cls.GetAllSymbols()
            print("END")
        if (strparam[0] == "chk"):
            ticker = strparam[1]
            cls = TensorStrategy()
            cls.DoStrategy(ticker)
    except Exception as inst:
        msg = "args:", inst.args[0]
        print(msg)
        logging.error(msg)
    #str = sys.stdin.readline()
