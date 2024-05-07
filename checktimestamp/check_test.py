import os
import re
from datetime import datetime

# Example usage
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


##Read folder
# Specify the path to the folder
folder_path = '/home/ubuntu2004/CODE/smu_data/daily_staging_env'
dailysetfolder_path = '/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset'
# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

# Print the contents of the folder
# for file in folder_contents:
    # print('file',file)

i=0
array=[]
for item in folder_contents:
    #1 copy to staging_copy
    fileobj__= extract_timestamp(i,item)
    #2 compile to dailyset
    if (fileobj__.conditional == True):
        dailysetfolder_contents = os.listdir(dailysetfolder_path)
        if fileobj__.name in dailysetfolder_contents: 
            # print("exist") 
        else: 
            # print("not exist")
            # Create the directory if not exist
            path = os.path.join(dailysetfolder_path, f"{fileobj__.name}")             
            os.mkdir(path) 
            
        # print('dailysetfolder_contents',dailysetfolder_contents)
        #logging
        array.append(fileobj__)
    i +=1
    #3 Logging success
    # print('array',array[-1].name)
