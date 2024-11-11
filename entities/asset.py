from dataclasses import dataclass
import numpy as np
import yfinance as yf

from typing import Optional

@dataclass(frozen=True)
class Asset:
    # Define required fields
    ticker: str
    prices: np.ndarray 
    returns: np.ndarray
    expected_return: float
    volatility: float

    @classmethod
    def from_ticker(cls, ticker: str, period: str = "ytd") -> "Asset":
        """Create Asset instance from Yahoo Finance data"""
        try:
            print(f"Fetching data for {ticker} with period:{period}...")
            yf_ticker = yf.Ticker(ticker)
            hist = yf_ticker.history(period=period)
            
            if hist.empty:
                raise ValueError(f"No data found for ticker {ticker}")
            
            prices = hist['Close'].values
            returns = np.log(prices[1:] / prices[:-1])
            expected_return = np.mean(returns)
            return cls(
                ticker=ticker,
                prices=prices,
                returns=returns,
                expected_return=expected_return,
                volatility=np.std(returns)
            )
        except Exception as e:
            raise ValueError(f"Error fetching data for {ticker}: {str(e)}")

    def __repr__(self) -> str:
        return f"Asset(ticker={self.ticker!r}, volatility={self.volatility:.2%})"
