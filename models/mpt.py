import numpy as np
from scipy.optimize import minimize
from entities.portfolio import Portfolio

class MPTModel:
    def __init__(self):
        """
        Modern Portfolio Theory Class.
        """
        pass

    def optimize(self, assets, weights, target_return=None):
        """
        Optimize the portfolio.

        If target_return is specified, minimize the portfolio variance for the given target return.
        If target_return is None, find the minimum volatility portfolio.

        Parameters:
        - assets (list): List of assets in the portfolio.
        - weights (np.array): Initial weights of the assets.
        - target_return (float, optional): The target return of the portfolio.

        Returns:
        - np.array: The optimal weights of the assets in the portfolio.
        """
        # Objective function: portfolio variance
        temp_portfolio = Portfolio(assets, weights, name='Optimized Portfolio')
        
        def portfolio_variance(weights):
            temp_portfolio.weights = weights
            return temp_portfolio.calculate_variance()

        # Constraints
        constraints = [{'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}]  # Sum of weights equals 1

        if target_return is not None:
            # Add the target return constraint
            constraints.append({'type': 'eq', 'fun': lambda weights: Portfolio(assets, weights, name='Temp Portfolio').calculate_expected_return() - target_return})

        # Bounds of weights: between 0 and 1 (no short selling)
        bounds = tuple((0, 1) for _ in range(len(assets)))

        # Optimization
        result = minimize(
            portfolio_variance,
            weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        return result.x  # Return optimal weights
