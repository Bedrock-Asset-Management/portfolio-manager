from typing import Dict, List
from dataclasses import dataclass
import numpy as np
from entities.market import Market, MarketObserver

@dataclass
class Portfolio(MarketObserver):
    name: str
    market: Market
    asset_symbols: List[str]
    weights: np.ndarray
    risk_free_rate: float = 0.0431 # Annual risk-free rate

    def __post_init__(self):
        # Validate weights sum to 1
        if not np.isclose(np.sum(self.weights), 1.0):
            raise ValueError("Weights must sum to 1")
        
        # Validate weights length matches assets
        if len(self.weights) != len(self.asset_symbols):
            raise ValueError("Weights length must match number of assets")
        
        # Validate all symbols exist in market
        for symbol in self.asset_symbols:
            if not self.market.get_asset(symbol):
                raise ValueError(f"Asset {symbol} not found in market")
        self._update_metrics()

    def update(self, market_data: Dict) -> None:
        """Recalculate metrics when market updates"""
        self._update_metrics()
        
    def _update_metrics(self) -> None:
        """Calculate all portfolio risk metrics"""
        self.prices: np.ndarray = self._calculate_portfolio_prices()
        self.returns: np.ndarray = np.log(self.prices[1:] / self.prices[:-1]) # Log returns
        self.volatility: float = np.std(self.returns) * np.sqrt(252)  # Annualized
        self.expected_return: float = np.mean(self.returns) * 252  # Annualized
        self.risk_premium: float = self.expected_return - self.risk_free_rate
        self.beta: float = self._calculate_beta()
        self.sharpe: float = self._calculate_sharpe()
        self.treynor: float = self._calculate_treynor()
    
    def _calculate_portfolio_prices(self) -> np.ndarray:
        """Calculate weighted sum of asset returns using market data"""
        return np.dot(self.weights, [self.market.get_asset(symbol).prices for symbol in self.asset_symbols])
    
    def _calculate_sharpe(self) -> float:
        """
        Calculate portfolio Sharpe ratio
        
        Raises:
            ValueError: If portfolio volatility is zero
        """
        if self.volatility == 0:
            raise ValueError("Portfolio volatility is zero")
        return self.risk_premium / self.volatility

    def _calculate_beta(self) -> float:
        """Calculate portfolio beta relative to market index 
        
        Beta = Cov(Portfolio Returns, Market Returns) / Var(Market Returns)
        """
        index_returns = self.market.index.returns
        
        # Calculate beta
        market_var = self.market.index.volatility ** 2
        if market_var == 0:
            raise ValueError("Market variance is zero")
            
        covariance = np.cov(self.returns, index_returns)[0, 1]
        return covariance / market_var
    
    def _calculate_treynor(self) -> float:
        """
        Calculate portfolio Treynor ratio
        
        Raises:
            ValueError: If portfolio beta is zero
        """
        if self.beta == 0:
            raise ValueError("Portfolio beta is zero") 
        return self.risk_premium / self.beta
    
    def __repr__(self) -> str:
        return f"Portfolio(name={self.name!r}, volatility={self.volatility:.2%}, expected_return={self.expected_return:.2%}, beta={self.beta:.2f}, sharpe={self.sharpe:.2f}, treynor={self.treynor:.2f})"