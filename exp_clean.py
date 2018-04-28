#encoding=utf-8
'''
step one 
Read from excel,删除多余的字符:\n,空格
step two
解析结构，用字符串组或者链表来完成，提取参数的方法？看是否存在已有的代码可用  模块sqlparse 
结构可类似
判断同一层级下的条件，计算当前范围内的左右括号数量
main_exp,length,para1,para2,....

select  from
from    where
union   
and     
step three 
进行比较，根据长度，结构相似度
'''

def Get_Condition():
    return 


import sqlparse
import os 
import openpyxl

xls_file=openpyxl_loadworkbook('exp.xls')

sheet=xls_file[xls_file.sheetnames[0]]

sql=u''
sql.replace('\n','').replace('_x000D_','') #清除回车及excel特有的换行符

#step 1     判断是否开始有函数
if sql.find('decode') != -1:
    sql=sql[6:]
elif  sql.find('nvl') !=-1:
    sql=sql[3:]
'''
step 2  根据select from 
            from where 
            and
            and 
'''
#第一个select 即是第一层select from 
index_begin=sql.find('select')
index_end=sql.find('from')
while sql[index_begin:index_end].count('(')!=sql[index_begin:index_end].count(')'):
    index_end=sql.find('from',index_end+1)
    if index_end==-1:
        break
para1=sql[index_begin+6:index_end]

#第一个from where
index_begin=index_end
index_end=sql.find('where')
while sql[index_begin:index_end].count('(')!=sql[index_begin:index_end].count(')'):
    index_end=sql.find('where',index_end+1)
    if index_end==-1:
        break
if  index_end==-1:  
    table1=sql[index_begin:index_end]
else    :
    table1=sql[index_begin:]
    condition=Get_Condition(sql)






print sql