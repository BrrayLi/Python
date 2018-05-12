#encoding=utf-8
#encoding=utf-8


'''
阶段一目标：根据现网表找BSS改造后的对应表名及所属中心

'''
import os
import openpyxl
import sys

# sys.argv[0] 参数一

reload(sys)  
sys.setdefaultencoding('utf8')    

def Read_From_Xlsx(file_name):
    #用于从xlsx中读取数据，作为数据准备
    #使用模块openpyxl

    xls_file=openpyxl.load_workbook(file_name)
    sheet_temp=xls_file[u'现网表映射']
    table_list_old=[]
    table_list_new=[]
    table_list_cen=[]
    for i in range(2,sheet_temp.max_row+1):
        table_list_old.append(sheet_temp['D'+str(i)].value)
        table_list_new.append(sheet_temp['B'+str(i)].value)
        table_list_cen.append(sheet_temp['A'+str(i)].value)
    return table_list_old,table_list_new,table_list_cen


def print_list(target_list):
    #打印输出列表List，若存在嵌套则展开打印
    for l in target_list:
        if type(l) == list:
            print '|'
            print_list(l)
            print '|'
        else :
            print l
            # print '\n'
    return

def Add_Dict(dic,key,value):
    #用于增加字典内容
    for i in range(len(key)):
        try:
            dic[key[i]]=value[i]
            dic[value[i]]=value[i]
        except:
            pass
    return

def Read_From_Txt(file_name):
    table_old=[]
    table_new=[]
    txt_file=open(file_name,'r')
    
    #一次性读取所有行，适用于文件较小
    lines=txt_file.readlines()
    for line in lines:
        index=line.find('|')    #以|作为分割符，|前为旧表名称，|后为新表名称
        if index!=-1:
            table_old.append(line[:index])
            table_new.append(line[index+1:])
        else:
            pass
    # print len(lines),len(table_new)
    txt_file.close()
    return table_old,table_new

#main
###########################################################
###########################################################

reload(sys)
sys.setdefaultencoding("utf-8")


Read_From_Txt('table_list.txt')


#创建字典
dic_table={}
dic_center={}

for xlsxfile in os.listdir(os.getcwd()+r'\table_list'):
    table_old,table_new,table_center=Read_From_Xlsx(os.getcwd()+'\\table_list\\'+xlsxfile)
    Add_Dict(dic_table,table_old,table_new)
    Add_Dict(dic_center,table_new,table_center)


#取传递参数搜索新旧表对应关系
if len(sys.argv) >=2:
    print dic_table[sys.argv[1]]
    print dic_center[dic_table[sys.argv[1]]]
else:
    print 'No argv Input!'


#将所有记录写入txt中，方法以后处理，采用dict.items()方法获取
file_w=open('table_list.txt','w')
for lis in dic_table.items():
    try:
        file_w.write(lis[0][:]+'|'+lis[1][:]+'\n')
    except:
        pass
file_w.close()


file_w=open('table_center.txt','w')
for lis in dic_center.items():
    try:
        file_w.write(lis[0][:]+'|'+lis[1][:]+'\n')
    except:
        pass
file_w.close()        


while True:
    target=raw_input("请输入表名：")
    try:
        print dic_table[target]
        print dic_center[dic_table[target]]
    except:
        print 'Table not exists:'+target
        
