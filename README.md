**Project Description**:
This project is aimed at implementing a simple prototype of a Mean-Variance Portfolio Theory (MPT) model for optimizing a financial portfolio, with future compatibility to integrate other models such as machine learning-based asset prediction and advanced optimization approaches. The project will allow for the generation of multiple portfolios for different sectors, thus providing the ability to assess and compare multiple strategies over time.

Key features:
- **Investment Universe**: Ability to select a set of symbols/assets for investment.
- **Portfolio Optimization**: Implement an MPT-based optimization to maximize returns while minimizing risk (using variance as a measure).
- **Risk Assessment**: Integration of risk constraints such as volatility and maximum allowable loss.
- **Portfolio Evaluation**: Create multiple portfolios, possibly grouped by sectors, to assess the performance of different models and optimization approaches.
- **Trading Mechanism**: Initially, assets will be considered "held" indefinitely, but modularity will be ensured to integrate trading rules later (manual or algorithmic). Future plans may include automatic trading decision-making.
- **Web Interface**: A basic visualization tool to monitor portfolio performance in real time, including current return on investment (ROI).
- **Metrics Calculation**: Differentiation between returns used in model training (e.g., `calculate_logarithmic_returns()`) and returns used in portfolio performance.

**Core Design Considerations**:
- **Modularity**: The design should be modular to facilitate integration of more advanced models without a significant overhaul.
- **Flexibility**: The ability to define different risk metrics and optimization goals.

**UML Class Diagram Description**:

1. **Class: Asset**
    - **Attributes**:
        - `symbol: str` 
        - `historical_prices: pd.DataFrame  # DataFrame with 'date' and 'price' columns`
    - **Methods**:
        - `fetch_current_price() -> float`: Fetches the latest price from a data source.
        - `calculate_logarithmic_returns(start_date: datetime, end_date: datetime) -> pd.Series`: Computes logarithmic returns for use in portfolio optimization, filtered by a specific date range.

2. **Class: Portfolio**
    - **Attributes**:
        - `assets: List[Asset]`
        - `weights: List[float]`
        - `sector: str` (for categorizing portfolios by sector)
        - `transaction_history: List[Transaction]` (to keep track of portfolio transactions)
        - `balance_history: pd.DataFrame  # DataFrame with 'date' and 'net_worth' columns for tracking portfolio value over time`
    - **Methods**:
        - `net_worth(currency: str = 'USD') -> float`: Calculates the net worth of the portfolio in a given currency.
        - `optimize_weights(model: OptimizationModel) -> None`: Optimizes asset weights based on the selected model.
        - `calculate_return(start_date: datetime, end_date: datetime) -> float`: Calculates the return of the portfolio over a specific date range.
        - `calculate_risk(start_date: datetime, end_date: datetime) -> float`: Calculates the portfolio risk, typically using variance, for a given time frame.
        - `track_value_over_time() -> None`: Updates the `balance_history` DataFrame to reflect changes in the portfolio's net worth.

3. **Class: Transaction**
    - **Attributes**:
        - `asset_symbol: str`
        - `date: datetime`
        - `transaction_type: str` (buy/sell)
        - `quantity: float`
        - `price: float`

4. **Class: OptimizationModel (Abstract)**
    - **Methods**:
        - `optimize(assets: List[Asset], risk_tolerance: float) -> List[float]`: Abstract method for optimizing the portfolio.

5. **Class: MPTModel (Inherits OptimizationModel)**
    - **Methods**:
        - `optimize(assets: List[Asset], risk_tolerance: float) -> List[float]`: Implements mean-variance optimization.

6. **Class: RiskManager**
    - **Attributes**:
        - `risk_tolerance: float`
    - **Methods**:
        - `calculate_value_at_risk(portfolio: Portfolio, start_date: datetime, end_date: datetime) -> float`: Calculates the VaR for a given portfolio over a specified date range.
        - `apply_risk_constraints(portfolio: Portfolio) -> None`: Adjusts weights if necessary to adhere to risk limits.

7. **Class: PortfolioEvaluator**
    - **Methods**:
        - `evaluate(portfolios: List[Portfolio], start_date: datetime, end_date: datetime) -> Dict`: Evaluates a list of portfolios and returns performance metrics over a specific time frame.

8. **Class: WebInterface**
    - **Attributes**:
        - `portfolios: List[Portfolio]`
    - **Methods**:
        - `render_dashboard(start_date: datetime = None, end_date: datetime = None) -> None`: Displays key metrics, current returns, and risk assessments for each portfolio over a selected time range.

**Workflow Overview**:
- **Asset Selection**: Create instances of `Asset` for each symbol in the investment universe.
- **Portfolio Creation**: Instantiate `Portfolio` objects with selected `Asset` instances, categorized by sector or other attributes.
- **Weight Optimization**: Use `MPTModel` to determine optimal asset weights while considering risk, and set these in the `Portfolio` instances.
- **Risk Management**: Use `RiskManager` to apply any risk constraints.
- **Evaluation**: Evaluate the performance using `PortfolioEvaluator`, including metrics like current ROI and historical returns.
- **Web Visualization**: Use `WebInterface` to visualize portfolio performance, tracking metrics over time.

**Class Diagram (Pseudocode UML)**:
```
+--------------------+
|      Asset         |
+--------------------+
| - symbol: str      |
| - historical_prices: pd.DataFrame  # DataFrame with 'date' and 'price' columns |
+--------------------+
| + fetch_current_price() -> float |
| + calculate_logarithmic_returns(start_date: datetime, end_date: datetime) -> pd.Series |
+--------------------+

+-----------------------+
|      Portfolio        |
+-----------------------+
| - assets: List[Asset] |
| - weights: List[float]|
| - sector: str         |
| - transaction_history: List[Transaction] |
| - balance_history: pd.DataFrame  # DataFrame with 'date' and 'net_worth' columns |
+-----------------------+
| + net_worth(currency: str = 'USD') -> float               |
| + optimize_weights(model: OptimizationModel) -> None      |
| + calculate_return(start_date: datetime, end_date: datetime) -> float |
| + calculate_risk(start_date: datetime, end_date: datetime) -> float |
| + track_value_over_time() -> None                         |
+-----------------------+

+-----------------------+
|     Transaction       |
+-----------------------+
| - asset_symbol: str   |
| - date: datetime      |
| - transaction_type: str |
| - quantity: float     |
| - price: float        |
+-----------------------+

+-----------------------+
|  OptimizationModel    |  <Abstract Class>
+-----------------------+
| + optimize(assets: List[Asset], risk_tolerance: float) -> List[float] |
+-----------------------+

+-----------------------+
|      MPTModel         | <inherits OptimizationModel>
+-----------------------+
| + optimize(assets: List[Asset], risk_tolerance: float) -> List[float] |
+-----------------------+

+-----------------------+
|      RiskManager      |
+-----------------------+
| - risk_tolerance: float   |
+-----------------------+
| + calculate_value_at_risk(portfolio: Portfolio, start_date: datetime, end_date: datetime) -> float |
| + apply_risk_constraints(portfolio: Portfolio) -> None    |
+-----------------------+

+-----------------------+
|  PortfolioEvaluator   |
+-----------------------+
| + evaluate(portfolios: List[Portfolio], start_date: datetime, end_date: datetime) -> Dict |
+-----------------------+

+-----------------------+
|    WebInterface       |
+-----------------------+
| - portfolios: List[Portfolio] |
+-----------------------+
| + render_dashboard(start_date: datetime = None, end_date: datetime = None) -> None     |
+-----------------------+
```

This structure gives you a starting point for your MPT model while keeping it flexible for later additions. Different models can be easily integrated by subclassing `OptimizationModel`. Similarly, trading rules can be added by extending `Portfolio` with new methods or creating a `TradingStrategy` class to define the rules. The differentiation between returns for model training (`calculate_logarithmic_returns`) and for monitoring (`calculate_portfolio_return()`) is handled clearly within the `Asset` and `Portfolio` classes.

**Extensive Example Usage**:

1. **Step 1: Asset Selection**
    ```python
    # Create assets with historical prices
    historical_data_1 = pd.DataFrame({'date': pd.to_datetime(['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04']), 'price': [145.0, 147.0, 149.0, 150.0]})
    asset_1 = Asset(symbol='AAPL', historical_prices=historical_data_1)
    historical_data_2 = pd.DataFrame({'date': pd.to_datetime(['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04']), 'price': [2700.0, 2750.0, 2780.0, 2800.0]})
    asset_2 = Asset(symbol='GOOG', historical_prices=historical_data_2)
    historical_data_3 = pd.DataFrame({'date': pd.to_datetime(['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04']), 'price': [3300.0, 3350.0, 3380.0, 3400.0]})
    asset_3 = Asset(symbol='AMZN', historical_prices=historical_data_3)
    
    assets = [asset_1, asset_2, asset_3]
    ```

2. **Step 2: Portfolio Creation**
    ```python
    # Create a portfolio with selected assets
    portfolio = Portfolio(assets=assets, weights=[0.3, 0.4, 0.3], sector='Technology')
    ```

3. **Step 3: Weight Optimization**
    ```python
    # Use MPTModel to optimize weights for the portfolio
    mpt_model = MPTModel()
    portfolio.optimize_weights(model=mpt_model)
    
    # After optimization, weights are updated in the portfolio
    print(f'Optimized Weights: {portfolio.weights}')
    ```

4. **Step 4: Risk Management**
    ```python
    # Apply risk management constraints
    risk_manager = RiskManager(risk_tolerance=0.05)
    risk_manager.apply_risk_constraints(portfolio)
    
    # Check adjusted weights after applying risk constraints
    print(f'Weights after Risk Constraints: {portfolio.weights}')
    ```

5. **Step 5: Portfolio Evaluation**
    ```python
    # Evaluate the portfolio performance
    evaluator = PortfolioEvaluator()
    performance_metrics = evaluator.evaluate([portfolio], start_date=pd.to_datetime('2024-10-01'), end_date=pd.to_datetime('2024-10-04'))
    
    # Display performance metrics
    print(f'Performance Metrics: {performance_metrics}')
    ```

6. **Step 6: Web Visualization**
    ```python
    # Render portfolio performance via a web interface
    web_interface = WebInterface(portfolios=[portfolio])
    web_interface.render_dashboard(start_date=pd.to_datetime('2024-10-01'), end_date=pd.to_datetime('2024-10-04'))
    ```

**Example Output**:
- **Optimized Weights**: `[0.25, 0.5, 0.25]` (weights updated to balance risk and return)
- **Weights after Risk Constraints**: `[0.2, 0.6, 0.2]` (adjusted to adhere to risk tolerance)
- **Performance Metrics**: `{ 'portfolio_return': 0.12, 'portfolio_risk': 0.08, 'sharpe_ratio': 1.5 }`

This example demonstrates how the system components work together, from asset selection and weight optimization to risk management and performance evaluation. The workflow ensures that portfolios are optimized while adhering to risk constraints and are continuously monitored, with a web interface providing real-time performance visualization.
