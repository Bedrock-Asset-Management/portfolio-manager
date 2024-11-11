import numpy as np
from scipy.optimize import minimize
from typing import List, Optional  
from dataclasses import dataclass
from entities.portfolio import Portfolio

@dataclass
class OptimizationResult:
    """Container for optimization results"""
    weights: np.ndarray
    expected_return: float
    volatility: float
    sharpe_ratio: float

class MPTModel:
    def __init__(self):
        self.efficient_frontier: List[OptimizationResult] = []
        self.min_vol_portfolio: Optional[OptimizationResult] = None
        self.max_sharpe_portfolio: Optional[OptimizationResult] = None
    
    def _validate_inputs(self, assets: List[str], weights: np.ndarray) -> None:
        """Validate optimization inputs"""
        if len(assets) != len(weights):
            raise ValueError("Number of assets must match weights length")
        if not np.isclose(np.sum(weights), 1.0):
            raise ValueError("Initial weights must sum to 1")
            
    def optimize(self, assets: List[str], weights: np.ndarray, 
                target_return: Optional[float] = None) -> OptimizationResult:
        """Optimize portfolio weights for minimum variance"""
        try:
            self._validate_inputs(assets, weights)
            temp_portfolio = Portfolio(assets, weights, name='Temp')
            
            constraints = [
                {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}  # weights sum to 1
            ]
            
            if target_return is not None:
                constraints.append({
                    'type': 'eq',
                    'fun': lambda w: self._portfolio_return(temp_portfolio, w) - target_return
                })
                
            bounds = tuple((0, 1) for _ in range(len(assets)))
            
            result = minimize(
                lambda w: self._portfolio_variance(temp_portfolio, w),
                weights,
                method='SLSQP',
                bounds=bounds,
                constraints=constraints
            )
            
            if not result.success:
                raise OptimizationError(f"Optimization failed: {result.message}")
            
            return OptimizationResult(
                weights=result.x,
                expected_return=self._portfolio_return(temp_portfolio, result.x),
                volatility=np.sqrt(self._portfolio_variance(temp_portfolio, result.x)),
                sharpe_ratio=self._calculate_sharpe(temp_portfolio, result.x)
            )
            
        except Exception as e:
            raise OptimizationError(f"Portfolio optimization failed: {str(e)}")
    
    def calculate_efficient_frontier(self, assets: List[str], weights: np.ndarray, 
                                  points: int = 100) -> List[OptimizationResult]:
        """Calculate efficient frontier points"""
        min_vol_port = self.optimize(assets, weights)
        max_ret_port = self._maximize_return(assets, weights)
        
        target_returns = np.linspace(
            min_vol_port.expected_return,
            max_ret_port.expected_return,
            points
        )
        
        self.efficient_frontier = [
            self.optimize(assets, weights, target_return=r)
            for r in target_returns
        ]
        
        return self.efficient_frontier
    
    def _portfolio_variance(self, portfolio: Portfolio, weights: np.ndarray) -> float:
        """Calculate portfolio variance"""
        portfolio.weights = weights
        return portfolio.calculate_variance()
    
    def _portfolio_return(self, portfolio: Portfolio, weights: np.ndarray) -> float:
        """Calculate expected portfolio return"""
        portfolio.weights = weights
        return portfolio.calculate_expected_return()
    
    def _calculate_sharpe(self, portfolio: Portfolio, weights: np.ndarray) -> float:
        """Calculate portfolio Sharpe ratio"""
        portfolio.weights = weights
        return portfolio.calculate_sharpe()
        
    def _maximize_return(self, assets: List[str], weights: np.ndarray) -> OptimizationResult:
        """Find maximum return portfolio on efficient frontier"""
        portfolio = Portfolio(assets, weights, name='Max Return')
        
        result = minimize(
            lambda w: -self._portfolio_return(portfolio, w),
            weights,
            method='SLSQP',
            bounds=tuple((0, 1) for _ in range(len(assets))),
            constraints=[{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
        )
        
        return OptimizationResult(
            weights=result.x,
            expected_return=self._portfolio_return(portfolio, result.x),
            volatility=np.sqrt(self._portfolio_variance(portfolio, result.x)),
            sharpe_ratio=self._calculate_sharpe(portfolio, result.x)
        )

class OptimizationError(Exception):
    """Custom exception for optimization failures"""
    pass
