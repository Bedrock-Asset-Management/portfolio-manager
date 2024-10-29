class Portfolio:
    def __init__(self):
        self.assets = []
        self.weights = []
        self.risk_strategy = None
        self.optimization_strategy = None

    def add_asset(self, asset, weight):
        self.assets.append(asset)
        self.weights.append(weight)

    def set_risk_strategy(self, risk_strategy):
        self.risk_strategy = risk_strategy

    def set_optimization_strategy(self, optimization_strategy):
        self.optimization_strategy = optimization_strategy

    def calculate_portfolio_return(self):
        return sum(asset.calculate_return() * weight for asset, weight in zip(self.assets, self.weights))

    def calculate_portfolio_variance(self, covariance_matrix):
        return sum(self.weights[i] * self.weights[j] * covariance_matrix[i, j]
                   for i in range(len(self.assets)) for j in range(len(self.assets)))

    def calculate_risk(self):
        if not self.risk_strategy:
            raise ValueError("No risk strategy set")
        return self.risk_strategy.calculate(self)

    def optimize_allocation(self):
        if not self.optimization_strategy:
            raise ValueError("No optimization strategy set")
        self.weights = self.optimization_strategy.optimize(self)
