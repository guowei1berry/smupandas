import pandas as pd
from dateutil.parser import parse

# data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
data1 = pd.read_csv("3.csv")#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("4.csv",skiprows=[1,2,3])#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
data3 = pd.concat([data1,data2],ignore_index=False, axis=0) # needs right header for concat to work
data3.to_csv("concatclean.csv")