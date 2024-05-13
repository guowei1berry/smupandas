import os

# Specify the path to the folder
folder_path = '/home/ubuntu2004/CODE/smu_env/checktimestamp/'

# Get a list of all files and directories in the folder
folder_contents = os.listdir(folder_path)

# Print the contents of the folder
for item in folder_contents:
    print(item)