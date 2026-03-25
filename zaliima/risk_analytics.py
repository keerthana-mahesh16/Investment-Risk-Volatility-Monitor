import yfinance as yf
import pandas as pd
import numpy as np
import time

def fetch_data(tickers, period="1y", retries=3):
    """
    Robust fetching of historical Adjusted Close price data.
    """
    for i in range(retries):
        try:
            print(f"Attempt {i+1}: Fetching price data for: {tickers}...")
            data = yf.download(tickers, period=period, progress=False)
            
            # Using 'Adj Close' is critical for Data Quality (handles splits/dividends)
            if isinstance(data.columns, pd.MultiIndex):
                if 'Adj Close' in data.columns.levels[0]:
                    data = data['Adj Close']
                else:
                    data = data['Close']
            else:
                data = data['Adj Close'] if 'Adj Close' in data.columns else data['Close']
            
            if len(tickers) == 1 and isinstance(data, pd.Series):
                data = data.to_frame()
                data.columns = tickers
            
            if data.empty:
                raise ValueError("Downloaded data is empty.")
                
            return data
        except Exception as e:
            print(f"Error fetching data: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    
    raise Exception(f"Failed to fetch data after {retries} attempts.")

def fetch_volume_data(tickers, period="1y", retries=3):
    """
    Robust fetching of historical volume data.
    """
    for i in range(retries):
        try:
            print(f"Attempt {i+1}: Fetching volume data for: {tickers}...")
            data = yf.download(tickers, period=period, progress=False)
            
            if isinstance(data.columns, pd.MultiIndex):
                return data['Volume']
            return data[['Volume']] if 'Volume' in data.columns else data
        except Exception as e:
            print(f"Error fetching volume: {e}. Retrying...")
            time.sleep(5)
    return None

def calculate_log_returns(data):
    """
    Calculates daily Log Returns using efficient NumPy operations.
    Log returns are time-additive and better for financial modeling.
    """
    return np.log(data / data.shift(1)).dropna()

def export_to_csv(data, filename):
    """
    Exports processed data to a CSV for Tableau/PowerBI.
    """
    print(f"Exporting data to {filename} for Tableau...")
    data.to_csv(filename)

def calculate_returns(data):
    """
    Calculates daily percentage returns (Simple Returns).
    """
    return data.pct_change().dropna()

def calculate_rolling_vol(returns, window=30):
    """
    Calculates rolling standard deviation (volatility).
    """
    return returns.rolling(window=window).std() * np.sqrt(252)  # Annulized

def calculate_var(returns, confidence_level=0.95):
    """
    Calculates Value at Risk (VaR) using the historical method.
    """
    return returns.quantile(1 - confidence_level)

if __name__ == "__main__":
    # Quick test
    test_tickers = ["AAPL", "MSFT", "GOOGL"]
    df = fetch_data(test_tickers)
    rets = calculate_returns(df)
    print("Daily Returns (First 5 lines):")
    print(rets.head())
    
    var_95 = calculate_var(rets)
    print("\n95% Value at Risk (VaR):")
    print(var_95)
