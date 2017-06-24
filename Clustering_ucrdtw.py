# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:18:29 2017
Knn Clustering with the ucrdtw method from the paper
 
Thanawin Rakthanmanon, Bilson Campana, Abdullah Mueen, Gustavo Batista, 
Brandon Westover, Qiang Zhu, Jesin Zakaria, Eamonn Keogh (2012). 
Searching and Mining Trillions of Time Series Subsequences under Dynamic 
Time Warping SIGKDD 2012.

Usage

import _ucrdtw
import numpy as np
import matplotlib.pyplot as plt

data = np.cumsum(np.random.uniform(-0.5, 0.5, 1000000))
query = np.cumsum(np.random.uniform(-0.5, 0.5, 100))
loc, dist = _ucrdtw.ucrdtw(data, query, 0.05, True)
query = np.concatenate((np.linspace(0.0, 0.0, loc), query)) + (data[loc] - query[0])

plt.figure()
plt.plot(data)
plt.plot(query)
plt.show()

@author: Alessandro
"""
import sys
sys.path.append('/media/sf_windows-share/Portfolio/ucrdtw-master')
import _ucrdtw
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp

import matplotlib.pylab as plt
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
#%% Importing data
df = pd.read_csv("/media/sf_windows-share/Portfolio/DATA/df_views_30d_norm.csv")
#%% Calculating the cumulative sum
df.iloc[:,0]=0
df_30d_cum=df.iloc[:,:].cumsum(axis=1)

#%%
def UCR_DTW_Distance(data, query,w=0.05, logic=True):
    loc, dist = _ucrdtw.ucrdtw(data, query, w, logic)
    return loc, dist
#%%
def k_means_clust(data,num_clust,num_iter,w=0.05):
    centroids = data[np.random.choice(data.shape[0], num_clust, replace=False)]
    counter=0
    for n in range(num_iter):
        counter+=1
        print (counter)
        assignments={}
        #assign data points to clusters
        for ind,i in enumerate(data):
        #for ind,i in data.iterrows():
            min_dist=float('inf')
            closest_clust=None
            for c_ind,j in enumerate(centroids):
                cur_dist=UCR_DTW_Distance(i,j,w,True)[1]
                if cur_dist<min_dist:
                    min_dist=cur_dist
                    closest_clust=c_ind
            if closest_clust in assignments:
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[]

        #recalculate centroids of clusters
        for key in assignments:
            clust_sum=np.array([0])
            for k in assignments[key]:
                clust_sum=clust_sum+data[k]
            #centroids[key]=[m/len(assignments[key]) for m in clust_sum]
            centroids[key] = clust_sum/len(assignments[key])
    return centroids, assignments 
#%%
centroids, assignments=k_means_clust(
        df_30d_cum.iloc[:,:].values, num_clust = 6, num_iter = 10, w = 0.05
        )
#%% Plotting Centroids
patterns = pd.DataFrame(centroids)
X=pd.Series(range(0,patterns.shape[1]))
trace=list()
for i in range(patterns.shape[0]):
    trace.append( Scatter(
            x=X,
            y=patterns.iloc[i,:]
              ))
trace.append(Scatter(x=X, y=df_30d_cum.iloc[20,:]))
data = Data(trace)
plotly.offline.plot(data, filename = 'basic-line')
#%%
pickle.dump(centroids, open("/media/sf_windows-share/Portfolio/DATA/centroids_30d_cum.p",'wb'))
pickle.dump(assignments, open("/media/sf_windows-share/Portfolio/DATA/assignments_30d_cum.p",'wb'))