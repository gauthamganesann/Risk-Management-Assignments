# Risk Management Assignment 2
# Bootstrap Analysis for Portfolio VaR

# Steps:
# 1. Import the weighted portfolio returns data.
# 2. Define bootstrap parameters.
# 3. Perform bootstrap sampling to calculate VaR estimates.
# 4. Calculate the confidence interval for bootstrap VaR.
# 5. Plot the bootstrap distribution.
# 6. Export the results.

# Step 1: Import the weighted portfolio returns data
input_file_path = "/Users/gauthamganesan/Downloads/Weighted_VaR_ES.xlsx"
data = pd.read_excel(input_file_path, sheet_name="Weighted Returns")
portfolio_returns = data["Weighted Portfolio Returns"]

# Step 2: Define bootstrap parameters
num_bootstrap_samples = 1000
confidence_level = 0.99
bootstrap_var_values = []

# Step 3: Perform bootstrap sampling to calculate VaR estimates
for _ in range(num_bootstrap_samples):
    bootstrap_sample = np.random.choice(portfolio_returns, size=len(portfolio_returns), replace=True)  # Sample with replacement
    sorted_sample = np.sort(bootstrap_sample)  # Sort the sample
    var_index = int((1 - confidence_level) * len(sorted_sample))  # Index for VaR calculation
    bootstrap_var = sorted_sample[var_index]  # Calculate VaR for the given confidence level
    bootstrap_var_values.append(bootstrap_var)

# Step 4: Calculate the confidence interval for bootstrap VaR
lower_bound = np.percentile(bootstrap_var_values, 2.5)  # 2.5th percentile for 95% CI lower bound
upper_bound = np.percentile(bootstrap_var_values, 97.5)  # 97.5th percentile for 95% CI upper bound

# Step 5: Plot the bootstrap distribution
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_var_values, bins=30, alpha=0.7, color='blue', edgecolor='black')  # Histogram of bootstrap VaR values
plt.title("Bootstrap Distribution of Portfolio VaR", fontsize=14)
plt.xlabel("VaR", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.axvline(lower_bound, color='red', linestyle='--', label=f"95% CI Lower Bound: {lower_bound:.4f}")  # Lower bound
plt.axvline(upper_bound, color='green', linestyle='--', label=f"95% CI Upper Bound: {upper_bound:.4f}")  # Upper bound
plt.legend()
plt.grid(True)
plt.savefig("/Users/gauthamganesan/Downloads/Bootstrap_Distribution.png")  # Save the plot as an image
plt.show()

# Step 6: Export the results
output_file_path = "/Users/gauthamganesan/Downloads/Bootstrap_VaR_Analysis.xlsx"

bootstrap_results = pd.DataFrame({
    "Bootstrap VaR Values": bootstrap_var_values  # Bootstrap VaR values
})

summary = pd.DataFrame({
    "Metric": ["Lower Bound", "Upper Bound"],  # Confidence interval metrics
    "Value": [lower_bound, upper_bound]       # Corresponding values
})

with pd.ExcelWriter(output_file_path, engine="openpyxl") as writer:
    bootstrap_results.to_excel(writer, sheet_name="Bootstrap VaR", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)
