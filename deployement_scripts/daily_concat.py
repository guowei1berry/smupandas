import os
import re
from datetime import datetime
import shutil
import pandas as pd
import xlsxwriter

dateSet = '2024-04-17'
# Specify the path to the folder
dailysetfolder_path = f'/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset/{dateSet}'

# Get a list of all files and directories in the folder
dailysetfolder = os.listdir(dailysetfolder_path)
sorted_dailyset = sorted(dailysetfolder)

#eliminate files with .~lock prefix
for eachFile in sorted_dailyset:
    print('eachFile[0:6]',eachFile[0:6])
    if eachFile[0:6]=='.~lock':
        print('locking',eachFile,f'{dailysetfolder_path}/{eachFile}')
        os.remove(f'{dailysetfolder_path}/{eachFile}')

#Concat horizontally
print('sorted_dailyset',sorted_dailyset)

for eachFile in sorted_dailyset:

    if os.path.isfile('/home/ubuntu2004/CODE/smu_env/deployement_scripts/concatedHoriz.csv') ==False:
        readFirstFile = pd.read_csv(f'{dailysetfolder_path}/{eachFile}',header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
        slicedFirst = eachFile[0:9]
        readFirstFile.insert(0, f'{slicedFirst}=>', f'{slicedFirst}=>')
        readFirstFile.to_csv("concatedHoriz.csv")
        prevFile = eachFile
        print('prevFile',prevFile)  

    else:  
        
        readPrevFile = pd.read_csv('concatedHoriz.csv',index_col=0)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
        print('prevFile>>>',readPrevFile.head)
        readCurrentFile = pd.read_csv(f'{dailysetfolder_path}/{eachFile}',header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
        slicedCurrent = eachFile[0:9]
        readCurrentFile.insert(0, f'{slicedCurrent}=>', f'{slicedCurrent}=>')
        print("readPrevFile",readPrevFile.head)
        data3 = pd.concat([readPrevFile,readCurrentFile],ignore_index=False, axis=1,join='outer') # needs right header for concat to work
        data3.to_csv("concatedHoriz.csv")

#output Excel with multiple sheets and concatenated data
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer: #engine='xlsxwriter') as writer: 
    
    concatdf = pd.read_csv("concatedHoriz.csv") 
    concatdf.to_excel(writer, sheet_name=f"ALL-STATIONS-{dateSet}", index=True)
    # Write each DataFrame to a separate worksheet #sheetname max 31 char
    for eachFile in sorted_dailyset:
        sliced = eachFile[6:31]
        print('sliced',sliced)
        df = pd.read_csv(f'{dailysetfolder_path}/{eachFile}')
        df.to_excel(writer, sheet_name=f"{sliced}", index=True)

