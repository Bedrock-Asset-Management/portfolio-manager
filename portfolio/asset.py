import numpy as np

class Asset:
    def __init__(self, symbol, prices):
        """
        Initialise un actif avec un nom et une liste de prix.

        :param symbol: Nom de l'actif (str)
        :param prices: Prix de l'actif (array 1D)
        """
        self.symbol = symbol
        self.prices = np.array(prices)
        self.returns = self.calculate_returns()
        self.volatility = self.calculate_volatility()
    
    def calculate_returns(self):
        """
        Calculate logarithmic returns of the asset from prices.
        """
        return np.log(self.prices[1:] / self.prices[:-1])
    

    def calculate_volatility(self):
        """
        Calcule la volatilité de l'actif.

        :return: Volatilité (float)
        """
        return np.std(self.returns)

    def __repr__(self):
        return f"Asset(name={self.symbol}, volatility={self.volatility:.2%})"