import math
import numpy as np
import os
import matplotlib.pyplot as plt
import bitermplus as btm
import pandas as pd

# Change current directory to get corpora
print(os.getcwd())
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2')

ds = []

for i in range(0,6):
    ii = i+1
    ci = 'c'+str(ii)
    cori = 'Cor'+str(ii)+'b.txt'
    ci = open(cori)
    ds.append(ci.readlines())
    
cl = open('LargeCor.txt')
ds.append(cl.readlines())
cl2 = open('LargeCor2.txt')
ds.append(cl2.readlines())
cl3 = open('LargeCor3.txt')
ds.append(cl3.readlines())

# Function for BTM
def btmfun(dl,i):
    
    # PREPROCESSING
    # Obtaining terms frequency in a sparse matrix and corpus vocabulary
    X, vocabulary, vocab_dict = btm.get_words_freqs(dl)
    tf = np.array(X.sum(axis=0)).ravel()
    # Vectorizing documents
    docs_vec = btm.get_vectorized_docs(dl, vocabulary)
    docs_lens = list(map(len, docs_vec))
    # Generating biterms
    biterms = btm.get_biterms(docs_vec)
    # INITIALIZING AND RUNNING MODEL
    model = btm.BTM(
        X, vocabulary, seed=i, T=40, M=10, alpha=0.1, beta=0.01)
    model.fit(biterms, iterations=15)
    p_zd = model.transform(docs_vec)

    # METRICS
    perplexity = btm.perplexity(model.matrix_topics_words_, p_zd, X, 8)
    coherence = btm.coherence(model.matrix_topics_words_, X, M=10)
    # or
    perplexity = model.perplexity_
    coherence = np.mean(model.coherence_)

    # LABELS
    lab = model.labels_
    # or
    btm.get_docs_top_topic(dl, model.matrix_docs_topics_)
    topw = btm.get_top_topic_words(model,10)
    topw = np.transpose(topw)

    topwl = topw.values.tolist()
    
    return topwl


os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/results')
btmtw = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
ri = ['','a','b']
mn = ['c1','c2','c3','c4','c5','c6','Lc','Lc2','Lc3']

# Saving top words
for mi in range(0,9):
    
    ri = ['a','b','c']
    
    if mi==8:
        
        ri = ['','a','b']
    
    for i in range(0,3):   

        topwli = btmfun(ds[mi],i)
    
        btmtw[mi][i] = topwli
        runname = mn[mi]+'BTM40'+ri[i]+'.topWords'
        open('runname', 'w').close()
        # Creating corpus
        with open(runname, 'w') as f:
            for line in topwli:
                line = ' '.join(line)
                f.write(line)
                f.write('\n')

# BTM on Lc4
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2')
with open('LargeCor4.txt') as dl4:
    dl4 = dl4.readlines()
    
ri = ['','b']

for i in range(0,2):    
    
    btm_tw_Lc4 = btmfun(dl4,i)

    os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/results')

    with open('Lc4BTM40'+ri[i]+'.topWords', 'w') as f:
        for line in btm_tw_Lc4:
            line = ' '.join(line)
            f.write(line)
            f.write('\n')   
