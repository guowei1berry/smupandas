import os
import re
from datetime import datetime
import shutil
import pandas as pd
import xlsxwriter

# Specify the path to the folder
dailysetfolder_path = '/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset/2024-04-16'

# Get a list of all files and directories in the folder
dailysetfolder = os.listdir(dailysetfolder_path)
sorted_dailyset = sorted(dailysetfolder)


##output Excel with multiple sheets and concatenated data
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer: #engine='xlsxwriter') as writer: 
    # Write each DataFrame to a separate worksheet #sheetname max 31 char
    for eachFile in sorted_dailyset:
        sliced = eachFile[6:31]
        print('sliced',sliced)
        df = pd.read_csv(f'{dailysetfolder_path}/{eachFile}')
        df.to_excel(writer, sheet_name=f"{sliced}", index=True)
