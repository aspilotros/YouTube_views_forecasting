# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:57:30 2017

@author: Alessandro
"""

#%%
import pickle
import numpy as np
import pandas as pd
#%% Importing data

#%%
def LB_Keogh(s1,s2,r):
    LB_sum=0
    for ind,i in enumerate(s1):

        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])

        if i>upper_bound:
            LB_sum=LB_sum+(i-upper_bound)**2
        elif i<lower_bound:
            LB_sum=LB_sum+(i-lower_bound)**2

    return sqrt(LB_sum)
#%%

def DTWDistance(s1, s2,w):
    DTW={}

    w = max(w, abs(len(s1)-len(s2)))

    for i in range(-1,len(s1)):
        for j in range(-1,len(s2)):
            DTW[(i, j)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(max(0, i-w), min(len(s2), i+w)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return sqrt(DTW[len(s1)-1, len(s2)-1])

def k_means_clust(data,num_clust,num_iter,w=5):
    centroids = data[np.random.choice(data.shape[0], num_clust, replace=False)]
    #centroids=random.sample(data,num_clust)
    #centroids=data.sample(num_clust)
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
                if LB_Keogh(i,j,5)<min_dist:
                    cur_dist=DTWDistance(i,j,w)
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
centroids, assignments=k_means_clust(train_3M_rb.values,4,10,4)
#%% Plotting Centroids
import matplotlib.pylab as plt
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
patterns = pd.DataFrame(centroids)
X=pd.Series(range(0,patterns.shape[1]))
trace=list()
for i in range(patterns.shape[0]):
    trace.append( Scatter(
            x=X,
            y=patterns.iloc[i,:]
              ))

data = Data(trace)

plotly.offline.plot(data, filename = 'basic-line')


#%%
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
train = df_views_norm_24m.iloc[0::20,0:30].values

np.random.seed(0)

n_clusters=4
avg_dist = np.zeros((n_clusters, n_clusters))

metric="cityblock"
model = AgglomerativeClustering(n_clusters=n_clusters,
                                linkage="average", affinity=metric)
model.fit(train)
#%%
plt.figure()
plt.axes([0, 0, 2, 2])

for l, c in zip(np.arange(model.n_clusters), 'rgbk'):
    plt.plot(train[model.labels_ == l].T, c=c, alpha=.5)

plt.axis('tight')
plt.axis('off')
plt.suptitle("AgglomerativeClustering(affinity=%s)" % metric, size=20)
plt.show()