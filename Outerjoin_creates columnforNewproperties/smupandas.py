import pandas as pd

# Read the CSV file
data1 = pd.read_csv("table1.csv",dtype={'PTemp_C': int})
data2 = pd.read_csv("table2.csv",dtype={'PTemp_C': int})

# View the first 5 rows
# print (data1.head())
# print (data2.head())

data3 = pd.merge(data2,data1, how="outer")

data3.to_csv("merged.csv")
# data2.head()