import os
import re
from datetime import datetime
import shutil
def moveCSVfromStaging2dailyset(file,dailypath,stagingMovepath):
    shutil.copy(f'{folder_path}/{file}', dailypath)
    shutil.copy(f'{folder_path}/{file}', stagingMovepath)

    

##Read folder
# Specify the path to the folder
folder_path = '/home/ubuntu2004/CODE/smu_data/daily_staging_env'
dailysetfolder_path = '/home/ubuntu2004/CODE/smu_data/daily_compiled/dailyset'
dailyMovedfolder_path ='/home/ubuntu2004/CODE/smu_data/daily_compiled/staging_moved'
# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

item = folder_contents[0]
print('item',item)
moveCSVfromStaging2dailyset(item,f'{dailysetfolder_path}/{item}',f'{dailyMovedfolder_path}/{item}')