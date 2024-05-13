import os
import re
from datetime import datetime

# Example usage
filename = "COOLCOATING_ENVDATA_PERDAY_2024-04-07_00-01-00.402.csv"
sliced = filename[27:37]

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
folder_path = '/home/ubuntu2004/CODE/smu_env/checktimestamp/'

# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

# Print the contents of the folder

i=0
array=[]
for item in folder_contents:
    # print(i,item)
    # print(i,extract_timestamp(i,item))
    fileobj__= extract_timestamp(i,item)
    # print('fileobjcond',fileobj__.conditional,'fileobjname',fileobj__.name)
    # print(extract_timestamp(i,item)[1])
    if (fileobj__.conditional == True):
        array.append(fileobj__)
    i +=1

print('array',array[1].name)