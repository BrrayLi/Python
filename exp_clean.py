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
        #argue1[index_begin:index_end].rfind('(')<=argur1[index_begin:index_end].rfind(')')
        if argue1[index_begin:index_end].count('(')==argue1[index_begin:index_end].count(')') and \
            argue1[index_begin:index_end].find('(')<=argue1[index_begin:index_end].find(')')   and \
            argue1[index_begin:index_end].rfind('(')<=argue1[index_begin:index_end].rfind(')'):
            temp_list.append(argue1[index_begin:index_end].strip())        
            index_begin=index_end+len(argue2)
        index_end=argue1.find(argue2,index_end+1)    
        #os.system("pause")
    temp_list.append(argue1[index_begin:].strip())
    return temp_list
def find_max_index(para1, para2):
    '''
    用于返回满足para1中最大值的位置，对应的para2中相应位置的值
    ''' 
    index=[]
    max_value=max(para1)
    while True:
        try:
            index.append(para2[para1.index(max_value)])
        except:
            break           
    return index    

import sqlparse
import os 
import openpyxl
import sys

xls_file=openpyxl.load_workbook('exp.xlsx')
sheet=xls_file[xls_file.sheetnames[0]]
sql_sum=[]
para_sum=[]
table_sum=[]
condition_sum=[]
for index in range(1,sheet.max_row+1):
    sheet_index='A'+str(index)
    sql=str(sheet[sheet_index].value)

    print index,sql

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
    sql_sum.append(sql)

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
    para_sum.append(para_list)

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
    table_sum.append(table_list)
    condition_sum.append(condition_list)


'''
print para_list,table_list,condition_list
para_list.sort(key=lambda x:len(x),reverse=True)
table_list.sort(key=lambda x:len(x),reverse=True)
condition_list.sort(key=lambda x:len(x),reverse=True)
print para_list,table_list,condition_list
print type([para_list,table_list,condition_list])

'''
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

'''
example=[]      #供参考使用的例子
example.sort(lambda x:len(x[1]),reverse=True) #根据表个数进行排序
inst=[]         #当前需要处理的实例
result=[] 
para_count_sum=[]

try:    #判断是否存在一致的语句
    index=example.index(inst)
except:
    index=-1    
if index==-1:
    #无完全相同项
    #先对比表格,取相同表格数最大的记录
    table_result=[]
    target_index=[]
    for index   in  len(example):
        if  len(example[index][1])==len(inst[1]):
            target_index.append(1)
        else:
            target_index.append(0)
    target_index=find_max_index(target_index,range(len(example)))
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
    target_index=find_max_index(table_result,target_index)

    #判断参数值是否一致,example[0]
    for index in target_index:
        try:
            example[index].index(inst[0])
            para_count_sum.append(len(inst[0]))
        except:                
            #对比参数列表,example[0]
            example_para=example[index][0]
            para_count=0
            for i in len(inst[0]):
                if inst[0][i]==example_para[i]:
                    para_count=para_count+1
            para_count_sum.append(para_count)
    target_index=find_max_index(para_count_sum,target_index)#取符合条件的Index

    #验证条件记录,example[2]
    condition_count_sum=[]
    for index in target_index:
        try:
            example[index].index(inst[2])
            condition_count_sum.append(len(inst[2]))
        except:
            example_condition=example[index][2]
            condition_count=0
            for i in len(inst[2]):
                if  inst[2][i]==example_para[i]:
                    condition_count=condition+1                   
            condition_count_sum.append(condition_count)
    target_index=find_max_index(condition_count_sum,target_index)
else:
    result[index]='right exp!'

'''
'''
设置最终输出格式
原始SQL;参数列表;涉及表格列表;参考的新函数;入参;入参;入参;.......
以;为分隔符，存放在csv或者txt文件中
'''
file_exp_result=open('test.txt','w')
for i in range(len(sql_sum)):
    #file_exp_result.write(sql+';'+para_list+';'+table_list+';'+target_function+';'+para1+';'+'para2'+';'+....)
    file_exp_result.write(sql_sum[i])
    file_exp_result.write(';'+str(len(para_sum[i])))
    for  string in para_sum[i]:
        file_exp_result.write(';'+string)
    file_exp_result.write(';'+str(len(table_sum[i])))
    for  string in table_sum[i]:
        file_exp_result.write(';'+string)
    file_exp_result.write(';'+str(len(condition_sum[i])))
    for  string in condition_sum[i]:
        file_exp_result.write(';'+string)
    file_exp_result.write('\n')    
file_exp_result.close()