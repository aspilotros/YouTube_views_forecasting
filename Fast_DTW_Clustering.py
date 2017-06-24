# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:14:04 2017

@author: Alessandro
"""

#%%
# Fast Version of DTW
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw

#x=df_views_norm_24m.iloc[0,0:730]
#y=df_views_norm_24m.iloc[1,0:730]

#distance, path = fastdtw(x, y, dist=euclidean)
#print(distance)

def k_means_clust_fast(data,num_clust,num_iter,w=5):
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
                cur_dist, path = fastdtw(i,j,dist=euclidean)
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
    return centroids

train = df_views_norm_24m.iloc[190000:210000,0:30].values

import matplotlib.pylab as plt

centroids=k_means_clust_fast(train,4,10,4)
for i in centroids:

    plt.plot(i)

plt.show()