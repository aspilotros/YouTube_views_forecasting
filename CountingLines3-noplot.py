#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:54:35 2017

@author: ale
"""
#sys.stdout.write(frmt_date)

# Counting the number of lines in a file each 5 min
import time
import datetime as dt
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
import numpy as np


root1 = input('insert the complete path that hosts the output folder')
root2 = input('output folder name')

name = root1 + '/' + root2 + '/key.done'

    
name1 = root1 + '/' + root2 + 'key.disabled'

    
name2 = root1 + '/' + root2 + 'key.invalidrequest'


name3 = root1 + '/' + root2 + 'key.nostatyet'


name4 = root1 + '/' + root2 + 'key.notfound'


name5 = root1 + '/' + root2 + 'key.private'


name6 = root1 + '/' + root2 + 'key.quotalimit'

j=0

counts=[]
counts1=[]
counts2=[]
counts3=[]
counts4=[]
counts5=[]
counts6=[]

while True:
    
    handle = open(name, 'r')
    handle1 = open(name1, 'r')
    handle2 = open(name2, 'r')
    handle3 = open(name3, 'r')
    handle4 = open(name4, 'r')
    handle5 = open(name5, 'r')
    handle6 = open(name6, 'r')
    
    counts.append(0)
    counts1.append(0)
    counts2.append(0)
    counts3.append(0)
    counts4.append(0)
    counts5.append(0)
    counts6.append(0)
    
    for line in handle:
        counts[j]=counts[j]+1
    for line1 in handle1:
        counts1[j]=counts1[j]+1
    for line2 in handle2:
        counts2[j]=counts2[j]+1
    for line3 in handle3:
        counts3[j]=counts3[j]+1
    for line4 in handle4:
        counts4[j]=counts4[j]+1
    for line5 in handle5:
        counts5[j]=counts5[j]+1
    for line6 in handle6:
        counts6[j]=counts6[j]+1
        
    total=counts[j]+counts1[j]+counts2[j]+counts3[j]+counts4[j]+counts5[j]+counts6[j]
    epoch_now = time.time()
    frmt_date = dt.datetime.utcfromtimestamp(epoch_now)
    frmt_date=frmt_date+dt.timedelta(hours=2)
    frmt_date = frmt_date.strftime("%Y/%m/%d %H:%M")
    
    #plt.plot(epoch_now,counts, 'r--', counts1, 'b--', counts2, 'g--', counts3, 'rs', counts4, 'bs', counts5, 'gs', counts6, 'r^')
    #plt.show()
    # Create traces
    
    
    print (
            'line in file = ',counts[j],'time = ' ,frmt_date, ' out of total =', total,'/n',  
            'done ',counts[j],' disabled ',counts1[j],' invalidreq',counts2[j],' notstatyet ',counts3[j],' notfound ',counts4[j],' private ',counts5[j],' quotalimit ',counts6[j])
    
    
    
    
    
    #plotting each 12 cycles i.e. each 12*300sec=each hour
    '''   
    if j % 12 == 11:
    
        trace0 = go.Scatter(
            x = np.arange(j),
            y = counts,
            mode = 'markers',
            name = 'done'
        )
        trace1 = go.Scatter(
            x = np.arange(j),
            y = counts1+counts2+counts3+counts4+counts5,
            mode = 'markers',
            name = 'key not available'
        )
        trace2 = go.Scatter(
            x = np.arange(j),
            y = counts6,
            mode = 'lines',
            name = 'quotalimit'
        )
        data = [trace0, trace1, trace2]
        py.offline.plot({
        "data": data,
        "layout": go.Layout(title="Crawler Stats")
        })
    '''
    j=j+1

    time.sleep(300)
