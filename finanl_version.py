
#encoding=utf-8

import xlrd

#xlxs module
import openpyxl



# windows modules
import tkFileDialog
import tkMessageBox
import gc  
import os
import time 



#if read from xls,using this function
def Xls_Read(Target_sheet,source_xls):
    time.clock()
    xls_temp=xlrd.open_workbook(filename=source_xls)
    source_sheet=xls_temp.sheets()[0]
    print time.clock()
    for index in range(1,source_sheet.nrows):
        Target_sheet.append(source_sheet.row_values(index))
    print time.clock()
    del xls_temp
    gc.collect()
    return

def Xlsx_Read(Target_sheet,source_xlsx):
    xlsx_temp=openpyxl.load_workbook(filename=source_xlsx)
    source_sheet=xlsx_temp[xlsx_temp.sheetnames[0]]
    for index in source_sheet.iter_rows(min_row=1,max_row=source_sheet.max_row,max_col=source_sheet.max_column):
        Target_sheet.append(['%s' % value.value for value in index])  
    xlsx_temp.close()   
    del xlsx_temp       
    gc.collect()
    return  

source_filename=tkFileDialog.askopenfilenames(title='file',filetypes=[('excel','*.xls *.xlsx')])
if len(source_filename)==0:
    print u'无文件被选择'
    exit() 
filename_target=os.path.splitext(source_filename[0])[0]+'-Merge.xlsx'
if os.path.split(filename_target)[1] in os.listdir(os.path.split(filename_target)[0]):
    print u'文件已存在！'
    exit()

file_write=openpyxl.Workbook(write_only=True)
Sheet_target=file_write.create_sheet()
for temp in source_filename:
    print temp
    if os.path.splitext(temp)[1]=='.xls':
        Xls_Read(Sheet_target,temp)
    else:
        Xlsx_Read(Sheet_target,temp)
file_write.save(filename_target)


