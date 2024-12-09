# Risk Management Assignment 3 Part 2
# Data Analysis: Variance Covariance Matrix (Historical Method)

# Steps,
# 1. Import the clean data
# 2. Filter the relevant columns and merge the dataframes
# 3. Compute the covariance matrix using historical method

import pandas as pd


# Step 1: Imports the clean data
file_path = "/Users/gauthamganesan/Downloads/Daily Return.xlsx"
data = pd.read_excel(file_path, sheet_name="Daily Return")


# Step 2: Filters the relevant columns and merges the dataframes
djia_returns = data["DJ Industrial Average"]
ftse_returns = data["FTSE 100"]
cac_returns = data["France CAC 40"]
returns_data = pd.concat([djia_returns, ftse_returns, cac_returns], axis=1)
returns_data.columns = ["DJIA", "FTSE 100", "CAC 40"]


# Step 3: Computes the covariance matrix
historical_cov_matrix = returns_data.cov()
output_file = "/Users/gauthamganesan/Downloads/Variance_Covariance_Matrix.xlsx"
historical_cov_matrix.to_excel(output_file)
