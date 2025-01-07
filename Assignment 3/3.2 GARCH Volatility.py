# Risk Management Assignment 3
# GARCH Volatility Calculation

# Steps:
# 1. Import the index values data.
# 2. Calculate percentage returns for each index.
# 3. Compute GARCH volatilities for each index.
# 4. Export the results.

# Step 1: Import the index values data
input_file_path = "/Users/gauthamganesan/Downloads/RM Assignment 3 Part 1/3.1 EWMA Volatility and Garch Volatility.xlsx"
index_data = pd.read_excel(input_file_path, sheet_name="Total Return Index")

# Step 2: Calculate percentage returns for each index
index_data["DJIA Returns"] = index_data["DJ Industrial Average"].pct_change()
index_data["FTSE Returns"] = index_data["FTSE 100"].pct_change()
index_data["CAC Returns"] = index_data["France CAC 40"].pct_change()

returns_data = index_data[["DJIA Returns", "FTSE Returns", "CAC Returns"]].dropna()

# Step 3: Compute GARCH volatilities for each index
garch_params = {
    "DJIA": {"omega": 0.0776, "alpha": 0.2099, "beta": 0.7526},
    "FTSE 100": {"omega": 0.0843, "alpha": 0.1608, "beta": 0.7816},
    "France CAC 40": {"omega": 0.1206, "alpha": 0.1774, "beta": 0.7705},
}

def calculate_garch_volatility(return_series, omega, alpha, beta):
    n = len(return_series)
    variances = np.zeros(n)
    variances[0] = omega / (1 - alpha - beta)  # Unconditional variance
    for t in range(1, n):
        variances[t] = omega + alpha * (return_series[t - 1] ** 2) + beta * variances[t - 1]
    return np.sqrt(variances)

garch_volatilities = {
    "GARCH Volatility DJIA": calculate_garch_volatility(
        returns_data["DJIA Returns"].values, garch_params["DJIA"]["omega"], garch_params["DJIA"]["alpha"], garch_params["DJIA"]["beta"]
    ),
    "GARCH Volatility FTSE 100": calculate_garch_volatility(
        returns_data["FTSE Returns"].values, garch_params["FTSE 100"]["omega"], garch_params["FTSE 100"]["alpha"], garch_params["FTSE 100"]["beta"]
    ),
    "GARCH Volatility CAC 40": calculate_garch_volatility(
        returns_data["CAC Returns"].values, garch_params["France CAC 40"]["omega"], garch_params["France CAC 40"]["alpha"], garch_params["France CAC 40"]["beta"]
    ),
}

# Step 4: Export the results
output_file_path = "/Users/gauthamganesan/Downloads/RM Assignment 3 Part 1/GARCH_Volatilities_Corrected.xlsx"
garch_volatility_df = pd.DataFrame(garch_volatilities)
garch_volatility_df.to_excel(output_file_path, index=False)
