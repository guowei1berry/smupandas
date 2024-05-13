import os
import re
from datetime import datetime
import shutil
import pandas as pd
import xlsxwriter

data1 = pd.read_csv("SchoolA_1_Roof_Daily.csv")
print("data1head",data1.head)

workbook = xlsxwriter.Workbook('outputhere.xlsx')
workbook.add_worksheet('sheet1')

with pd.ExcelWriter('outputhere.xlsx',engine='xlsxwriter') as writer: #engine='xlsxwriter') as writer: 
    # df.to_excel('output.xlsx', engine='openpyxl', index=False)
    # Write each DataFrame to a separate worksheet #sheetname max 31 char
        # sliced = data1[6:31]
        # print('sliced',sliced)
        data1.to_excel(writer, sheet_name="hello1", index=True)
        data1.to_excel(writer, sheet_name="hello2", index=True)