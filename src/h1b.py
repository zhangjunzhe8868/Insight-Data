#!/usr/local/bin/python

import csv
from collections import Counter
count=0
count1=0
count2=0
state=[]
job=[]
state_str=[]
state_arr=[]
job_str=[]
job_arr=[]
state_per1=[]
job_per1=[]
#with open ('Book1.csv',newline='',encoding="utf8") as csvfile:
with open ('./input/Book1.csv') as csvfile:
    reader=csv.reader(csvfile,delimiter=';',quotechar='|')
    row1=next(reader)
    for i in range (len(row1)):
        if row1[i].find('SOC_NAME')!=-1:
            job_title=i
        if row1[i].find('WORKSITE_STATE')!=-1:
            employ_state=i
   
    for row in reader:
        count+=1
        if row[2]=='CERTIFIED':
            count1+=1
            state.extend([row[employ_state]])
            job.extend([row[job_title]])
        else:
            count2+=1
            
state_list=Counter(state).most_common(10)
job_list=Counter(job).most_common(10)

for i in range (len(state_list)):
    state_str.append(state_list[i][0])
    state_arr.append(state_list[i][1])   
state_per=list(map(lambda i:i/count1,state_arr))

for i in range (len(job_list)):
    job_str.append(job_list[i][0])
    job_arr.append(job_list[i][1])   
job_per=list(map(lambda i:i/count1,job_arr))

for i in range(len(state_list)):
    temp=format(state_per[i],'.1%')
    state_per1.append(temp)

for i in range(len(job_list)):
    temp=format(job_per[i],'.1%')
    job_per1.append(temp)

state_output=[state_str,state_arr,state_per1]
state_output1=list(map(list, zip(*state_output)))
    
job_output=[job_str,job_arr,job_per1]
job_output1=list(map(list, zip(*job_output)))

output = open('./output/top_10_states.txt','w')
output.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for row in state_output1:
    rowtxt = '{};{};{}'.format(row[0],row[1],row[2])
    output.write(rowtxt)
    output.write('\n')
output.close()
            
output = open('./output/top_10_occupations.txt','w')
output.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for row in job_output1:
    rowtxt = '{};{};{}'.format(row[0],row[1],row[2])
    output.write(rowtxt)
    output.write('\n')
output.close()
            
    

        

