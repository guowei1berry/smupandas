import os
import re
from datetime import datetime

# Example usage
filename = "COOLCOATING_ENVDATA_PERDAY_2024-04-07_00-01-00.402.csv"
sliced = filename[27:37]

def extract_timestamp(i,filename):
    # Extract the basename without extension
    basename = os.path.splitext(filename)[0]
    # slicedbased = basename[0:10]
    # Define the regular expression pattern to match the timestamp format
    # timestamp_pattern = r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})'
    # timestamp_pattern = r'(\d{4})(\d{2})(\d{2}))'
    timestamp_pattern = r'\d{4}[/-]\d{2}[/-]\d{2}'
    
    # Use regex to find the timestamp in the filename
    match = re.search(timestamp_pattern, basename)

    if match:
        # Extract matched groups and format the timestamp
        matched_string= match.group()
        year, month, day = matched_string.split('-')
        # print('year',year)
        # print('month',month)
        # print('day',day)
        timestamp1 = matched_string
        # timestamp = f"{year}-{month}-{day} {hour}:{minute}:{second}"
        # timestamp = f"{year}-{month}-{day} "
        return timestamp1
    else:
        print('Date format check failed')
        ##logging
        return None

# print(extract_timestamp(sliced))

# timestamp = extract_timestamp(sliced)
# if timestamp:
#     print("Timestamp extracted from filename:", timestamp)
# else:
#     print("No timestamp found in the filename.")


##read folder
# Specify the path to the folder
folder_path = '/home/ubuntu2004/CODE/smu_env/checktimestamp/'

# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

# Print the contents of the folder

i=0
for item in folder_contents:
    # print(i,item)
    print(i,extract_timestamp(i,item))
    i +=1