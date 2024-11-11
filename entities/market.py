import numpy as np
from types import MappingProxyType
from typing import Dict, List, Optional, Protocol
from datetime import datetime
from entities.asset import Asset

class MarketObserver(Protocol):
    """Protocol for objects that can receive market updates"""
    def update(self, assets: Dict[str, Asset]) -> None:
        pass

class Market:
    def __init__(self, tickers: List[str], index_symbol: str, time_range: str = "1y"):
        """Initialize market with given tickers and optional benchmark
        
        Args:
            tickers: List of asset tickers to load
            index_symbol: Ticker symbol for market index
            time_range: Time range for historical data (default: 1 year)
            
        Raises:
            ValueError: If tickers list is empty or index_symbol is invalid
        """
        if not tickers:
            raise ValueError("Tickers list cannot be empty")
            
        self._subscribers: List[MarketObserver] = []
        self._assets: Dict[str, Asset] = {}
        self._time_range = time_range
        self._last_update = datetime.now()
        
        # Load index first
        self._index = Asset.from_ticker(index_symbol, time_range)
        
        # Load all assets
        for symbol in tickers:
            self._assets[symbol] = Asset.from_ticker(symbol, self._time_range)
    
    def get_asset(self, symbol: str) -> Optional[Asset]:
        """Get asset by symbol"""
        return self._assets.get(symbol)

    @property
    def assets(self) -> Dict[str, Asset]:
        """Read-only view of assets"""
        return MappingProxyType(self._assets)

    @property
    def index(self) -> Asset:
        """Read-only view of market index"""
        return self._index

    @property
    def last_update(self) -> datetime:
        """Last market data update timestamp"""
        return self._last_update

    def subscribe(self, observer: MarketObserver) -> None:
        """Add observer to receive market updates"""
        self._subscribers.append(observer)

    def unsubscribe(self, observer: MarketObserver) -> None:
        """Remove observer from market updates"""
        if observer in self._subscribers:
            self._subscribers.remove(observer)

    def notify_subscribers(self) -> None:
        """Notify all subscribers with current market data"""
        for subscriber in self._subscribers:
            subscriber.update(self._assets)

class MarketUpdateError(Exception):
    """Custom exception for market update failures"""
    pass