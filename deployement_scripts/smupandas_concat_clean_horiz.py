
#concat horizontally axis 1
import pandas as pd
from dateutil.parser import parse

# data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
data1 = pd.read_csv("SchoolA_1_Roof_Daily_2024-04-19_00-01-00.277.csv",header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
# data1['FileName'] = 'data1'
data1.insert(0, 'Data1', 'data1')
# data1.at[2, 'C'] = 'data1'
print("data1",data1.head)
data2 = pd.read_csv("SchoolA_2_Daily_2024-04-19_00-01-00.906.csv",header=[1],index_col=0)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
# data2['FileName'] = 'data2'
data2.insert(0, 'Data2', 'data2')
# data2.at[2, 'C'] = 'data2'
print("data2",data2.head)
data3 = pd.concat([data1,data2],ignore_index=False, axis=1,join='outer') # needs right header for concat to work
data3.to_csv("concatHoriz.csv")
