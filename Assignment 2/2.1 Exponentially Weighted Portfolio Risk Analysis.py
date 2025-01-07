# Risk Management Assignment 2
# Exponentially Weighted Portfolio Risk Analysis

# Steps:
# 1. Import the daily returns data.
# 2. Extract daily returns for the indices and define portfolio weights.
# 3. Define the exponential decay function.
# 4. Calculate exponentially weighted portfolio returns.
# 5. Calculate Value at Risk (VaR) and Expected Shortfall (ES).
# 6. Export the results.

# Step 1: Import the daily returns data
input_file_path = "/Users/gauthamganesan/Downloads/Daily Returns.xlsx"
data = pd.read_excel(input_file_path, sheet_name="Daily Return")
data = data.dropna()  # Removes rows with missing values

# Step 2: Extract daily returns for the indices and define portfolio weights
djia_returns = data["DJ Industrial Average"]
ftse_returns = data["FTSE 100"]
cac_returns = data["France CAC 40"]

initial_weights = {
    "DJIA": 0.50,
    "FTSE": 0.30,
    "CAC": 0.20
}

# Step 3: Define the exponential decay function
def calculate_exponential_weights(length, lambda_=0.99):
    weights = np.array([lambda_ ** i for i in range(length)])
    return weights / weights.sum()

# Step 4: Calculate exponentially weighted portfolio returns
returns_matrix = np.column_stack((djia_returns, ftse_returns, cac_returns))
portfolio_weights = np.array(list(initial_weights.values()))

num_days = returns_matrix.shape[0]
decaying_weights = calculate_exponential_weights(num_days, lambda_=0.99)
weighted_portfolio_returns = []

for i in range(num_days):
    current_weights = decaying_weights[: i + 1][::-1]
    weighted_returns = np.dot(returns_matrix[: i + 1], portfolio_weights)
    weighted_portfolio_return = np.dot(weighted_returns, current_weights)
    weighted_portfolio_returns.append(weighted_portfolio_return)

weighted_portfolio_returns = np.array(weighted_portfolio_returns)

# Step 5: Calculate Value at Risk (VaR) and Expected Shortfall (ES)
confidence_level = 0.99
sorted_returns = np.sort(weighted_portfolio_returns)
var_index = int((1 - confidence_level) * len(sorted_returns))

VaR = sorted_returns[var_index]
ES = sorted_returns[:var_index].mean()

# Step 6: Export the results
output_file_path = "/Users/gauthamganesan/Downloads/Weighted_VaR_ES.xlsx"

output_data = pd.DataFrame({
    "Date": data["Date"],
    "Weighted Portfolio Returns": weighted_portfolio_returns
})

summary = pd.DataFrame({
    "Metric": ["VaR", "ES"],
    "Value": [VaR, ES]
})

with pd.ExcelWriter(output_file_path, engine="openpyxl") as writer:
    output_data.to_excel(writer, sheet_name="Weighted Returns", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)
