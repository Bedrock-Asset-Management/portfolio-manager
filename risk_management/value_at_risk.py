from .risk_management import RiskManagement
import numpy as np

class ValueAtRisk(RiskManagement):
    def calculate(self, portfolio, confidence_level=0.95):
        portfolio_returns = [asset.calculate_return() for asset in portfolio.assets]
        mean = np.mean(portfolio_returns)
        std_dev = np.std(portfolio_returns)
        var = mean - std_dev * np.percentile(np.random.normal(size=10000), confidence_level * 100)
        return var