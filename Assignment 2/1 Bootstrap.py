# Risk Management Assignment 2
# Data Analysis: Bootstrap

# Steps,
# 1. Import the clean data
# 2. Perform bootstrap resampling using NumPy
# 3. Calculate the confidence intervals
# 4. Export the result



import pandas as pd
import numpy as np
from openpyxl import Workbook


# Step 1: Import the clean data
file_path = "/Users/gauthamganesan/Downloads/Bootstrap resampling.xlsx"
data = pd.read_excel(file_path, sheet_name="Bootstrap")

portfolio_returns = data["Portfolio Return"]


# Step 2: Performs bootstrap resampling
n_iterations = 1000
bootstrap_vars = []

for _ in range(n_iterations):
    resampled_returns = np.random.choice(portfolio_returns, size=len(portfolio_returns), replace=True)
    var = np.percentile(resampled_returns, 1)                                                               # 1st percentile for 99% VaR
    bootstrap_vars.append(var)


# Step 3: Calculates the confidence intervals
bootstrap_vars = np.array(bootstrap_vars)

lower_bound = np.percentile(bootstrap_vars, 2.5)                                                            # 2.5th percentile
upper_bound = np.percentile(bootstrap_vars, 97.5)                                                           # 97.5th percentile


# Step 4: Exports the result
output_file = "/Users/gauthamganesan/Downloads/Bootstrap_Results.xlsx"
wb = Workbook()
ws = wb.active
ws.title = "Bootstrap Results"

ws.append(["Bootstrap Iterations", n_iterations])
ws.append(["95% Confidence Interval Lower Bound", lower_bound])
ws.append(["95% Confidence Interval Upper Bound", upper_bound])
ws.append([])
ws.append(["Bootstrap VaR Values"])

for var in bootstrap_vars:
    ws.append([var])

wb.save(output_file)
