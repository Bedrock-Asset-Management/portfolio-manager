from abc import ABC, abstractmethod
import pandas as pd

class DataSource(ABC):
    @abstractmethod
    def fetch_data(self, tickers, start_date, end_date) -> pd.DataFrame:
        """
        Fetch historical data for specified tickers within the date range.
        Returns:
            DataFrame with price data.
        """
        pass