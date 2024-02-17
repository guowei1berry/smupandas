import pandas as pd
from dateutil.parser import parse

data1 = pd.read_csv("table1.csv",nrows=10) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("table2.csv",nrows=10)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)

##identifying HEADER row
wordsearch = 'TIMESTAMP'

def findHeaderrow(dataframe):
    i = 0
    while i < 5:
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

data1_header = pd.read_csv("table1.csv",header=findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
data2_skiprows = pd.read_csv("table2.csv",header=findHeaderrow(data2),skiprows=findSkiprows_2ndfile(data2))#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)


data3 = pd.concat([data1_header,data2_skiprows],ignore_index=True, axis=0)
data3.to_csv("concat.csv")
