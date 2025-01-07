# Risk Management Assignment 3 Part 2
# Data Analysis: Variance-Covariance Matrix using EWMA
# Data Analysis: Monte Carlo Simulation for Portfolio VaR

# Steps,
# 1. Import the clean data
# 2. Calculate the EWMA-based variance for each index
# 3. Calculate the EWMA-based covariance for each pair of indices
# 4. Compute the EWMA-based variance-covariance matrix
# 5. Calculate portfolio weights, variance, and 99% 1-Day VaR using EWMA-based matrix
# 6. Perform Monte Carlo Simulation to calculate Portfolio VaR
# 7. Export the result
# 8. Plot histogram of Monte Carlo simulated portfolio returns


import pandas as pd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt


# Step 1: Imports the clean data
file_path = "/Users/gauthamganesan/Downloads/Daily Return.xlsx"
data = pd.read_excel(file_path, sheet_name="Daily Return")

djia_returns = data["DJ Industrial Average"].dropna()
ftse_returns = data["FTSE 100"].dropna()
cac_returns = data["France CAC 40"].dropna()

returns_data = pd.concat([djia_returns, ftse_returns, cac_returns], axis=1)
returns_data.columns = ["DJIA", "FTSE 100", "CAC 40"]


# Step 2: Calculate the EWMA-based variance for each index
lambda_value = 0.94                                                                                 # Define the lambda (decay factor)

def calculate_ewma_variance(series, lambda_value):                                                  # Function to calculate EWMA variance
    ewma_variance = [series.var()]
    for return_t in series[1:]:
        new_variance = lambda_value * ewma_variance[-1] + (1 - lambda_value) * return_t ** 2
        ewma_variance.append(new_variance)
    return np.array(ewma_variance)

djia_ewma_variance = calculate_ewma_variance(djia_returns, lambda_value)                            # Calculate EWMA variance for each index
ftse_ewma_variance = calculate_ewma_variance(ftse_returns, lambda_value)
cac_ewma_variance = calculate_ewma_variance(cac_returns, lambda_value)


# Step 3: Calculate the EWMA-based covariance for each pair of indices
def calculate_ewma_covariance(series1, series2, lambda_value):
    ewma_covariance = [np.cov(series1, series2)[0][1]]                                              # Initialize with sample covariance
    for r1, r2 in zip(series1[1:], series2[1:]):
        new_covariance = lambda_value * ewma_covariance[-1] + (1 - lambda_value) * r1 * r2
        ewma_covariance.append(new_covariance)
    return np.array(ewma_covariance)

djia_ftse_covariance = calculate_ewma_covariance(djia_returns, ftse_returns, lambda_value)          # Calculate EWMA covariance for each pair
djia_cac_covariance = calculate_ewma_covariance(djia_returns, cac_returns, lambda_value)
ftse_cac_covariance = calculate_ewma_covariance(ftse_returns, cac_returns, lambda_value)


# Step 4: Construct the EWMA-based variance-covariance matrix
ewma_cov_matrix = pd.DataFrame({
    "DJIA": [djia_ewma_variance[-1], djia_ftse_covariance[-1], djia_cac_covariance[-1]],
    "FTSE 100": [djia_ftse_covariance[-1], ftse_ewma_variance[-1], ftse_cac_covariance[-1]],
    "CAC 40": [djia_cac_covariance[-1], ftse_cac_covariance[-1], cac_ewma_variance[-1]]
}, index=["DJIA", "FTSE 100", "CAC 40"])


# Step 5: Calculates portfolio metrics using EWMA-based matrix
weights = np.array([0.4, 0.3, 0.3])                                                                 # Define portfolio weights

portfolio_variance = np.dot(weights.T, np.dot(ewma_cov_matrix.values, weights))                     # Portfolio variance and standard deviation
portfolio_std_dev = np.sqrt(portfolio_variance)

z_score = 2.33                                                                                      # For 99% confidence level
portfolio_var = z_score * portfolio_std_dev


# Step 6: Performs Monte Carlo Simulation for Portfolio VaR
n_simulations = 100000                                                                              # Simulate portfolio returns
simulated_returns = np.random.multivariate_normal(
    mean=returns_data.mean(),
    cov=ewma_cov_matrix.values,
    size=n_simulations
)

simulated_portfolio_returns = np.dot(simulated_returns, weights)                                    # Calculate portfolio returns
monte_carlo_var = -np.percentile(simulated_portfolio_returns, 1)                                    # Calculate 99% 1-Day VaR from simulations


# Step 7: Exports the result
output_file = "/Users/gauthamganesan/Downloads/EWMA_MC_Results.xlsx"
wb = Workbook()
ws = wb.active
ws.title = "EWMA and MC Results"

ws.append(["", "DJIA", "FTSE 100", "CAC 40"])
for idx, row in ewma_cov_matrix.iterrows():
    ws.append([idx] + row.tolist())

ws.append([])
ws.append(["Portfolio Metrics"])
ws.append(["Portfolio Variance", portfolio_variance])
ws.append(["Portfolio Standard Deviation", portfolio_std_dev])
ws.append(["Portfolio VaR (99%)", portfolio_var])
ws.append(["Monte Carlo VaR (99%)", monte_carlo_var])

wb.save(output_file)


# Step 8: Plot histogram of Monte Carlo simulated portfolio returns
plt.figure(figsize=(10, 6))
plt.hist(simulated_portfolio_returns, bins=50, color="skyblue", edgecolor="black")
plt.title("Monte Carlo Simulated Portfolio Returns")
plt.xlabel("Portfolio Return")
plt.ylabel("Frequency")
plt.grid()
plt.show()
