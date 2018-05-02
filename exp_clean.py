#encoding=utf-8
'''
step one 
Read from excel,删除多余的字符:\n,空格
step two
解析结构，用字符串组或者链表来完成，提取参数的方法？看是否存在已有的代码可用  模块sqlparse 
结构可类似
判断同一层级下的条件，计算当前范围内的左右括号数量
main_exp,length,para1,para2,....


相似度判断规则
1、直接使用list.index查找，完全相同才能确认
2、判断各元素，table para condition，次序应为para table condition或者table para condition 
3、考虑是否需要判断下层层级

select  from
from    where
union   
and     
step three 
进行比较，根据长度，结构相似度
'''

def Get_Condition(argue1):
    return 'sda'
def separate(argue1,argue2):
    temp_list=[]
    index_begin=0
    index_end=argue1.find(argue2)
    while index_end!=-1:
        #是否需要增加条件，第一个出现的（必须比）早，最后一个出现的）必须比（晚
        #argue1[index_begin:index_end].find('(')<=argur1[index_begin:index_end].find(')')   && \
        # argue1[index_begin:index_end].rfind('(')<=argur1[index_begin:index_end].rfind(')')
        if argue1[index_begin:index_end].count('(')==argue1[index_begin:index_end].count(')'):
            temp_list.append(argue1[index_begin:index_end])        
            index_begin=index_end+len(argue2)
        index_end=argue1.find(argue2,index_end+1)    
        #os.system("pause")
    temp_list.append(argue1[index_begin:])
    return temp_list

import sqlparse
import os 
import openpyxl
import sys

xls_file=openpyxl.load_workbook('exp.xlsx')
sheet=xls_file[xls_file.sheetnames[0]]
sql=sheet['A2'].value
sql=sql.replace('\n','').replace('_x000D_','') #清除回车及excel特有的换行符
sql=' '.join(sql.split())
sql=sql.lower()
#print sql
condition=''
#sql='select p1,p2 from (select p from (dsds) t1) t2,dsa2 e3 where t2.serv=21132111 and t1.sfd=213 and fds3=321fd'
#step 1     判断是否开始有函数,并去除最外层的函数
if sql.find('decode') != -1:
    sql=sql[7:]    
    sql=sql[:sql.rfind(')')]
if  sql.find('nvl') !=-1:
    sql=sql[4:len(sql)]
    sql=sql[:sql.rfind(')')]
if sql[0:1]=='(':
    sql=sql[1:sql.rfind(')')]

#print sql
#os.system("pause")
#第一个select 即是第一层select from 
index_begin=sql.find('select')
index_end=sql.find('from')
while sql[index_begin:index_end].count('(')!=sql[index_begin:index_end].count(')'):
    index_end=sql.find('from',index_end+1)
    if index_end==-1:
        break
para1=sql[index_begin+7:index_end-1]
para_list=separate(para1,',')

#第一个from where
index_begin=index_end
index_end=sql.find('where')
while sql[index_begin:index_end].count('(')!=sql[index_begin:index_end].count(')'):
    index_end=sql.find('where',index_end+1)
    if index_end==-1:
        break
if  index_end==-1:  
    table1=sql[index_begin+5:]
else    :
    table1=sql[index_begin+5:index_end-1]
    condition=sql[index_end+6:]
table_list=separate(table1,',')
condition_list=separate(condition,'and')

'''debug
print 'para1:'+para1+'\n'
print 'para_list:',len(para_list),'\n',para_list
print 'tables:',len(table1),'\n',table1
print 'tables:',len(table_list),'\n',table_list
print '\n'
print 'condition:'+condition
print 'condition_list:',len(condition_list),'\n'
print condition_list
'''
#print 'select '+para1+' from '+table1+' where '+condition

example=[]
example.sort(lambda x:len(x[1]),reverse=True) #根据表个数进行排序
result=[]
inst=[]

try:
    index=example.index(inst)
except:
    index=-1
    
if index==-1:
    #无完全相同项
    #选对比表格
    index=1
    table_result=[]
    target_index=[]
    for  index  in  target_index:
        example_table=example[index][1]
        table_num_same=0
        for  table_name in inst[1]:
            try:
                example_table.index(table_name) #逐个表查找
                table_num_same+=1
            except:
                pass
        table_result.append(table_num_same)
    target_index=table_result.index(max(table_result))
    #判断参数值是否一致
    try:
        example[target_index].index(inst[0])
    except:
        pass
    
else:
    result[index]='right exp!'

