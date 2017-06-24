# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:32:36 2017

@author: Alessandro
"""
import pandas as pd
import pickle

#%% Loading Labels and reindexing according to Video Ids

labels = pd.read_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/yt8M_train_labels.csv", header=None)
labels_reindex = pd.DataFrame(labels.values,index=labels.iloc[:,0])
# Loading vocabulary for labels and cleaning it
colnames = pd.read_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/vocabulary.csv", header=None,nrows=1)
vocabulary = pd.read_csv("C:/Users/Alessandro/windows-share/Portfolio/DATA/vocabulary.csv", header=0, names=colnames.iloc[0,:])
vocabulary_simple=vocabulary.loc[:, ['Index', 'Vertical1', 'Vertical2', 'Vertical3', 'Name']]
pickle.dump(vocabulary_simple,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/vocabulary_simple.p",'wb'))
pickle.dump(labels_reindex,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/labels_reindex.p",'wb'))

# deleting variables not in use to save space in RAM

del labels
del vocabulary

#%%
###############################################################################
#########################   Batch 1
##############################################################################


batch1_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Firstbatch-IDs.p",'rb'))
batch2_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Secondbatch-IDs.p",'rb'))
batch3_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Thirdbatch-IDs.p",'rb'))
batch4_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Fourthbatch-IDs.p",'rb'))

batches=[batch1_dict, batch2_dict, batch3_dict, batch4_dict]

for batch in batches:
    for key in batch:
        labels_list=labels_reindex.loc[key][1].split(' ') # take the labels corresponding to video ID=key    
        batch[key]={'views':batch[key]}
        batch[key]['labels']=labels_list
             
# Merging batches and cleaning memory

for batch in batches:
    batches[0].update(batch)

for batch in batches[1:]:
    batch.clear()

# Saving the first quarter of data to a single dictionary
batch1 =  pickle.dump(batch1_dict,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/batch1.p",'wb'))
#%%
###############################################################################
#########################   Batch 2
##############################################################################

# Loading the batches for batch2

batch1_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Fifthbatch-IDs.p",'rb'))
batch2_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Sixthbatch-IDs.p",'rb'))
batch3_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Seventhbatch-IDs.p",'rb'))
batch4_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Eightbatch-IDs.p",'rb'))

batches=[batch1_dict, batch2_dict, batch3_dict, batch4_dict]

for batch in batches:
    for key in batch:
        labels_list=labels_reindex.loc[key][1].split(' ') # take the labels corresponding to video ID=key    
        batch[key]={'views':batch[key]}
        batch[key]['labels']=labels_list
             
# Merging batches and cleaning memory

for batch in batches:
    batches[0].update(batch)

for batch in batches[1:]:
    batch.clear()

# Saving the first quarter of data to a single dictionary
batch2 =  pickle.dump(batch1_dict,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/batch2.p",'wb'))

#%%
###############################################################################
#########################   Batch 3
##############################################################################

# Loading the batches for batch2

batch1_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Ninethbatch-IDs.p",'rb'))
batch2_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Tenthbatch-IDs.p",'rb'))
batch3_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Eleventhbatch-IDs.p",'rb'))
batch4_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Twelvebatch-IDs.p",'rb'))

batches=[batch1_dict, batch2_dict, batch3_dict, batch4_dict]

for batch in batches:
    for key in batch:
        labels_list=labels_reindex.loc[key][1].split(' ') # take the labels corresponding to video ID=key    
        batch[key]={'views':batch[key]}
        batch[key]['labels']=labels_list
             
# Merging batches and cleaning memory

for batch in batches:
    batches[0].update(batch)

for batch in batches[1:]:
    batch.clear()

# Saving the first quarter of data to a single dictionary
batch3 =  pickle.dump(batch1_dict,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/batch3.p",'wb'))

#%%
###############################################################################
#########################   Batch 4
##############################################################################

# Loading the batches for batch2

batch1_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Thirteenbatch-IDs.p",'rb'))
batch2_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Fourteenbatch-IDs.p",'rb'))
batch3_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Fifteenbatch-IDs.p",'rb'))
batch4_dict = pickle.load(open("C:/Users/Alessandro/windows-share/Portfolio/DATA/Sixteenbatch-IDs.p",'rb'))

batches=[batch1_dict, batch2_dict, batch3_dict, batch4_dict]

for batch in batches:
    for key in batch:
        labels_list=labels_reindex.loc[key][1].split(' ') # take the labels corresponding to video ID=key    
        batch[key]={'views':batch[key]}
        batch[key]['labels']=labels_list
             
# Merging batches and cleaning memory

for batch in batches:
    batches[0].update(batch)

for batch in batches[1:]:
    batch.clear()

# Saving the first quarter of data to a single dictionary
batch4 =  pickle.dump(batch1_dict,open("C:/Users/Alessandro/windows-share/Portfolio/DATA/batch4.p",'wb'))

