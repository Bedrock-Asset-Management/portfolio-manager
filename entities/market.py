from asset import Asset
import numpy as np
from types import MappingProxyType
from typing import Dict, List, Optional, Protocol
from datetime import datetime

class MarketObserver(Protocol):
    """Protocol for objects that can receive market updates"""
    def update(self, market_data: Dict) -> None: ...

class Market:
    def __init__(self, benchmark_symbol: str = "^GSPC"):
        self._subscribers: List[MarketObserver] = []
        self._assets: Dict[str, Asset] = {}
        self._market_data: Dict[str, Dict] = {}
        self._benchmark: Asset = Asset.from_ticker(benchmark_symbol)
        self._market_data[benchmark_symbol] = self._update_market_data(benchmark_symbol, self.benchmark)

    @property
    def assets(self) -> Dict[str, Asset]:
        """Read-only view of assets"""
        return self._assets

    @property
    def benchmark(self) -> Asset:
        """Read-only view of market benchmark"""
        return MappingProxyType(self._benchmark)

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
            subscriber.update(self._market_data)

    def update_asset(self, symbol: str, period: str = "1d") -> None:
        """Update specific asset with fresh data"""
        if symbol not in self._assets:
            raise KeyError(f"Asset {symbol} not in market")
    
        try:
            updated_asset = Asset.from_ticker(symbol, period)
            self._assets[symbol] = updated_asset
            self._update_market_data(symbol, updated_asset)
        except Exception as e:
            raise MarketUpdateError(f"Failed to update {symbol}: {str(e)}")

    def update_all(self, period: str = "1d") -> None:
        """Update all assets with fresh data"""
        for symbol in self._assets:
            try:
                self.update_asset(symbol, period)
            except Exception as e: # REDONANT ?
                print(f"Error updating {symbol}: {e}")

    def add_asset(self, asset: Asset) -> None:
        """Add new asset to market"""
        self._assets[asset.ticker] = asset
        self._update_market_data(asset.ticker, asset)

    def remove_asset(self, symbol: str) -> None:
        """Remove asset from market"""
        if symbol in self._assets:
            del self._assets[symbol]
            if symbol in self._market_data:
                del self._market_data[symbol]
            self.notify_subscribers()

    def get_asset(self, symbol: str) -> Optional[Asset]:
        """Get asset by symbol"""
        return self._assets.get(symbol)

    def _update_market_data(self, symbol: str, asset: Asset) -> None:
        """Internal method to update market data and notify"""
        self._market_data[symbol] = {
            'price': asset.prices[-1],
            'returns': asset.returns[-1] if len(asset.returns) > 0 else None,
            'volatility': asset.volatility,
            'last_update': datetime.now()
        }
        self.notify_subscribers()

class MarketUpdateError(Exception):
    """Custom exception for market update failures"""
    pass