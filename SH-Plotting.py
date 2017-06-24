# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:51:27 2017

@author: Alessandro
"""
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
#%% Importing the data
df = pd.read_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_30d.csv")
#%%
df_cum = df.cumsum(axis=1)
#%% Plotting views on logarithmic scale
patterns = df_cum

X=patterns.iloc[0:500000:10,7].values
Y=patterns.iloc[0:500000:10,29].values

line_x = np.linspace(0.5, 50000000, 10000)
line_y = line_x
#np.corrcoef()
trace=list()
trace.append(
        Scatter(
                x=X,
                y=Y,
                mode="markers"
                )
        )

trace.append(
        Scatter(
                x=line_x,
                y=line_y,
#                mode="lines",
                line = dict(width = 2, dash= 'dash')
                )
        )

data = Data(trace)

layout = plotly.graph_objs.Layout(
    title = '1st week vs. 1st month',
    showlegend=False,
    font=dict(family='Cambria', size=18, color='#7f7f7f'),
    annotations=[
        dict(
            x=6,
            y=7.5,
            xref='x',
            yref='y',
            text='r = 0.96',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=0
        )
    ],
    xaxis=dict(
        type='log',
        autorange=True,
        title = "Popularity after 7 days",
    
    ),
    yaxis=dict(
        type='log',
        autorange=True,
        title = "Popularity after 30 days"
    )
)

fig = plotly.graph_objs.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename = 'SH-line')
