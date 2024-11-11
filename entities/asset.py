from dataclasses import dataclass
import numpy as np
import yfinance as yf

@dataclass(frozen=True)
class Asset:
    ticker: str
    prices: np.ndarray
    returns: np.ndarray
    volatility: float

    @classmethod
    def from_ticker(cls, ticker: str, period: str = "1y") -> "Asset":
        """
        Create an Asset instance by fetching data from Yahoo Finance.

        Args:
            ticker: Stock symbol (e.g., 'AAPL')
            period: Time period for historical data (e.g., '1d', '5d', '1mo', '1y')

        Returns:
            Asset: New Asset instance with fetched data

        Raises:
            ValueError: If ticker is invalid or data fetch fails
        """
        try:
            yf_ticker = yf.Ticker(ticker)
            hist = yf_ticker.history(period=period)
            
            if (hist.empty):
                raise ValueError(f"No data found for ticker {ticker}")
            
            prices = hist['Close'].values
            return Asset(
                ticker=ticker,
                prices=prices,
                returns=np.log(prices[1:] / prices[:-1]),
                volatility=np.std(np.log(prices[1:] / prices[:-1]))
            )
        except Exception as e:
            raise ValueError(f"Error fetching data for {ticker}: {str(e)}")
    

    def __repr__(self) -> str:
        """String representation showing ticker and volatility"""
        return f"Asset(ticker={self.ticker!r}, volatility={self.volatility:.2%})"
