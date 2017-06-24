# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:56:32 2017

@author: Alessandro
"""

import pandas as pd
import numpy as np
import pickle
import h5py
#%%

df_views_1= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch1_views.p",'rb'))
df_views_2= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch2_views.p",'rb'))
df_views_3= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch3_views.p",'rb'))
#%%
df_views_4= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch4_views.p",'rb'))
#%%
list_df_views=[df_views_1, df_views_2, df_views_3]

df_views_24m=pd.concat(list_df_views)
#%%
pickle.dump(df_views_24m,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_24m.p",'wb'))

#%%
df_tags_1= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch1_tags.p",'rb'))
df_tags_2= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch2_tags.p",'rb'))
df_tags_3= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch3_tags.p",'rb'))
#%%
df_tags_4= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_batch4_tags.p",'rb'))
#%%
list_df_tags=[df_tags_1, df_tags_2, df_tags_3]
df_tags_24m=pd.concat(list_df_tags)
#%%
pickle.dump(df_tags_24m,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_tags_24m.p",'wb'))
#%%
df= pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_24m.p",'rb'))
#%%
df.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_24m.csv')

