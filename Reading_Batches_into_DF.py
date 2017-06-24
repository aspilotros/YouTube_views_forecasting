# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:07:12 2017

@author: Alessandro
"""

import pandas as pd
import numpy as np
import pickle
#%%
name=input ("input batch name in pickle format:")
batch1 = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/" + name + ".p",'rb'))

batch1_24m_views = dict()
batch1_24m_tags = dict()
for key in batch1:
    if len(batch1[key]["views"])>=730:
        batch1_24m_tags[key]={"labels": batch1[key]["labels"][0]}
        batch1_24m_views[key]={"views":batch1[key]["views"][0:730]}
# Cleaning memory
batch1.clear()
# Saving into Pandas dataframes
df_batch1_views=pd.DataFrame.from_dict(batch1_24m_views, orient='index')
df_batch1_views_IDs = pd.DataFrame(df_batch1_views.index)
df_batch1_views = pd.DataFrame( 
        np.concatenate(
                df_batch1_views.iloc[:,0].values
                                    ).reshape(df_batch1_views.shape[0], 730)
        )
df_batch1_views['IDs']=df_batch1_views_IDs
#
pickle.dump(df_batch1_views,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_" + name +"_views.p",'wb'))
#
batch1_24m_views.clear()
# Same procedure for tags
df_batch1_tags=pd.DataFrame.from_dict(batch1_24m_tags, orient='index')
df_batch1_tags_IDs = pd.DataFrame(df_batch1_tags.index)

df_batch1_tags["IDs"]=df_batch1_tags.index
df_batch1_tags.reset_index(inplace=True, drop=True)

# Creating tags from vocabulary
vocabulary_simple=pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/vocabulary_simple.p",'rb'))
#
j=0
count=0
for tags in df_batch1_tags["labels"]:
    df_batch1_tags.set_value(j,"labels",vocabulary_simple["Vertical1"][int(tags)])
    j=j+1
    print (count)
    count = count + 1
#
batch1_24m_tags.clear()
#
pickle.dump(df_batch1_tags,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_" + name +"_tags.p",'wb'))


