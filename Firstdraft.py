#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 23:34:20 2017

@author: ale
"""
import pandas as pd
import numpy as np

#%%
df = pd.read_csv('/home/ale/Desktop/Portfolio/yt8M_train_labels.csv',header=None)
np.sum(df.isnull()) #Cheking for null values
#%%
#Creating a random permutation of the indexes and saving as csv
np.random.seed(42)
df_reshuffle=df.reindex(np.random.permutation(df.index)).reset_index().copy()
df_reshuffle.to_csv('/home/ale/Desktop/Portfolio/reshuffle.csv')

#%%
# Saving the list of Video ID for the crawler

#df_reshuffle.to_csv("test", sep="\t", quoting=csv.QUOTE_NONE)
#df_reshuffle.iloc[0:10,1].to_csv('/home/ale/Desktop/Portfolio/test',sep="/n")
np.savetxt(r'/home/ale/Desktop/Portfolio/test.txt',df_reshuffle.iloc[0:10,1].values, fmt='%s')

#%%
#Running the crawler
'''
import sys
sys.path.append('/home/ale/Desktop/Portfolio/YTCrawl-master')
from crawler import Crawler
c=Crawler()
c._crawl_delay_time = 1 # set crawling delay to 1
c._cookie_update_delay_time = 1 # set cookie updating delay to 1
c.batch_crawl("/home/ale/Desktop/Portfolio/test.txt", "/home/ale/Desktop/Portfolio/test")'''

#%%
#Creating the first 200 000 files
#import pandas as pd
#import numpy as np
#df_reshuffle= pd.read_csv('/home/ale/Desktop/Portfolio/reshuffle.csv',header=None)
np.savetxt(r'/home/ale/Desktop/Portfolio/secondbatch.txt',df_reshuffle.iloc[32899:99999,1].values, fmt='%s')


#%%

df_o = pd.read_csv('/home/ale/Desktop/Portfolio/firstbatch.txt',header=None)
df_n = pd.read_csv('/home/ale/Desktop/Portfolio/secondbatch.txt',header=None)