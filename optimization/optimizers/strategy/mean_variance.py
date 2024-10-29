# In optimization/strategy/mean_variance.py
from ..optimization import Optimization
from scipy.optimize import minimize
import numpy as np

class MeanVarianceOptimization(Optimization):
    def __init__(self, returns, covariance_matrix):
        self.returns = returns
        self.covariance_matrix = covariance_matrix

    def objective(self, weights):
        return np.dot(weights.T, np.dot(self.covariance_matrix, weights))

    def optimize(self, target_return):
        num_assets = len(self.returns)
        constraints = [
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x: np.dot(x, self.returns) - target_return}
        ]
        bounds = tuple((0, 1) for _ in range(num_assets))

        result = minimize(self.objective, [1/num_assets] * num_assets, bounds=bounds, constraints=constraints)
        return result.x  # Optimized weights