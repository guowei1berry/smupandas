import pandas as pd

# Read the CSV file
data1 = pd.read_csv("table1.csv")
data2 = pd.read_csv("table2.csv")

# View the first 5 rows
# print (data1.head())
# print (data2.head())

data1.append(data2, ignore_index=True)#,axis=0,join='inner' ,ignore_index=True)


# data3.to_csv("concat_ignoreindex.csv")
# data2.head()