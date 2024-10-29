```
portfolio_project/
│
├── main.py                     # Point d'entrée principal du programme
├── data/                       # Données brutes et transformées pour le ML et les tests
│   ├── raw/
│   └── processed/
├── models/                     # Modèles financiers et machine learning
│   ├── __init__.py
│   ├── ml_models/
│   ├── mpt.py                  # Modèle de Modern Portfolio Theory
│   └── capm.py                 # Modèle CAPM
│
├── portfolio/                  # Gestion des portefeuilles et actifs
│   ├── __init__.py
│   ├── asset.py                # Classe pour gérer chaque actif
│   └── portfolio.py            # Classe de gestion de portefeuille
│
├── ml_pipeline/                # Pipelines de traitement des données et de formation des modèles
│   ├── __init__.py
│   ├── preprocessing.py        
│   ├── feature_engineering.py  
│   └── evaluation.py           
│
├── optimization_lib/           # Bibliothèque d’optimisation
│   ├── __init__.py
│   ├── optimizers/
│   └── constraints/
│
├── risk_management/            # Nouveau module pour la gestion des risques et le backtesting
│   ├── __init__.py
│   ├── var.py                  # Méthodes pour calculer la Value at Risk (historique, paramétrique, etc.)
│   ├── expected_shortfall.py   # Calcul de l'Expected Shortfall (moyenne des pertes au-delà de la VaR)
│   ├── backtester.py           # Classe de backtesting pour évaluer les stratégies et portefeuilles
│   └── metrics.py              # Fonctions pour calculer des métriques de risque et de performance
│
└── utils/                      # Fonctions utilitaires (chargement des données, visualisation)
    ├── __init__.py
    ├── data_loader.py          
    └── visualizer.py
```