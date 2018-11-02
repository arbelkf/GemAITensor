
class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def ProcessSpecificTicker(self, ticker):
        X, y = self._strategy.ProcessSpecificTicker(ticker)
        return X, y
