from nltk import sent_tokenize
import re
import random
import numpy as np
import sys
import os
import pandas as pd 


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

Num_of_articles = 300

#failed attempt at trying to exhaust the dataset
# tot_articles = 0
# for i in np.arange(len(topic_map)):
#     # TopicName = topic_map[topics_indices[i]] # TopicName ( TopicNames and Foldernames are same)
#     PathToFolder = "./Data/" + topic_map[i]
#     No_of_Files = len(os.listdir(PathToFolder))
#     tot_articles += No_of_Files


file_indices = [[] for i in np.arange(len(topic_map))]
''' To store which files have already been used to create multi-topic document . 
    This will be stored for each topic'''


total = []
for make in np.arange(Num_of_articles):
# while tot_articles>0:
    k=random.randint(1,len(topic_map)) # no of topics
    # k=2

    indices = list(range(len(topic_map)))
    random.shuffle(indices)
    topics_indices = indices[:k]

    names = [topic_map[topics_indices[i]] for i in np.arange(0,k)]
    print(k,topics_indices, names)


    data = [] # This contains text of selected files
    pointers = [] # This is indicates the current pointer(line) of each file
    for i in np.arange(0,k):
        TopicName = topic_map[topics_indices[i]] # TopicName ( TopicNames and Foldernames are same)
        PathToFolder = "./Data/" + TopicName
        No_of_Files = len(os.listdir(PathToFolder))

        while True :
            File_no = random.randint(1,No_of_Files)
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

    # fp3=open("1.txt","w+")
    # tot_articles -= len(pointers)
    single_doc = []
    topic_order = []
    while True:
        file_number = random.randint(0,k-1) # From which file next line has to be taken
        print(file_number)
        topic_order.append(file_number)
        if pointers[file_number]<len(data[file_number]): # Check whether there are any lines left to write
            single_doc.append(data[ file_number ][ pointers[file_number] ])
            pointers[file_number]=pointers[file_number]+1

        '''Exit when all the files have reached an end '''
        flag=0
        for i in range(0,k):
            if pointers[i] < len(data[i]):
                flag=1
    
        if flag==0 :
            break

    print(pointers)
    total.append([" ".join(single_doc),k,names,topic_order])
    # print(type("".join(single_doc)))

    print(len(single_doc),k,names)
    print()
    # fp3.close()

# print(len(total))
    

# creating a data frame
df = pd.DataFrame(total, columns = ['Doc', 'Num_of_topics', 'Topics', 'Topic_order'])

# writing data frame to a CSV file
df.to_csv(r'~/Desktop/Topic-based-Abstarctive-Summarization/data-{}.csv'.format(Num_of_articles))
# print(df)
