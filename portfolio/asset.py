import numpy as np

class Asset:
    def __init__(self, ticker, prices):
        """
        Initializes an asset with a name and a list of prices.

        Attributes:
        - ticker: String representing the name of the asset
        - prices: Numpy 1D array of historical prices for the asset
        - returns: Numpy array of logarithmic returns
        - volatility: Standard deviation of returns
        
        Parameters:
        - ticker: Name (ticker) of the asset
        - prices: Historical prices of the asset
        """
        self.ticker = ticker
        self.prices = np.array(prices)
        self.returns = self.calculate_returns()
        self.volatility = self.calculate_volatility()
    
    def calculate_returns(self):
        """
        Calculate logarithmic returns of the asset from prices

        Returns:
        - Numpy Array of logarithmic returns
        """
        return np.log(self.prices[1:] / self.prices[:-1])
    
    def calculate_volatility(self):
        """
        Calculate the volatility of the asset based on the standard deviation of returns

        Returns:
        - Volatility of the asset
        """
        return np.std(self.returns)

    def __repr__(self):
        """
        String representation of the Asset object

        Returns:
        - A string showing the asset's name and volatility in percentage format
        """
        return f"Asset(name={self.ticker}, volatility={self.volatility:.2%})"
