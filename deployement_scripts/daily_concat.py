import os
import re
from datetime import datetime
import shutil
import pandas as pd
import xlsxwriter

##Read folder
# Specify the path to the folder
dailysetfolder_path = '/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset/2024-04-16'

# Get a list of all files and directories in the folder
dailysetfolder = os.listdir(dailysetfolder_path)

# print('dailysetfolder',dailysetfolder)

# filename = "COOLCOATING_ENVDATA_PERDAY_2024-04-07_00-01-00.402.csv"
# sliced = filename[27:37]
# print('sliced',sliced)
class fileobj:
  def __init__(object_, conditional, name):
    object_.conditional = conditional
    object_.name = name

def extract_timestamp(i,filename):
    #Initialise Object
    initObject = fileobj(False, filename)
    # Extract the basename without extension
    basename = os.path.splitext(filename)[0]
    # slicedbased = basename[0:10]
    # Define the regular expression pattern to match the timestamp format
    # timestamp_pattern = r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})'
    timestamp_pattern = r'\d{4}[/-]\d{2}[/-]\d{2}'
    
    # Use regex to find the timestamp in the filename
    match = re.search(timestamp_pattern, basename)

    if match:
        # Extract matched groups and format the timestamp
        matched_string= match.group()
        # print('matched_string',matched_string)
        # year, month, day = matched_string.split('-')
        # print('year',year)
        # print('month',month)
        # print('day',day)
        initObject.conditional =True
        initObject.name = matched_string  
        # timestamp1 = fileobj
        # timestamp = f"{year}-{month}-{day} {hour}:{minute}:{second}"
        # timestamp = f"{year}-{month}-{day} "
        return initObject
    else:
        # print('Date format check failed')
        ##logging
        return initObject

# for eachFile in dailysetfolder:
#     print('eachFile',eachFile)


# Create a Pandas Excel writer
# with pd.ExcelWriter('output.xlsx') as writer:
#     for i, csv_file in enumerate(csv_files, start=1):
#         # Read CSV into DataFrame
#         df = pd.read_csv(csv_file)
        
#         # Write DataFrame to Excel sheet
#         sheet_name = f"Sheet_{i}"
#         df.to_excel(writer, sheet_name=sheet_name, index=False)
#with pd.ExcelWriter('output.xlsx') as writer:#
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer: #engine='xlsxwriter') as writer: 
    # df.to_excel('output.xlsx', engine='openpyxl', index=False)
    # Write each DataFrame to a separate worksheet #sheetname max 31 char
    for eachFile in dailysetfolder:
        sliced = eachFile[6:31]
        print('sliced',sliced)
        df = pd.read_csv(f'{dailysetfolder_path}/{eachFile}')
        df.to_excel(writer, sheet_name=f"{sliced}", index=True)
        # worksheet = writer.sheets[f'{sliced}']
        # column_len = df[column].astype(str).str.len().max()
        # worksheet.set_column(1, 20, max(10, 30))  # Adjust 10 as per your requirement