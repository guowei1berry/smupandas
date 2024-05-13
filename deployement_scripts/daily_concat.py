import os
import re
from datetime import datetime
import shutil
import pandas as pd
import xlsxwriter

#Check which folder does not exist in daily_Aggregation folder
dailyaggregation_path = f'/home/ubuntu2004/CODE/smu_data/daily_compiled/aggregation/daily_Aggregation'
dailyaggregationSet = set(os.listdir(dailyaggregation_path))
dailycompiledfolder_path = '/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset'
sortedDailySet = set(os.listdir(dailycompiledfolder_path))
missing_in_dailyAggregation = sorted(sortedDailySet.difference(dailyaggregationSet))
# dateSet = '2024-04-17'


def concatDailyStations(dateSet):

    # Specify the path to the folder
    dailysetfolder_path = f'/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset/{dateSet}'

    # Get a list of all files and directories in the dailyset folder
    dailysetfolder = os.listdir(dailysetfolder_path)
    sorted_dailyList = sorted(dailysetfolder)
    no_stations = len(sorted_dailyList)

    print(f'Doing {dateSet}')
    with open("/home/ubuntu2004/CODE/smu_data/daily_compiled/aggregation/logging.txt", "a") as f:
        print(f'Doing {dateSet} with {no_stations}stations', file=f)
    ##Concated path
    mergedpath = f'/home/ubuntu2004/CODE/smu_data/daily_compiled/aggregation/daily_Aggregation/{dateSet}/{dateSet}'
    mergedCSVpath = f'{mergedpath}.csv'
    mergedxlsxpath = f'{mergedpath}.xlsx'
    with open(f'{mergedpath}_{no_stations}stations.txt', "w") as f:   # Opens file and casts as f 
        f.write(f'{no_stations}stations')       # Writing

    #eliminate files with .~lock prefix
    for eachFile in sorted_dailyList:
        if eachFile[0:6]=='.~lock':
            # print('locking',eachFile,f'{dailysetfolder_path}/{eachFile}')
            os.remove(f'{dailysetfolder_path}/{eachFile}')

    #Concat horizontally
    for eachFile in sorted_dailyList:

        if os.path.isfile(mergedCSVpath) ==False:
            readFirstFile = pd.read_csv(f'{dailysetfolder_path}/{eachFile}',header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
            slicedFirst = eachFile[0:9]
            readFirstFile.insert(0, f'{slicedFirst}=>', f'{slicedFirst}=>')
            readFirstFile.to_csv(mergedCSVpath)
            prevFile = eachFile

        else:  
            
            readPrevFile = pd.read_csv(f'{mergedCSVpath}',index_col=0)#usecols = cols) #skiprows=4,index_col=None)#,skiprows=5)
            readCurrentFile = pd.read_csv(f'{dailysetfolder_path}/{eachFile}',header=[1],index_col=0)#,header=[1],skiprows=[2,3])#findHeaderrow(data1)) #header index is start from 0, so this means 2nd row
            slicedCurrent = eachFile[0:9]
            readCurrentFile.insert(0, f'{slicedCurrent}=>', f'{slicedCurrent}=>')
            data3 = pd.concat([readPrevFile,readCurrentFile],ignore_index=False, axis=1,join='outer') # needs right header for concat to work
            data3.to_csv(mergedCSVpath)

    #output Excel with multiple sheets and concatenated data
    with pd.ExcelWriter(f'{mergedxlsxpath}', engine='openpyxl') as writer: #engine='xlsxwriter') as writer: 
        
        #Write ALL-Stations data to one tab
        concatdf = pd.read_csv(mergedCSVpath) 
        concatdf.to_excel(writer, sheet_name=f"ALL-STATIONS-{dateSet}", index=True)
        # Write each DataFrame to a separate worksheet #sheetname max 31 char
        for eachFile in sorted_dailyList:
            sliced = eachFile[6:31]
            df = pd.read_csv(f'{dailysetfolder_path}/{eachFile}')
            df.to_excel(writer, sheet_name=f"{sliced}", index=True)


for eachDate in missing_in_dailyAggregation:
    print('eachDateloop',eachDate)
    os.mkdir(f'{dailyaggregation_path}/{eachDate}')
    concatDailyStations(eachDate)
