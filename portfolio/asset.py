import numpy as np

class Asset:
    def __init__(self, name, symbol, prices, dividends=None):
        """
        Initialize the Asset with basic properties.

        :param name: str, the name of the asset (e.g., "Apple Inc.")
        :param symbol: str, the ticker symbol of the asset (e.g., "AAPL")
        :param prices: list or array, historical price data
        :param dividends: list or array, historical dividends (optional)
        """
        self.name = name
        self.symbol = symbol
        self.prices = prices  # Historical daily closing prices
        self.dividends = dividends if dividends else []  # Optional dividend data

    def __repr__(self):
        """String representation for debugging and logging."""
        return f"Asset({self.name}, {self.symbol})"

    # Property for the latest price
    @property
    def latest_price(self):
        """Returns the most recent price."""
        return self.prices[-1] if self.prices else None

    # Property for historical prices
    @property
    def price_history(self):
        """Returns the full historical price data."""
        return self.prices

    # Method to add new prices (e.g., for live updates)
    def add_price(self, price):
        """Append a new price to the price history."""
        self.prices.append(price)

    # Method to add new dividend (if applicable)
    def add_dividend(self, dividend):
        """Append a new dividend to the dividend history."""
        if self.dividends is not None:
            self.dividends.append(dividend)

    def calculate_return(self, method="simple"):
        """
        Calculate return based on the specified method.
        
        :param method: str, the return calculation method
                       "simple" - Simple (absolute) return
                       "log" - Logarithmic return
                       "arithmetic" - Arithmetic average return
                       "geometric" - Geometric average return (CAGR)
                       "holding" - Holding period return with dividends
                       "annualized" - Annualized return over the period
        :return: float, the calculated return
        """
        if method == "simple":
            # Simple (absolute) return
            return (self.prices[-1] - self.prices[0]) / self.prices[0]
        
        elif method == "log":
            # Logarithmic (continuous) return
            return np.log(self.prices[-1] / self.prices[0])
        
        elif method == "arithmetic":
            # Arithmetic average of daily returns
            daily_returns = np.diff(self.prices) / self.prices[:-1]
            return np.mean(daily_returns)
        
        elif method == "geometric":
            # Geometric average return (CAGR)
            total_return = (self.prices[-1] / self.prices[0])
            return total_return ** (1 / len(self.prices)) - 1
        
        elif method == "holding":
            # Holding period return, including dividends if available
            dividend_sum = np.sum(self.dividends) if self.dividends is not None else 0
            return (self.prices[-1] + dividend_sum - self.prices[0]) / self.prices[0]
        
        elif method == "annualized":
            # Annualized return over the entire period
            total_return = (self.prices[-1] / self.prices[0])
            return (total_return ** (252 / len(self.prices))) - 1  # Assuming 252 trading days per year
        
        else:
            raise ValueError(f"Unknown method: {method}")
