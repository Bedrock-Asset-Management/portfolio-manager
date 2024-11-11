import json
import numpy as np
from market import Market
from asset import Asset
from portfolio import Portfolio

# 1. Load indices data
with open("indices_tickers.json", "r") as file:
    indices = json.load(file)

# 2. Create market with CAC40 index as benchmark
cac40_market = Market(benchmark_symbol="^FCHI")

# 3. Add CAC40 stocks to market 
cac40_tickers = indices["CAC 40"]
for ticker in cac40_tickers:
    try:
        asset = Asset.from_ticker(ticker)
        cac40_market.add_asset(asset)
    except Exception as e:
        print(f"Failed to add {ticker}: {e}")

# 4. Create equally weighted portfolio
cac40_portfolio = Portfolio(
    name="CAC40 Portfolio",
    market=cac40_market,
    asset_symbols=list(cac40_market.assets.keys()),
    weights=np.array([1/len(cac40_market.assets)] * len(cac40_market.assets))
)

# 5. Subscribe portfolio to market updates
cac40_market.subscribe(cac40_portfolio)



"""T = 1  # 1 year
N = 252  # Number of trading days in a year
dt = T / N
# Parameters for 3 assets
S0_1, mu_1, sigma_1 = 100, 0.1, 0.2
S0_2, mu_2, sigma_2 = 100, 0.12, 0.25
S0_3, mu_3, sigma_3 = 100, 0.08, 0.15

# Generate price
prices_asset1 = generate_gbm(S0_1, mu_1, sigma_1, T, N)
prices_asset2 = generate_gbm(S0_2, mu_2, sigma_2, T, N)
prices_asset3 = generate_gbm(S0_3, mu_3, sigma_3, T, N)

# Create asset object with the first serie of prices
asset1 = Asset("stock1", prices_asset1)
asset2 = Asset("stock2", prices_asset2)
asset3 = Asset("stock3", prices_asset3)


portfolio1 = Portfolio(assets=[asset1, asset2, asset3], weights=[1/3, 1/3, 1/3], name="test")

mpt_model = MPTModel()

print(portfolio1.weights)
print(portfolio1)

portfolio1.optimize_weights(model=mpt_model)

print(portfolio1.weights)
print(portfolio1)

# Plot asset1 and returns
#fig, axs = plt.subplots(2,1)
#axs[0].plot(asset1.prices)
#axs[1].plot(asset1.returns, color="r", alpha = 0.5)
#plt.show()

# Plot all assets
#fig, axs = plt.subplots(3,1)
#for i, asset in zip(range(3), portfolio1.assets):
#    axs[i].plot(asset.prices)
#plt.show()

# Plot portfolio and returns
#fig, axs = plt.subplots(2,1)
#axs[0].plot(portfolio1.prices)
#axs[1].plot(portfolio1.returns, color="r", alpha = 0.5)
#plt.show()


# Instantiate the data source
data_source = YahooFinance()

tickers = ['AAPL', 'GOOG', 'MSFT', 'NVDA']  
data = data_source.fetch_data(['AAPL', 'GOOG', 'MSFT', 'NVDA'], '2023-10-31', '2024-10-31')

assets = []
for ticker in tickers:
    # Extract the prices for the current ticker
    prices = data[ticker].values  # Convert to numpy array if needed
    
    # Create an Asset object for this ticker
    asset = Asset(symbol=ticker, prices=prices)
    assets.append(asset)

# Step 3: Define weights for each asset
# Here, we'll use equal weights, but you could set these based on your strategy
num_assets = len(assets)
weights = [1 / num_assets] * num_assets  # Equal weights

# Step 4: Initialize the Portfolio with assets and weights
portfolio = Portfolio(assets=assets, weights=weights, name="Tech Portfolio")

# Display the portfolio
mpt_model = MPTModel()
print(portfolio)

portfolio.optimize_weights(model=mpt_model)

print(portfolio.weights)

portfolio.calculate_variance

"""
