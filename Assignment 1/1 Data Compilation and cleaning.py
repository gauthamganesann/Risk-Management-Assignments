# Risk Management Assignment 1
# Data Compilation and Cleaning

# Steps,
# 1. Import the raw data
#    Maturities: 1Y, 2Y, 3Y, 4Y, 5Y, 6Y, 7Y, 8Y, 9Y, 10Y, 12Y, 15Y, 20Y, 25Y, 30Y
# 2. Rename the columns
# 3. Filter out the relevant columns
# 4. Merge all the dataframes
# 5. Export the clean data



import pandas as pd


# Step 1: Imports the raw data
file_path_1Y = "/Users/gauthamganesan/Downloads/Raw Data/1Y ECB Data.csv"
file_path_2Y = "/Users/gauthamganesan/Downloads/Raw Data/2Y ECB Data.csv"
file_path_3Y = "/Users/gauthamganesan/Downloads/Raw Data/3Y ECB Data.csv"
file_path_4Y = "/Users/gauthamganesan/Downloads/Raw Data/4Y ECB Data.csv"
file_path_5Y = "/Users/gauthamganesan/Downloads/Raw Data/5Y ECB Data.csv"
file_path_6Y = "/Users/gauthamganesan/Downloads/Raw Data/6Y ECB Data.csv"
file_path_7Y = "/Users/gauthamganesan/Downloads/Raw Data/7Y ECB Data.csv"
file_path_8Y = "/Users/gauthamganesan/Downloads/Raw Data/8Y ECB Data.csv"
file_path_9Y = "/Users/gauthamganesan/Downloads/Raw Data/9Y ECB Data.csv"
file_path_10Y = "/Users/gauthamganesan/Downloads/Raw Data/10Y ECB Data.csv"
file_path_12Y = "/Users/gauthamganesan/Downloads/Raw Data/12Y ECB Data.csv"
file_path_15Y = "/Users/gauthamganesan/Downloads/Raw Data/15Y ECB Data.csv"
file_path_20Y = "/Users/gauthamganesan/Downloads/Raw Data/20Y ECB Data.csv"
file_path_25Y = "/Users/gauthamganesan/Downloads/Raw Data/25Y ECB Data.csv"
file_path_30Y = "/Users/gauthamganesan/Downloads/Raw Data/30Y ECB Data.csv"

df1 = pd.read_csv(file_path_1Y)
df2 = pd.read_csv(file_path_2Y)
df3 = pd.read_csv(file_path_3Y)
df4 = pd.read_csv(file_path_4Y)
df5 = pd.read_csv(file_path_5Y)
df6 = pd.read_csv(file_path_6Y)
df7 = pd.read_csv(file_path_7Y)
df8 = pd.read_csv(file_path_8Y)
df9 = pd.read_csv(file_path_9Y)
df10 = pd.read_csv(file_path_10Y)
df12 = pd.read_csv(file_path_12Y)
df15 = pd.read_csv(file_path_15Y)
df20 = pd.read_csv(file_path_20Y)
df25 = pd.read_csv(file_path_25Y)
df30 = pd.read_csv(file_path_30Y)


# Step 2: Renames the columns
df1.columns = ["DATE", "TIME PERIOD", "1Y Yield"]
df2.columns = ["DATE", "TIME PERIOD", "2Y Yield"]
df3.columns = ["DATE", "TIME PERIOD", "3Y Yield"]
df4.columns = ["DATE", "TIME PERIOD", "4Y Yield"]
df5.columns = ["DATE", "TIME PERIOD", "5Y Yield"]
df6.columns = ["DATE", "TIME PERIOD", "6Y Yield"]
df7.columns = ["DATE", "TIME PERIOD", "7Y Yield"]
df8.columns = ["DATE", "TIME PERIOD", "8Y Yield"]
df9.columns = ["DATE", "TIME PERIOD", "9Y Yield"]
df10.columns = ["DATE", "TIME PERIOD", "10Y Yield"]
df12.columns = ["DATE", "TIME PERIOD", "12Y Yield"]
df15.columns = ["DATE", "TIME PERIOD", "15Y Yield"]
df20.columns = ["DATE", "TIME PERIOD", "20Y Yield"]
df25.columns = ["DATE", "TIME PERIOD", "25Y Yield"]
df30.columns = ["DATE", "TIME PERIOD", "30Y Yield"]


# Step 3: Filters the relevant columns
df1 = df1.loc[:, ["DATE", "1Y Yield"]]
df2 = df2.loc[:, ["DATE", "2Y Yield"]]
df3 = df3.loc[:, ["DATE", "3Y Yield"]]
df4 = df4.loc[:, ["DATE", "4Y Yield"]]
df5 = df5.loc[:, ["DATE", "5Y Yield"]]
df6 = df6.loc[:, ["DATE", "6Y Yield"]]
df7 = df7.loc[:, ["DATE", "7Y Yield"]]
df8 = df8.loc[:, ["DATE", "8Y Yield"]]
df9 = df9.loc[:, ["DATE", "9Y Yield"]]
df10 = df10.loc[:, ["DATE", "10Y Yield"]]
df12 = df12.loc[:, ["DATE", "12Y Yield"]]
df15 = df15.loc[:, ["DATE", "15Y Yield"]]
df20 = df20.loc[:, ["DATE", "20Y Yield"]]
df25 = df25.loc[:, ["DATE", "25Y Yield"]]
df30 = df30.loc[:, ["DATE", "30Y Yield"]]


# Step 4: Merges all the dataframes
merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df12, df15, df20, df25, df30], axis=1)
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()] # Removes duplicate "DATE" columns


# Step 5: Exorts the clean data
merged_df.to_csv("data.csv", index=False)
merged_df.to_excel("data.xlsx", index=False)
