import numpy as np
import math

class Portfolio:
    def __init__(self, assets, weights, name):
        """
        Initialize a Portfolio instance.
        
        Parameters:
        - assets: List of Asset objects included in the portfolio.
        - weights: List of weights for each asset in the portfolio
        - name: String representing the name of the portfolio.
        
        Attributes:
        - name: Stores the portfolio name.
        - assets: Stores the list of assets in the portfolio.
        - weights: Numpy array of asset weights for easy calculations.
        - prices: Weighted sum of asset prices, representing portfolio price.
        - returns: Computed log returns of the portfolio's prices.
        """
        self.name = name
        self.assets = assets
        self.weights = np.array(weights)
        self.prices = sum(asset.prices * weight for asset, weight in zip(self.assets, self.weights))
        self.returns = self.calculate_returns()

    def calculate_returns(self):
        """
        Calculate the log returns for the portfolio based on price changes.
        
        Returns:
        - Numpy array of log returns, calculated as log of price ratios.
        """
        return np.log(self.prices[1:] / self.prices[:-1])
    
    def calculate_expected_return(self):
        """
        Calculate the expected return of the portfolio.
        
        Returns:
        - Expected annualized return based on the average daily return scaled to 252 trading days.
        """
        return self.returns.mean() * 252

    def calculate_variance(self):
        """
        Calculate the variance of the portfolio based on asset returns and weights.
        
        Returns:
        - Portfolio variance as a float, taking into account the covariance of assets,
          annualized by a factor of 252 trading days.
        """
        returns_matrix = np.array([asset.returns for asset in self.assets])
        covariance_matrix = np.cov(returns_matrix)
        return np.dot(self.weights.T, np.dot(covariance_matrix * 252, self.weights))

    def optimize_weights(self, model):
        """
        Optimize the weights of assets in the portfolio based on a given model.
        
        Parameters:
        - model: Optimization model object with an `optimize` method, which updates weights
          to achieve a certain goal (e.g., maximize returns or minimize risk).
        """
        self.weights = model.optimize(self.assets, self.weights)

    def __repr__(self):
        """
        Representation of the portfolio.
        
        Returns:
        - A string summarizing the portfolio's name, expected return, and volatility.
        """
        return f"Portfolio(name={self.name}, Return ={self.calculate_expected_return():.2%}, Volatility ={math.sqrt(self.calculate_variance()):.2%})"
