#encoding=utf-8
import tkFileDialog
import tkMessageBox
import xlrd
import xlwt
import os

print u'''nihao 你好'''
source_filename=tkFileDialog.askopenfilenames(title='file',filetypes=[('excel','*.xls *.xlsx')])
if len(source_filename)==0:
    print u'无文件被选择'
    exit() 
filename_target=os.path.splitext(source_filename[0])[0]+'-Merge.xls'
print os.path.split(filename_target),os.listdir(os.path.split(filename_target)[0])
if os.path.split(filename_target)[1] in os.listdir(os.path.split(filename_target)[0]):
    print u'文件已存在！'
    exit()
file_temp=xlwt.Workbook()
Sheet_target=file_temp.add_sheet('Sheet1')
target_row=1
for temp in source_filename:
    #try:
        date_temp=xlrd.open_workbook(filename=temp)
        sheet=date_temp.sheets()[0]
        rows=sheet.nrows
        cols=sheet.ncols
        print temp,rows,cols
        for x in range(1,rows):
            for y in range(cols):
                Sheet_target.write(target_row,y,sheet.row_values(x)[y])
            target_row+=1      
else:
    for y in range(cols):
        Sheet_target.write(0,y,sheet.row_values(0)[y])  
file_temp.save(filename_target)        
  
    #    tkMessageBox.showinfo(message='Error! Merge failed!')
        