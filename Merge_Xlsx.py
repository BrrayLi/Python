# encoding=utf8

import tkMessageBox
import xlrd
import xlwt
import os
import tkFileDialog

print '你好'
source_filename=tkFileDialog.askopenfilenames(title='File',filetypes=[('excel','*.xls *.xlsx')])
print type(source_filename)
print source_filename[0]
for i in range(len(source_filename)):
    print source_filename[i]
