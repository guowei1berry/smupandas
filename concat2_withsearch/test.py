import pandas as pd
from dateutil.parser import parse

data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("4.csv",nrows=10)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)


data1__ = pd.read_csv("3.csv")
data2__ = pd.read_csv("4.csv",skiprows=[1,2,3])
#, skiprows=[1,2,3]) 
print (data1)

print (data2)

data3 = pd.concat([data1__,data2__],ignore_index=False) # needs right header for concat to work


data3.to_csv("concattest.csv")