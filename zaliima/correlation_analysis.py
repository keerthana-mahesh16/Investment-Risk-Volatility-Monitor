import pandas as pd

# load returns data
returns = pd.read_csv("tableau_returns.csv")

# if Date column exists
if "Date" in returns.columns:
    returns = returns.set_index("Date")

# calculate correlation
corr_matrix = returns.corr()

# save for Tableau
corr_matrix.to_csv("correlation_matrix.csv")
print("Correlation matrix saved to correlation_matrix.csv")
