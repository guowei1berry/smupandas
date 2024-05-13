import os
import re
from datetime import datetime
import shutil

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

def moveCSVfromStaging2dailyset(file,dailypath,stagingMovepath):
    shutil.copy(f'{folder_path}/{file}', dailypath)
    shutil.copy(f'{folder_path}/{file}', stagingMovepath)
    os.remove(f'{folder_path}/{file}')
    

##Read folder
# Specify the path to the folder
folder_path = '/home/ftpsensor_user/daily_staging'
dailysetfolder_path = '/home/ftpsensor_user/daily_compiled/dailyset'
dailyMovedfolder_path ='/home/ftpsensor_user/daily_compiled/staging_moved'
# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

i=0
array=[]
for item in folder_contents:
    #1 copy to staging_copy
    fileobj__= extract_timestamp(i,item)
    #2 compile to dailyset
    if (fileobj__.conditional == True):
        dailysetfolder_contents = os.listdir(dailysetfolder_path)
        dailydate = fileobj__.name
        if dailydate in dailysetfolder_contents: 
            # print("folder exist") 
            moveCSVfromStaging2dailyset(item,f'{dailysetfolder_path}/{dailydate}',f'{dailyMovedfolder_path}/{item}')
        else: 
            # print("folder not exist")
            # Create the directory if not exist
            dailysetpath = os.path.join(dailysetfolder_path, f"{dailydate}")             
            os.mkdir(dailysetpath)
            moveCSVfromStaging2dailyset(item,f'{dailysetfolder_path}/{dailydate}',f'{dailyMovedfolder_path}/{item}')
            
        # print('dailysetfolder_contents',dailysetfolder_contents)
        #logging
        array.append(fileobj__)
    i +=1
    #3 Logging success
    # print('array',array[-1].name)
