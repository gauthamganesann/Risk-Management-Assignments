# Risk Management Assignment 3 Part 1
# Data Analysis: Garch Model

# Steps,
# 1. Import the clean data
# 2. Rescale the return data (to make it compatible with pandas calculations)
# 3. GARCH (1,1) for DJIA
# 4. GARCH (1,1) for FTSE 100
# 5. GARCH (1,1) for CAC 40
# 6. Export the result



import pandas as pd
from arch import arch_model
from openpyxl import Workbook


# Step 1: Imports the clean data
file_path = "/Users/gauthamganesan/Downloads/Daily Return.xlsx"
data = pd.read_excel(file_path, sheet_name="Daily Return")

djia_returns = data["DJ Industrial Average"].dropna()
ftse_returns = data["FTSE 100"].dropna()
cac_returns = data["France CAC 40"].dropna()


# Step 2: Rescales the return data
djia_returns_scaled = djia_returns * 100
ftse_returns_scaled = ftse_returns * 100
cac_returns_scaled = cac_returns * 100


# Step 3: GARCH (1,1) for DJIA
djia_model = arch_model(djia_returns_scaled, vol="Garch", p=1, q=1)
djia_results = djia_model.fit(disp="off")
djia_omega = djia_results.params['omega']
djia_alpha = djia_results.params['alpha[1]']
djia_beta = djia_results.params['beta[1]']


# Step 4: GARCH (1,1) for FTSE 100
ftse_model = arch_model(ftse_returns_scaled, vol="Garch", p=1, q=1)
ftse_results = ftse_model.fit(disp="off")
ftse_omega = ftse_results.params['omega']
ftse_alpha = ftse_results.params['alpha[1]']
ftse_beta = ftse_results.params['beta[1]']


# Step 5: GARCH (1,1) for CAC 40
cac_model = arch_model(cac_returns_scaled, vol="Garch", p=1, q=1)
cac_results = cac_model.fit(disp="off")
cac_omega = cac_results.params['omega']
cac_alpha = cac_results.params['alpha[1]']
cac_beta = cac_results.params['beta[1]']


# Step 6: Exports the result
output_file = "/Users/gauthamganesan/Downloads/GARCH_Results.xlsx"
wb = Workbook()
ws = wb.active
ws.title = "GARCH Parameters"
ws.append(["Index", "Omega", "Alpha", "Beta"])
ws.append(["DJIA", djia_omega, djia_alpha, djia_beta])
ws.append(["FTSE 100", ftse_omega, ftse_alpha, ftse_beta])
ws.append(["CAC 40", cac_omega, cac_alpha, cac_beta])
wb.save(output_file)
