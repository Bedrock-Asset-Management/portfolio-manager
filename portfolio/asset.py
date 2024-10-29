class Asset:
    def __init__(self, ticker, returns):
        self.ticker = ticker
        self.returns = returns

    def calculate_return(self):
        return sum(self.returns) / len(self.returns)