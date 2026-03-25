import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_stock_prices(data):
    """
    Plots historical closing prices.
    """
    plt.figure(figsize=(12, 6))
    for column in data.columns:
        plt.plot(data.index, data[column], label=column)
    plt.title("Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_returns_distribution(returns):
    """
    Plots the distribution of daily returns with a KDE.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(returns, kde=True, bins=50)
    plt.title("Daily Returns Probability Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_heatmap(returns):
    """
    Plots a heatmap showing correlation between assets.
    """
    corr = returns.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Asset Correlation Heatmap")
    plt.show()

def plot_monte_carlo(simulation_df):
    """
    Plots the final 100 simulation paths from Monte Carlo.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(simulation_df.iloc[:, :100]) # Plot first 100 paths
    plt.title("Monte Carlo Simulation: Future Portfolio Paths")
    plt.xlabel("Days into Future")
    plt.ylabel("Normalized Portfolio Value")
    plt.grid(True)
    plt.show()

def plot_volume(volume_data):
    """
    Plots trading volume over time.
    """
    plt.figure(figsize=(12, 6))
    for column in volume_data.columns:
        plt.bar(volume_data.index, volume_data[column], label=column, alpha=0.5)
    plt.title("Trading Volume Trends")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.legend()
    plt.show()

def plot_rolling_vol(rolling_vol_data):
    """
    Plots 30-day rolling volatility.
    """
    plt.figure(figsize=(12, 6))
    for column in rolling_vol_data.columns:
        plt.plot(rolling_vol_data.index, rolling_vol_data[column], label=f"{column} (30d Vol)")
    plt.title("30-Day Rolling Volatility (Market Uncertainty)")
    plt.xlabel("Date")
    plt.ylabel("Annualized Volatility")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_simulation_dist(simulation_df):
    """
    Plots the probability distribution of final simulation prices.
    """
    final_prices = simulation_df.iloc[-1]
    plt.figure(figsize=(10, 6))
    sns.histplot(final_prices, kde=True, bins=50, color='purple')
    plt.axvline(final_prices.mean(), color='red', linestyle='--', label=f'Mean: {final_prices.mean():.2f}')
    plt.title("Monte Carlo: Probability Distribution of Future Outcomes")
    plt.xlabel("Final Normalized Portfolio Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
