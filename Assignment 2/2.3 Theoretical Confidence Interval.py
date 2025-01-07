# Risk Management Assignment 2
# Theoretical Confidence Interval for Portfolio VaR

# Steps:
# 1. Import the weighted portfolio returns data.
# 2. Calculate necessary statistics for portfolio VaR.
# 3. Calculate the theoretical confidence interval for VaR.
# 4. Export the results.

# Step 1: Import the weighted portfolio returns data
input_file_path = "/Users/gauthamganesan/Downloads/Weighted_VaR_ES.xlsx"
data = pd.read_excel(input_file_path, sheet_name="Weighted Returns")
portfolio_returns = data["Weighted Portfolio Returns"]

# Step 2: Calculate necessary statistics for portfolio VaR
confidence_level = 0.99
z_score = norm.ppf(1 - confidence_level)
mean_return = np.mean(portfolio_returns)
std_dev = np.std(portfolio_returns)

portfolio_var = mean_return + z_score * std_dev

# Step 3: Calculate the theoretical confidence interval for VaR
sample_size = len(portfolio_returns)
std_error = std_dev / np.sqrt(sample_size)

lower_bound = portfolio_var - 1.96 * std_error
upper_bound = portfolio_var + 1.96 * std_error

# Step 4: Export the results
output_file_path = "/Users/gauthamganesan/Downloads/Theoretical_VaR_Confidence_Interval.xlsx"

results = pd.DataFrame({
    "Metric": ["Mean Return", "Standard Deviation", "VaR", "95% CI Lower Bound", "95% CI Upper Bound"],
    "Value": [mean_return, std_dev, portfolio_var, lower_bound, upper_bound]
})

with pd.ExcelWriter(output_file_path, engine="openpyxl") as writer:
    results.to_excel(writer, sheet_name="Theoretical CI", index=False)
