import yfinance as yf
import pandas as pd
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def fetch_data(self, tickers, start_date, end_date) -> pd.DataFrame:
        """
        Fetch historical data for specified tickers within the date range.
        Returns:
            DataFrame with price data.
        """
        pass

class YahooFinance(DataSource):
    def fetch_data(self, tickers, start_date, end_date) -> pd.DataFrame:
        """
        Fetch historical data from Yahoo Finance.
        
        Parameters:
        - tickers (list of str): List of stock symbols, e.g., ['AAPL', 'GOOG'].
        - start_date (str): Start date for the data in 'YYYY-MM-DD' format.
        - end_date (str): End date for the data in 'YYYY-MM-DD' format.
        
        Returns:
        - pd.DataFrame: DataFrame with dates as index and columns for each ticker's adjusted close prices.
        """
        # Fetch data with yfinance
        data = yf.download(tickers, start=start_date, end=end_date)
        
        # Extract the 'Adj Close' 
        adj_close_data = data['Adj Close']
        
        # If only one ticker is provided, yfinance returns a Series instead of DataFrame, so we handle that case
        if isinstance(adj_close_data, pd.Series):
            adj_close_data = adj_close_data.to_frame(name=tickers[0])

        return adj_close_data
