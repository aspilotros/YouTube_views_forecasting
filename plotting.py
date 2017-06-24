# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:03:17 2017

@author: Alessandro
"""
#%%
import matplotlib.pyplot as plt

patterns = df_views_norm_24m.iloc[419040:419050,0:730]
X=pd.Series(range(0,patterns.shape[1]))
for i in range(patterns.shape[0]):

    plt.plot(X, patterns.iloc[i,:])

plt.show()
#%%
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
patterns = df_views_norm_24m.iloc[0:100,0:-1]
X=pd.Series(range(0,patterns.shape[1]))
trace=list()
for i in range(patterns.shape[0]):
    trace.append( Scatter(
            x=X,
            y=patterns.iloc[i,:]
              ))

data = Data(trace)

plotly.offline.plot(data, filename = 'basic-line')