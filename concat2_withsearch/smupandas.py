import pandas as pd
from dateutil.parser import parse

# Read the CSV file
# data1 = pd.read_csv("table1.csv",skiprows=4)
# data2 = pd.read_csv("table2.csv",header=4) #skiprows=4,index_col=None)#,skiprows=5)
# cols = ['TIMESTAMP','RECORD','BattV','PTemp_C','T108_C']
# cols = [0,2,3,4]



data1 = pd.read_csv("table1.csv",nrows=10) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("table2.csv",nrows=10)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)


# print (data1.iat[3,0])
theobject =data1.iat[2,0]
# print(parse(theobject))
try: 
    if parse(theobject):
        print(parse(theobject))
        print('is dateobject')
    # else: pass
except:
    pass

##identifying HEADER row
wordsearch = 'TIMESTAMP'

def findHeaderrow(dataframe):

    i = 0
    while i < 5:
        if (dataframe.iat[i,0]) == str(wordsearch):
            # print (dataframe.iat[i,0])
            header_row = i + 1 
            # print ("header_row",headeconcat2_withsearchr_row)
            return header_row

        else: i +=1

def findSkiprows_2ndfile(dataframe):
    header_index = findHeaderrow(dataframe)
    print(header_index)
    x=header_index +1
    print (x)
    array =[]
    print(array)
    # print(parse(theobject))
    while x<10:
        theobject =data1.iat[x,0]
        print(theobject)
        try: 
            if parse(theobject):
                print(parse(theobject))
                print('is dateobject')
                skiparray = header_index - x #[index to skip]
                
                array = array + skiparray
                print(array)
                return array
            # else: pass
        except:
            pass
        x += 1
    return

findSkiprows_2ndfile(data2)

data1_header = pd.read_csv("table1.csv",header=[findHeaderrow(data1)]) #header index is start from 0, so this means 2nd row
data2 = pd.read_csv("table2.csv",header=[findHeaderrow(data2)],skiprows=[2,3])#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)


# View the first 5 rows
# print ("table1")
# first_row = data1.loc[data1.index[0]]
# print(data1.iloc[:0])
# print (first_row)
# print (data1.head())
# print ("table2")
# print (data2.head())

# data1.columns=data2.columns

# data3 = pd.concat([data1,data2],ignore_index=True, axis=0)
# data4 = data1.iloc[:0]

# print(data1.iat[0,0])#timestamp
# print(data1.iat[1,0])#TS

# print('results')
# print (data3)
# data3 = pd.concat([data1,data2],ignore_index=True)#,join='inner' ,ignore_index=True)

# data3.to_csv("concat_normal_columns.csv")
# data4.to_csv("iloc.csv")
# data2.head()