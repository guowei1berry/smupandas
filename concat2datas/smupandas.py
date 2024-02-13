import pandas as pd

# Read the CSV file
# data1 = pd.read_csv("table1.csv",skiprows=4)
# data2 = pd.read_csv("table2.csv",header=4) #skiprows=4,index_col=None)#,skiprows=5)
# cols = ['TIMESTAMP','RECORD','BattV','PTemp_C','T108_C']
cols = [0,2,3,4]

data1 = pd.read_csv("table1.csv",header=[1])
data2 = pd.read_csv("table2.csv",header=[1],skiprows=[2,3])#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)


# View the first 5 rows
print ("table1")
print (data1.head())
print ("table2")
print (data2.head())

# data1.columns=data2.columns

data3 = pd.concat([data1,data2],ignore_index=True, axis=0)
print('results')
print (data3)
# data3 = pd.concat([data1,data2],ignore_index=True)#,join='inner' ,ignore_index=True)

data3.to_csv("concat_normal_columns.csv")
# data2.head()