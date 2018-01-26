#encoding=utf-8
import Tkinter
import tkFileDialog
import tkMessageBox
import xlrd #read xls
import xlwt #write xls
import os #file operator
import math
import sys 
reload(sys)   
sys.setdefaultencoding('utf-8')   
print(sys.getdefaultencoding())
def openfile():
    #open fileDialog
    sourec_filename = tkFileDialog.askopenfilename(title='File Open', filetypes=[('excel', '*.xls *.xlsx')])
    text1.delete(1.0,Tkinter.END)
    text1.insert(1.0,sourec_filename)
def cutfile():
    sourec_filename=text1.get(1.0,Tkinter.END)
    sourec_filename=sourec_filename.replace(u'\n','')
    print(sourec_filename)
    cut_number=int(ent1.get())
    if  sourec_filename=='':
        tkMessageBox.showinfo('Error','File %s not exists!'%sourec_filename)       
        return
    #get the name and path of file except extension
    target_filename_prepaper=os.path.splitext(sourec_filename)[0]
    filename_temp=os.path.splitext(os.path.split(sourec_filename)[1])[0]+'-1.xls'
    #get  all filename under the path of source file
    #decide file is cut or not 
    if filename_temp in os.listdir(os.path.split(sourec_filename)[0]):
        tkMessageBox.showinfo('Error','File %s exists!'%filename_temp)
    else:
        #open *.xls|*.xlsx to get data
        try:
            data=xlrd.open_workbook(filename=sourec_filename)
            sheet=data.sheets()[0]
            rows=sheet.nrows
            cols=sheet.ncols
            n=(rows-1)//cut_number
            for i in range(n):
                filename_temp=target_filename_prepaper+'-'+str(i+1)+'.xls'
                file_temp=xlwt.Workbook()
                work_sheet=file_temp.add_sheet('Sheet1')   
                #write the header of table
                for k in range(cols):
                    work_sheet.write(0,k,sheet.row_values(0)[k]) 
                for j in range(cut_number):
                    for k in range(cols):
                        #write data by every cell
                        work_sheet.write(j+1,k,sheet.row_values(i*cut_number+j+1)[k])
                file_temp.save(filename_temp)
            #deal last one piece
            if (rows-1)%cut_number!=0:
                filename_temp=target_filename_prepaper+'-'+str(n+1)+'.xls'
                file_temp=xlwt.Workbook()
                work_sheet=file_temp.add_sheet('Sheet1')    
                for k in range(cols):
                        work_sheet.write(0,k,sheet.row_values(0)[k]) 
                for j in range(rows-n*cut_number-1):
                    for k in range(cols):
                        work_sheet.write(j+1,k,sheet.row_values(n*cut_number+j+1)[k])
                file_temp.save(filename_temp)
            tkMessageBox.showinfo(message='Success!  File: \n%s \nhas been cut into %d files!'%(os.path.split(sourec_filename)[1],math.ceil((rows-1)/float(cut_number))))
        except Exception as err:
            tkMessageBox.showinfo(message='Error! Mssage :\n %s \nPlesae try again!'%err)


#main function            
global sourec_filename,cut_number
sourec_filename=''
root = Tkinter.Tk()
root.resizable(0,0)
root.title('APP for Cutting')
root.geometry("320x180+%d+%d"\
%((root.winfo_screenwidth()-320)//2,(root.winfo_screenheight()-180)//2 )   )
fm1=Tkinter.Frame(root,bg='red',height=60)
fm2=Tkinter.Frame(root,bg='blue',height=60)
fm3=Tkinter.Frame(root,bg='green',height=60)

btn1 = Tkinter.Button(fm1, text='File Select', command=openfile)
btn2 = Tkinter.Button(fm2, text='File Cut', command=cutfile)
text1=Tkinter.Text(fm1,height=3,state='normal',width=36)
tex1=Tkinter.StringVar()
tex2=Tkinter.StringVar()
tex3=Tkinter.StringVar()

ent1=Tkinter.Entry(fm2,textvariable=tex1)
ent2=Tkinter.Entry(fm2,textvariable=tex2,state='disabled')
ent3=Tkinter.Entry(fm3,textvariable=tex3,state='disabled')
tex1.set('2000')
tex2.set('Number Of Each Pieces:')
tex3.set('App for cutting *.xls|*.xlsx to pieces!')

fm3.pack(side='top',fill='x')
fm1.pack(side='top',fill='x')
fm2.pack(side='top',fill='x')
text1.pack(side='left',fill='both')
btn1.pack(side='left',fill='both')
btn2.pack(side='right',fill='both')
ent2.pack(side='left',fill='both')
ent1.pack(side='left',fill='both')
ent3.pack(fill='both')
print(''.encode('utf-8'))
root.mainloop()

#eee
