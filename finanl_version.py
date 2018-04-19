
#encoding=utf-8

import xlrd

#xlxs module
import openpyxl



# windows modules
import tkFileDialog
import tkMessageBox

import os



#if read from xls,using this function
def Xls_Read(Target_sheet,source_xls,begin_row):
    target_row=begin_row
    xls_temp=xlrd.open_workbook(filename=source_xls)
    source_sheet=xls_temp.sheets()[0]
    for x in range(1,source_sheet.nrows):
        for y in range(source_sheet.ncols):
            xlsx_index='%s%d'%(chr(y+97),target_row)
            Target_sheet[xlsx_index].value=source_sheet.row_values(x)[y]

        ''' 
            print xlsx_index
            print source_sheet.row_values(x)[y]
            print type(source_sheet.row_values(x)[y])
        '''

        target_row=target_row+1
    else:
        for y in range(source_sheet.ncols):
            xlsx_index='%s%d'%(chr(y+97),1)
            Target_sheet[xlsx_index].value=source_sheet.row_values(0)[y]
    del xls_temp
    return  target_row


def Xlsx_Read(Target_sheet,source_xlsx,begin_row):
    target_row=begin_row
    xlsx_temp=openpyxl.load_workbook(filename=source_xlsx)
    source_sheet=xlsx_temp[xlsx_temp.sheetnames[0]]
    for x in range(2,source_sheet.max_row):
        for y in range(97,97+source_sheet.max_column):
            source_index='%s%d'%(chr(y),x)
            target_index='%s%d'%(chr(y),target_row)
            Target_sheet[target_index].value=source_sheet[source_index].value
        target_row=target_row+1
    else:
        for y in range(97,97+source_sheet.max_column):
            source_index='%s%d'%(chr(y),1)
            target_index='%s%d'%(chr(y),1)
            Target_sheet[target_index].value=source_sheet[source_index].value
    xlsx_temp.close()   
    del xlsx_temp       
    return  target_row

source_filename=tkFileDialog.askopenfilenames(title='file',filetypes=[('excel','*.xls *.xlsx')])
if len(source_filename)==0:
    print u'无文件被选择'
    exit() 
filename_target=os.path.splitext(source_filename[0])[0]+'-Merge.xlsx'
if os.path.split(filename_target)[1] in os.listdir(os.path.split(filename_target)[0]):
    print u'文件已存在！'
    exit()

file_write=openpyxl.Workbook()
file_write.save(filename_target)
file_write.close()
w1=openpyxl.load_workbook(filename_target)
Sheet_target=w1[w1.sheetnames[0]]
target_row=2
for temp in source_filename:
    print temp
    if os.path.splitext(temp)[1]=='.xls':
        target_row=Xls_Read(Sheet_target,temp,target_row)
    else:
        target_row=Xlsx_Read(Sheet_target,temp,target_row)
w1.save(filename_target)


