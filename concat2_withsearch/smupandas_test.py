import pandas as pd
from dateutil.parser import parse

data1 = pd.read_csv("3.csv",nrows=10) #header index is start from 0, so this means 2nd row
# data2 = pd.read_csv("4.csv",nrows=10)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
# print("data1",list(data1.columns.values))
# print('data1.iloc[0,0]',data1.iloc[0,0])
##identifying HEADER row
wordsearch = 'TIMESTAMP'

def findHeaderrow(dataframe):
    i = 0
    while i < 5:
        print('dataframe.at[i,0]',dataframe.iat[i,0])
        if (dataframe.iat[i,0]) == str(wordsearch):
            header_row = [i + 1] 

            return header_row

        else: i +=1

def findSkiprows_2ndfile(dataframe):
    header_index = findHeaderrow(dataframe)[0] #header row considered index 1
    x=header_index # Skiprow counting starts from index0 / header row is indexed 1 => add 1 to account for index 0
    array =[]

    while x<10:
        theobject =data1.iat[x,0]
        try: 
            if parse(theobject):
                return array
            # else: pass
        except:
            array.append(x +1)     #error parsing, appends index to array
            pass
        x += 1
    return array
print("findHeaderrow(data1)",findHeaderrow(data1))
# print("findHeaderrow(data1)",findHeaderrow(data1))
# print("findSkiprows_2ndfile(data2)",findSkiprows_2ndfile(data2))
data1_header = pd.read_csv("3.csv")#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
data2_skiprows = pd.read_csv("4.csv",skiprows=[1,2,3])#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
data3 = pd.concat([data1_header,data2_skiprows],ignore_index=False, axis=0) # needs right header for concat to work

# ##Rearrange to add in Logger details
# new_index = [-1] + list(data3.index)
# # Reindex the DataFrame
# data3 = data3.reindex(new_index)
# # Fill in the new row
# data3.loc[-1] = list(data1.columns.values) #["TOA5", "CR300Series_2", "CR350", "5107", "CR350-CELL220.Std.01.04", "CPU:BG Sensor.CRB",	"50250", "Table1"]

data3.to_csv("concat.csv")
