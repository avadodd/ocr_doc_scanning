#!/usr/bin/env python
# coding: utf-8

# In[38]:


#this code takes all the raw text files outputted from AWS textract 
#and combines them into one long text file and re-separates them
#so there are not multiple apps in one document


#get the raw text file output for each pdf file and append the data to one huge text doc
#not sure if this chunk is needed or not
directories = "/file/path/"
for directory in directories:
    for files in directory:
            with open('rawText.txt','r') as fr:
                lines = fr.readlines()
            with open(directories+'/all_apps.txt','a') as fw:
                fw.write(lines)
                
    
#text doc with all the pdf text together
filename = directories+"/all_apps.txt"
#substring used to divide documents
sbstr = "1. agency position no."

#clean up text
with open(filename+".txt",'r') as f:
    buff = []
    i = 1
    lines = f.readlines()
    
    for line in lines:
        line = line.lower()
        line = line.strip()
        buff.append(line)
               
output = str("".join(buff))
num = output.count(sbstr)

#split data into seperate files
list = []
for i in range(1,num+1):
    file = open('file{}.txt'.format(i),'w')
    data = output.split(sbstr)[i]
    file.write(data)
    file.close()

