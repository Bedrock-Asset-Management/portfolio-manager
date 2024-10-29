```
portfolio-lib/
├── assets/                        # Asset-related classes
│   ├── asset.py                   # Asset class
│   └── __init__.py
├── portfolio/                     # Core portfolio class and management
│   ├── portfolio.py               # Portfolio class with risk and optimization strategies
│   └── __init__.py
├── market_data/                   # Handles data acquisition and preprocessing
│   ├── market_data.py             # MarketData class for fetching and cleaning data
│   └── __init__.py
├── risk_management/               # Risk management strategies (Strategy Pattern)
│   ├── risk_management.py         # RiskManagement interface
│   ├── value_at_risk.py           # ValueAtRisk strategy implementation
│   ├── stress_testing.py          # Other risk strategies can be added here
│   └── __init__.py
├── optimization/                  # Optimization strategies (Strategy Pattern)
│   ├── optimization.py            # Optimization interface
│   ├── mean_variance.py           # MeanVarianceOptimization strategy
│   ├── other_optimizer.py         # Additional optimizers (e.g., heuristic, LP)
│   └── __init__.py
├── tests/                         # Unit tests for all modules
│   ├── test_assets.py
│   ├── test_portfolio.py
│   ├── test_market_data.py
│   ├── test_risk_management/
│   │   ├── test_value_at_risk.py
│   │   └── ...
│   ├── test_optimization/
│   │   ├── test_mean_variance.py```
│   │   └── ...
│   └── ...
├── README.md                      # Project overview and documentation
├── requirements.txt               # Dependencies
└── setup.py                       # Installation script
