import numpy as np

class Asset:
    def __init__(self, name, prices):
        """
        Initialise un actif avec un nom et une liste de prix.

        :param name: Nom de l'actif (str)
        :param prices: Prix de l'actif (array 1D)
        """
        self.name = name
        self.prices = np.array(prices)
        self.returns = self.calculate_log_returns()

    def calculate_log_returns(self):
        """
        Calcule les rendements logarithmiques de l'actif.

        :return: Rendements logarithmiques (array 1D)
        """
        return np.log(self.prices[1:] / self.prices[:-1])

    def volatility(self):
        """
        Calcule la volatilité de l'actif.

        :return: Volatilité (float)
        """
        return np.std(self.returns)

    def __repr__(self):
        return f"Asset(name={self.name}, volatility={self.volatility():.2%})"