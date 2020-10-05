from nltk import sent_tokenize
import re
import random
import sys
import os

topic_map ={
    0 : "HealthCare",
    1 : "Business&Finance",
    2 : "Politics",
    3 : "CriminalJustice",
    4 : "Culture"
}

topic_map_shortcut = {
    "HealthCare" : "HC",
    "Business&Finance" : "BF",
    "Politics" : "P" ,
    "CriminalJustice" : "CJ",
    "Culture" : "C"
}

file_indices =[] 
''' To store which files have already been used to create multi-topic document . 
    This will be store for each topic'''

for i in range(0,len(topic_map)):
    temp=[]
    file_indices.append(temp)


k=random.randint(1,len(topic_map)) # no of topics
# k=2
topics_indices=[] # store the indices of topics

while True:
    index=random.randint(0,len(topic_map)-1)
    if index not in topics_indices:
        topics_indices.append(index)
    
    if len(topics_indices)==k:
        break

print(k,topics_indices)

data = [] # This contains text of selected files
pointers = [] # This is indicates the current pointer(line) of each file
for i in range(0,k):
    TopicName = topic_map[topics_indices[i]] # TopicName ( TopicNames and Foldernames are same)
    PathToFolder = "./Data/" + TopicName
    No_of_Files = len(os.listdir(PathToFolder))

    while True :
        File_no = random.randint(i,No_of_Files)
        if File_no not in file_indices[topics_indices[i]]:
            break

    print(TopicName,File_no)

    file_indices[topics_indices[i]].append(File_no) # Making that the file has been used to create a Multi-topic document

    Filename = topic_map_shortcut[TopicName] + str(File_no)
    fp = open("./Data/" + TopicName + "/" + Filename,"r")

    text=fp.read()
    text=re.sub("\n",". ",text)
    text=sent_tokenize(text)
    print(len(text))

    data.append(text)
    pointers.append(0)

fp3=open("1.txt","w+")


while True:
    file_number = random.randint(0,k-1) # From which file next line has to be taken
    print(file_number)
    if pointers[file_number]<len(data[file_number]): # Check whether there are any lines left to write
        fp3.write(data[ file_number ][ pointers[file_number] ])
        pointers[file_number]=pointers[file_number]+1

    '''Exit when all the files have reached an end '''
    flag=0
    for i in range(0,k):
        if pointers[i] < len(data[i]):
            flag=1
   
    if flag==0 :
        break

print(pointers)
fp3.close()

    
    

