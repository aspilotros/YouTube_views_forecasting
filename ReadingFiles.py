# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:56:56 2017

@author: Alessandro
GOAL:
Reading the XML files of YouTube Crawler extrating the time series of views

INPUT OUTPUT: 
Directory Complete path is the path of the data folder
Example of Directory C:/Users/Alessandro/windows-share/Portfolio/Firstbatch/data
The output files are written one directory up in respect data

PROGRAM STRUCTURE
1. The program is reading the names of all the files in the directory and creating
a txt file with these names

2. The program is opening all the files in the directory, parsing them as xml and
writing the relevant data to a pandas dataframe together with the name of the file
which correspond to the video ID (identification code) 
"""
#import numpy as np
import pandas as pd
import os

import xml.etree.ElementTree as ET
import json
import pickle

#%% Reading all the file names from the directory and importing them into a pandas DF

try:
    DIRECTORY = input("Directory complete path: ")
    os.chdir(DIRECTORY)
    directory_split = DIRECTORY.split("/")
    
    FILE_IDs = directory_split[directory_split.__len__() - 2] + "-IDs.txt"
    FILE_NAMES = open("../" + FILE_IDs, "w")
    
    for path, subdirs, files in os.walk(DIRECTORY):
        for filename in files:
            #f = os.path.join(path, filename)
            FILE_NAMES.write(str(filename)+"\n") 
    FILE_NAMES.close()
except: 
    print ("Directory not found")

df_ids = pd.read_csv("../" + FILE_IDs, header=None, names=["ids"])
#%% Reading the view counts per day from the all the files in the directory
dict_data=dict()
j = 0
file_names=df_ids.iloc[:,0]
for line in file_names:
    #file = open(DIRECTORY + "/" + line.rstrip('\n'), 'r')
    file= open(DIRECTORY + "/" + line, 'r') 
    f=file.read()
    
    try: # not all the xml crawled are well formed
        tree=ET.fromstring(f)
        file.close()
        text_data=tree.find("graph_data").text
        viewcounts=json.loads(text_data) 
        viewcounts=viewcounts["views"]["daily"]["data"]
    
    except:
        file.close()
        continue
    
    name=line
    dict_data[name]=viewcounts

    print(j) # to have a feedback on the status of the for loop
    j=j+1
pickle.dump(dict_data,open("../" + FILE_IDs.strip('.txt') + ".p","wb"))
#%% Creating the pandas data frame
df_data = pd.DataFrame.from_dict(dict_data, orient='index')
df_data.to_csv("../" + FILE_IDs.strip('.txt'))