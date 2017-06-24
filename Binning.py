# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:25:56 2017
The goal of this code is to 
     - rebin the dataset of views to the desired bin size
     - normalize after binning to the Total sum of views
@author: Alessandro
"""
import pickle
import numpy as np
import pandas as pd
#%%
def binning(data, bin):
    """Rebinning Dataframe averaging together bin columns per time"""   
    i=0
    data_bin=pd.DataFrame(
            np.zeros(
                    data.shape[0]*int(data.shape[1]/bin)
                    ).reshape(
                            data.shape[0],int(data.shape[1]/bin)
                            )
                    )
#    print("data_bin_shape", data_bin.shape)       
    while i<data_bin.shape[1]:
        j=i+1
        data_bin.iloc[:,i]=np.sum(data.iloc[:,(i*bin):(j*bin)].values, axis=1)
#        
#
        i=i+1
        
    return pd.DataFrame(data_bin)

def normalization(x):
    return x.div(np.sum(x,axis=1), axis=0)
#%% Loading the dataset for video views

file = open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_24m.p",'rb')
df_views_24m = pickle.load(file)
file.close()
#%% Rebinning
df_views_30d = df_views_24m.iloc[:,0:30]
df_views_3m = binning(df_views_24m.iloc[:,0:90], 3)
df_views_6m = binning(df_views_24m.iloc[:,0:180], 6)
df_views_1y = binning(df_views_24m.iloc[:,0:360], 12)
#%% Normalizing
df_views_norm_24m = normalization(df_views_24m.iloc[:,:-1])
df_views_30d_norm = normalization(df_views_30d)
df_views_3m_norm = normalization(df_views_3m)
df_views_6m_norm = normalization(df_views_6m)
df_views_1y_norm = normalization(df_views_1y)
#%%
pickle.dump(df_views_norm_24m, open( "df_views_norm_24m.p", "wb" ))
pickle.dump(df_views_30d_norm, open( "df_views_30d_norm.p", "wb" ))
pickle.dump(df_views_3m_norm, open( "df_views_3m_norm.p", "wb" ))
pickle.dump(df_views_6m_norm, open( "df_views_6m_norm.p", "wb" ))
pickle.dump(df_views_1y_norm, open( "df_views_1y_norm.p", "wb" ))
#%%
df_views_30d.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_30d.csv')
df_views_30d_norm.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_30d_norm.csv')
#%%
df_views_3m.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_3m.csv')
df_views_3m_norm.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_3m_norm.csv')
#%%
df_views_6m.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_6m.csv')
df_views_6m_norm.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_6m_norm.csv')
#%%
df_views_1y.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_1y.csv')
df_views_1y_norm.to_csv('C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_1y_norm.csv')
#%%
file = open("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_tags_24m.p",'rb')
df_tags_24m = pickle.load(file)
file.close()
#%%
df_tags_24m.to_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_tags_24m.csv")
#%%
df_views_norm_24m.to_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_norm_views_24m.csv")

