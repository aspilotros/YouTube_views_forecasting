# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 23:10:32 2017
Goal: Forecasting YouTube video view counts based on history of visualization 
Implement SH model, ML model, Pop model, Altman model


@refer_d The pivot date: before view counts are known, after not
@target_d The view counts before target_d to be predicted

@author: Alessandro

"""
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from sklearn.model_selection import train_test_split
#%%
df=pd.read_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/df_views_30d.csv",header=0)
df=df.iloc[:,1:]
#%% Splitting train and test
train, test = train_test_split(df, test_size=0.3, random_state = 12)
#%%
def SHModel(train, test, refer_d, target_d):
#    train=pd.read_csv(open(train, "rb"))
#    test=pd.read_csv(open(test, "rb"))
    train_x=train.iloc[:,0:refer_d].values
    train_y=train.iloc[:,0:target_d].values
    test_x=test.iloc[:,0:refer_d].values
    test_y=test.iloc[:,0:target_d].values
    
    alpha = 0
    sum1 = 0
    sum2 = 0
    """
        calculate alpha
        According S-H model: alpha * N(refer_d) = N(target_d)
    """
    for i in range(train_x.shape[0]):
        sum1 = sum1 +( sum(train_x[i]) / sum(train_y[i]) )
        sum2 = sum2 +( sum(train_x[i]) / sum(train_y[i]) ) ** 2
#        print("i:",i)
    
    alpha = sum1 / sum2
    print("alpha:", alpha)
    """
        calculate mRSE
    """
    RSE = []
    predictions = []
    for i in range(test_x.shape[0]):
        predictions.append(alpha * sum(test_x[i]))
#        RSE += ( (alpha * sum(test_x[i]) / sum(test_y[i])) - 1) ** 2
        RSE.append( ( (predictions[i] / sum(test_y[i])) - 1) ** 2)
#        print("i:",i)
    mRSE = sum(RSE)/test_x.shape[0]
    std = np.std(RSE)
    
    print("test_x shape", test_x.shape)
    print("test_y shape", test_y.shape)
    print("train_x shape", train_x.shape)
    print("train_y shape", train_y.shape)
    return predictions, mRSE, std, RSE
#%%
def MLmRSE(alpha, x, y):
    return (np.dot(alpha, x) / y - 1)


def MLModel(train, test, refer_d, target_d):
    train_x=train.iloc[:,0:refer_d].values
    train_y=np.sum(train.iloc[:,0:target_d].values,axis=1)
    test_x=test.iloc[:,0:refer_d].values
    test_y=np.sum(test.iloc[:,0:target_d].values, axis=1)
    """
        According M-L model: alpha1*day1 + ... + alphan*dayn = N(target_d)
        get alpha by using leastsq
    """
    alpha = [0] * train_x.shape[1]
    x     = np.transpose(np.array(train_x))
    y     = np.array(train_y)
    alpha = leastsq(MLmRSE, alpha, args = (x, y))[0]
    """
        calculate mRSE
    """
    RSE = []
    predictions = []
#    RSE = 0
    for i in range(test_x.shape[0]):
#        RSE += ((np.dot(alpha, test_x[i]) / test_y[i]) - 1) ** 2
        predictions.append(np.dot(alpha, test_x[i]))
        RSE.append( ((predictions[i] / test_y[i])-1)**2 )
    mRSE = sum(RSE) / test_x.shape[0]
    std = np.std(RSE)
    return predictions, mRSE, std, RSE
#%%
def MyModel(train, test, refer_d, target_d):
    
    return None