import numpy as np
import pandas as pd

from scipy.stats import skew, kurtosis

def run_monte_carlo(returns, num_simulations=10000, forecast_days=252):
    """
    Highly efficient Vectorized Monte Carlo simulation using NumPy.
    Predicts future portfolio price paths.
    """
    # Calculate daily mean and volatility from historical data
    mean_return = returns.mean()
    volatility = returns.std()
    
    # Generate all random daily returns at once (Vectorization)
    daily_yields = np.random.normal(mean_return, volatility, (num_simulations, forecast_days))
    
    # Create price paths: Price(t) = Price(0) * exp(cumulative sum of log returns)
    # We use log-normal assumption for price evolution
    price_paths = np.zeros((num_simulations, forecast_days + 1))
    price_paths[:, 0] = 1.0 # Starting normalized price
    
    # Efficiently calculate all paths using cumulative product
    price_paths[:, 1:] = np.cumprod(1 + daily_yields, axis=1)
    
    # Transpose to return (Days x Simulations) for consistency with previous logic
    return pd.DataFrame(price_paths.T)

def validate_simulation(simulation_df, historical_returns):
    """
    Statistical Validation: Compares simulation skewness/kurtosis against historical data.
    """
    simulated_final_returns = simulation_df.iloc[-1] / simulation_df.iloc[0] - 1
    
    validation = {
        "hist_skew": skew(historical_returns),
        "sim_skew": skew(simulated_final_returns),
        "hist_kurt": kurtosis(historical_returns),
        "sim_kurt": kurtosis(simulated_final_returns)
    }
    return validation

def get_simulation_summary(simulation_df):
    """
    Extracts summary statistics from simulation results.
    """
    last_prices = simulation_df.iloc[-1]
    results = {
        "mean": last_prices.mean(),
        "median": last_prices.median(),
        "5th_percentile": last_prices.quantile(0.05),
        "95th_percentile": last_prices.quantile(0.95)
    }
    return results
