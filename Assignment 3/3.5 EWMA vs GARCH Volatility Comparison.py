# Risk Management Assignment 3
# EWMA vs GARCH Volatility Comparison

# Steps:
# 1. Import the EWMA volatilities and corrected GARCH volatilities.
# 2. Align data lengths for comparison.
# 3. Plot EWMA vs. GARCH volatilities.

# Step 1: Import the EWMA volatilities and corrected GARCH volatilities
input_file_path = "/Users/gauthamganesan/Downloads/RM Assignment 3 Part 1/3.1 EWMA Volatility and Garch Volatility.xlsx"
garch_file_path = "/Users/gauthamganesan/Downloads/RM Assignment 3 Part 1/GARCH_Volatilities_Corrected.xlsx"

ewma_data = pd.read_excel(input_file_path, sheet_name="EWMA Variance and Volatility")
garch_data = pd.read_excel(garch_file_path)

# Step 2: Align data lengths for comparison
ewma_data = ewma_data.iloc[1:].reset_index(drop=True)  # Remove the first row to match GARCH data length
time_points = range(len(ewma_data))  # Generate time points for x-axis

ewma_volatilities = {
    "DJIA": ewma_data["EWMA Volatility DJIA"],
    "FTSE 100": ewma_data["EWMA Volatility FTSE 100"],
    "CAC 40": ewma_data["EWMA Volatility CAC 40"],
}

garch_volatilities = {
    "DJIA": garch_data["GARCH Volatility DJIA"],
    "FTSE 100": garch_data["GARCH Volatility FTSE 100"],
    "CAC 40": garch_data["GARCH Volatility CAC 40"],
}

# Step 3: Plot EWMA vs. GARCH volatilities
for index in ewma_volatilities.keys():
    plt.figure(figsize=(10, 6))
    zoom_start = 100  # Focus on data after the first 100 days
    plt.plot(time_points[zoom_start:], ewma_volatilities[index][zoom_start:], label="EWMA Volatility", linestyle='--')
    plt.plot(time_points[zoom_start:], garch_volatilities[index][zoom_start:], label="GARCH Volatility", linestyle='-')
    plt.title(f"{index} Volatility Comparison (EWMA vs. GARCH) - Zoomed In")
    plt.xlabel("Time (Post Day 100)")
    plt.ylabel("Volatility")
    plt.legend()
    plt.grid()
    plt.show()
