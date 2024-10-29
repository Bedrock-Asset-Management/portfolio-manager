# data_sources/yahoo_finance.py

import yfinance as yf
import pandas as pd
from .data_source import DataSource

class YahooFinanceSource(DataSource):
    def fetch_data(self, tickers, start_date, end_date) -> pd.DataFrame:
        data = yf.download(tickers, start=start_date, end=end_date)
        return data['Adj Close']  # Returns adjusted close prices