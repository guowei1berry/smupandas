import os
import re
from datetime import datetime
import shutil
def backupDaily(file,dailypath):
    shutil.copy(f'{folder_path}/{file}', dailyBackup_path)

    

##Read folder
# Specify the path to the folder
folder_path = '/home/ubuntu2004/CODE/smu_data/daily_staging_env'
dailyBackup_path ='/home/ubuntu2004/CODE/smu_data/daily_backup'
# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)



for item in folder_contents:
    print('item',item)
    backupDaily(item,f'{dailyBackup_path}/{item}')