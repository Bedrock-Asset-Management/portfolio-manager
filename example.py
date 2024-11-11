# %%
from entities.market import Market
from entities.portfolio import Portfolio
from entities.asset import Asset
from models.mpt import MPTModel
import numpy as np
import matplotlib.pyplot as plt
import json

# %%

# Initialize market with tech stocks and S&P500 benchmark

# get tickers from ../data/index_tickers.json
with open("utils/data/index_tickers.json", "r") as open_file:
    indexes = json.load(open_file)

market = Market(
    tickers=indexes["CAC 40"],
    index_symbol="^FCHI", 
)

# %%
#print all the assets in the market
print("Market Assets:")
for symbol, asset in market.assets.items():
    print(f"{symbol}: {asset.volatility:.2%}")

# %%

# Create portfolio with equal weights
portfolio = Portfolio(
    name='Tech Portfolio',
    market=market,
    asset_symbols=['AIR.PA', 'AI.PA', 'BNP.PA', 'ENGI.PA', 'KER.PA', 'OR.PA', 'MC.PA', 'RI.PA', 'SAN.PA', 'SU.PA', 'VIV.PA'],
    weights=np.ones(11)/11
)

print("\nInitial Portfolio Metrics:")
print(f"Volatility: {portfolio.volatility:.2%}")
print(f"Beta: {portfolio.beta:.2f}")
print(f"Sharpe: {portfolio.sharpe:.2f}")
