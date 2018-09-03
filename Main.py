# Auther : Kfir Arbel
# date : 6.8.2018
# Main Class

# Import Module - imports all or specific - stock or indexes
# StrategyModule - diffrent strategies to decide about the labels
# GemAIModule - runs diffrent kinds of prediction procedures
from ImportMod.Import import ImportUtil
import sys

print("Write \"import\" - to imp[ort all tickers")
str = sys.stdin.readline()
while(str != "END\n"):
    strparam = str.split()
    if (strparam[0] == "import"):
        cls = ImportUtil()
        cls.GetAllSymbols()
        print("END")
    str = sys.stdin.readline()
