
#concat vertically axis 0
import pandas as pd
from dateutil.parser import parse

# data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
data1 = pd.read_csv("SchoolA_1_Roof_Daily_2024-04-19_00-01-00.277.csv")#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("SchoolA_2_Daily_2024-04-19_00-01-00.906.csv",skiprows=[1,2,3])#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
data3 = pd.concat([data1,data2],ignore_index=False, axis=0) # needs right header for concat to work
data3.to_csv("concatVert.csv")
