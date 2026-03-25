
Investment Risk & Volatility Monitor

 Project Overview

The Investment Risk & Volatility Monitor is a data analytics project designed to analyze stock market data and evaluate portfolio performance. It helps in understanding returns, risk (volatility), and relationships between stocks using interactive visualizations.

This project combines Python for data processing and Tableau for visualization to create a professional financial dashboard.


 Objectives

* Analyze stock price movements over time
* Calculate and visualize returns and volatility
* Understand relationships between stocks using correlation analysis
* Build an interactive Tableau dashboard
* Perform basic risk analysis and scenario evaluation


Tools & Technologies Used

Python(Pandas, NumPy, yfinance)
Tableau(Data Visualization & Dashboard)
CSV Files (Data Storage)

 Dataset

The project uses stock market data fetched using Python.

Generated files:

* `tableau_prices.csv` → Stock prices
* `tableau_returns.csv` → Daily returns
* `correlation_matrix.csv` → Correlation values

---
 Project Workflow

1. Data Collection

Fetch stock data using `yfinance`

2. Data Processing

   * Clean and preprocess data using Pandas
   * Calculate log returns

3. Feature Engineering

   Compute:

      Returns
      Volatility (Standard Deviation)
      Correlation Matrix

4. Data Storage

    Export processed data into CSV files

5. Visualization (Tableau)

Import CSV files
Create charts and dashboard

---

 Dashboard Components

 Stock Price Trend

Shows how stock prices change over time.

 Returns Trend

Displays daily profit/loss of stocks.

 Volatility Chart

Shows the risk level of stocks using standard deviation.

 Correlation Heatmap

Visualizes relationships between different stocks.

 Histogram (Return Distribution)

Shows the frequency distribution of returns.

 KPIs

* Average Return
* Maximum Return
* Minimum Return
* Volatility

---

 Key Concepts Used

* **Returns** → Profit or loss percentage
* **Volatility** → Risk measurement
* **Correlation** → Relationship between stocks
* **Diversification** → Risk reduction strategy
* **Monte Carlo Simulation** (optional advanced feature)

---

 Insights

* High volatility indicates higher investment risk
* Correlation helps in building diversified portfolios
* Return trends show performance over time
* Distribution helps understand risk probability

---

 How to Run the Project

1. Run Python script to generate CSV files
2. Open Tableau
3. Connect:

   * `tableau_prices.csv`
   * `tableau_returns.csv`
4. Create charts and build dashboard

---

 Conclusion

This project demonstrates how data analytics can be used in finance to monitor investment risk and performance. It provides insights that help in **better decision-making and portfolio management**.

---
 Future Improvements

* Add real-time data updates
* Implement advanced risk metrics (VaR, Sharpe Ratio)
* Enhance dashboard interactivity with parameters

---

 Author

* Keerthana MM

---

## 📄 License

This project is for educational purposes.

---
