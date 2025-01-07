# Risk Management Assignment 1
# Data Analysis: Principal Component Analysis

# Steps,
# 1. Import the clean data
# 2. Filter the relevant columns (date and all numeric data)
# 3. Compute the covariance matrix
# 4. Perform eigne decomposition
# 5. Export the result



import pandas as pd
import numpy as np


# Step 1: Imports the clean data
file_path_data = "/Users/gauthamganesan/Downloads/data.csv"
dfdata = pd.read_csv(file_path_data)


# Step 2: Filters the relevant columns (date and all numeric data)
date_column = dfdata["DATE"]
numeric_data = dfdata.drop(columns=["DATE"])


# Step 3: Computes the covariance matrix
cov_matrix = numeric_data.cov()


# Step 4: Performs eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]  # Sorting eigenvalues and eigenvectors in descending order
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]


# Step 5: Exports the result
with pd.ExcelWriter("PCA_result.xlsx") as writer:
    # Sheet 1: Clean Data (including DATE column)
    clean_data_with_date = pd.concat([date_column.to_frame(), numeric_data], axis=1)
    clean_data_with_date.to_excel(writer, sheet_name="Clean Data", index=False)

    # Sheet 2: Covariance Matrix
    cov_matrix.to_excel(writer, sheet_name="Covariance Matrix")

    # Sheet 3: Eigenvectors
    pd.DataFrame(eigenvectors, columns=[f"PC{i+1}" for i in range(eigenvectors.shape[1])]).to_excel(
        writer, sheet_name="Eigenvectors", index=False
    )

    # Sheet 4: Eigenvalues
    pd.DataFrame(eigenvalues, columns=["Eigenvalues"]).to_excel(writer, sheet_name="Eigenvalues", index=False)
