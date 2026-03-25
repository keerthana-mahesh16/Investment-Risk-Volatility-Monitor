import risk_analytics as risk
import simulations as sim
import visualizer as vis
import pandas as pd
import numpy as np

def apply_sector_shocks(returns, shocks):
    """
    Applies 'What-If' shocks to specific sectors.
    Shocks is a dict: { 'SectorName': [Tickers], 'ShockValue': -0.10 }
    """
    shocked_returns = returns.copy()
    for sector, info in shocks.items():
        tickers = info['tickers']
        shock = info['shock']
        print(f"Applying 'What-If' shock: {sector} drop of {shock*100}%")
        # Apply logic: Last return is dropped by the shock value
        # or we simulate the shock as a mean shift for the simulation
        for t in tickers:
            if t in shocked_returns.columns:
                shocked_returns[t] = shocked_returns[t] + shock # Shift returns
    return shocked_returns

def main():
    print("=== Investment Risk & Volatility Monitor ===")
    
    # Configuration: 10 Diverse Stocks + ^GSPC (S&P 500)
    tickers = [
        "AAPL", "MSFT",  # Tech
        "JPM", "V",       # Finance
        "JNJ", "UNH",     # Healthcare
        "AMZN", "KO",      # Consumer
        "XOM", "CAT",      # Energy/Industrial
        "^GSPC"            # S&P 500 Index
    ]
    period = "1y"
    
    # 1. Fetch Data
    price_data = risk.fetch_data(tickers, period=period)
    
    # 2. Daily Returns (Log Returns are preferred for mathematical modeling)
    print("\nCalculating Log Returns using NumPy...")
    returns = risk.calculate_log_returns(price_data)
    
    # --- NEW: Tableau Connection (Moved to Top for Instant Access) ---
    # Create a combined cleaned dataset for Tableau
    risk.export_to_csv(price_data, "tableau_prices.csv")
    risk.export_to_csv(returns, "tableau_returns.csv")

    # 3. Basic Visuals
    print("Generating Price Trends...")
    vis.plot_stock_prices(price_data)
    
    # NEW: Volume Analysis
    print("Generating Volume Trends...")
    vol_data = risk.fetch_volume_data(tickers, period=period)
    vis.plot_volume(vol_data)

    # NEW: Rolling Volatility
    print("Generating Rolling Volatility...")
    rolling_vol = risk.calculate_rolling_vol(returns)
    vis.plot_rolling_vol(rolling_vol)
    
    print("\nGenerating Correlation Heatmap...")
    vis.plot_correlation_heatmap(returns)

    # --- NEW: What-If Scenario ---
    print("\n--- ENTERING WHAT-IF SCENARIO ---")
    # Define Tech Sector
    tech_tickers = ["AAPL", "MSFT"]
    
    # Simulate a 10% drop in Tech
    shocks = {
        'Technology': {'tickers': tech_tickers, 'shock': -0.10}
    }
    
    shocked_returns = apply_sector_shocks(returns, shocks)
    
    # 4. Advanced Analytics - Value at Risk (VaR)
    var_95 = risk.calculate_var(shocked_returns)
    print("\n95% Value at Risk (VaR) AFTER TECH SHOCK:")
    print(var_95)
    
    # 5. Advanced Analytics - Portfolio Simulation
    # For simulation, we'll use an equally weighted portfolio return
    portfolio_returns = shocked_returns.mean(axis=1)
    
    print("\nRunning Vectorized Monte Carlo Simulation (10,000 runs) WITH SHOCK...")
    sim_df = sim.run_monte_carlo(portfolio_returns)
    
    # Statistical Validation
    print("\nPerforming Statistical Validation (Skewness & Kurtosis)...")
    stats_val = sim.validate_simulation(sim_df, portfolio_returns)
    print(f"Historical Skew: {stats_val['hist_skew']:.4f} | Simulated Skew: {stats_val['sim_skew']:.4f}")
    print(f"Historical Kurtosis: {stats_val['hist_kurt']:.4f} | Simulated Kurtosis: {stats_val['sim_kurt']:.4f}")

    print("Generating Simulation Plot (What-If Scenario)...")
    vis.plot_monte_carlo(sim_df)
    
    # NEW: Probability Distribution
    print("Generating Simulation Probability Distribution...")
    vis.plot_simulation_dist(sim_df)
    
    summary = sim.get_simulation_summary(sim_df)
    print("\nSimulation Results (Normalized to 1.0):")
    print(f"Mean Outcome: {summary['mean']:.2f}")
    print(f"95% Confidence Upper: {summary['95th_percentile']:.2f}")
    print(f"5% Confidence Lower: {summary['5th_percentile']:.2f}")
    
    print("\nMonitor Complete.")

if __name__ == "__main__":
    main()
