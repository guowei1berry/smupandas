
#concat horizontally axis 1
import pandas as pd
from dateutil.parser import parse

eachFile = "SchoolA_1_Roof_Daily_2024-04-19_00-01-00.277.csv"
# data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
data1 = pd.read_csv(eachFile,header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
# data1['FileName'] = 'data1'
sliced = eachFile[0:9]
data1.insert(0, f'{sliced}=>', f'{sliced}=>')
# data1.at[2, 'C'] = 'data1'
print("data1",data1.head)

eachFile2= "SchoolA_2_Daily_2024-04-19_00-01-00.906.csv"
data2 = pd.read_csv(eachFile2,header=[1],index_col=0)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
# data2['FileName'] = 'data2'
sliced2 = eachFile2[0:9]
data2.insert(0, f'{sliced2}=>', f'{sliced2}=>')
# data2.at[2, 'C'] = 'data2'
print("data2",data2.head)
data3 = pd.concat([data1,data2],ignore_index=False, axis=1,join='outer') # needs right header for concat to work
data3.to_csv("concatHoriz.csv")
