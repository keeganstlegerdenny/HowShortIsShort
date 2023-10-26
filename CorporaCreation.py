import wikipedia
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import random as rd
import collections
import nltk.data
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import random
import pandas as pd
import gensim
from gensim import corpora, models
import math
import os

nltk.download('stopwords')

from nltk.corpus import stopwords

stopwords = stopwords.words('english')

from string import punctuation

punctuation = list(punctuation)

stemmer = WordNetLemmatizer()

# Data cleaning function
def clean(ss):
    
     newdoc = []
     alllens = []
     topn = []

     ds = re.sub(r'\W', ' ', str(ss))

     ds = re.sub(r'\s+[a-zA-Z]\s+', ' ', ds)

     ds = re.sub(r'\^[a-zA-Z]\s+', ' ', ds)

     ds = re.sub(r'\s+', ' ', ds, flags=re.I)

     ds = re.sub(r'^b\s+', '', ds)

     ds = ds.lower()

     tokens = ds.split()
     tokens = [stemmer.lemmatize(word) for word in tokens]
     tokens = [token for token in tokens if token not in stopwords and token not in punctuation]
     tokens = [word for word in tokens if len(word)  > 4]
     
 
     st = ' '.join(tokens)

     wordcount = collections.Counter(tokens)

     ts.append(tokens)
     alllens.append(len(tokens))
     newdoc.append(st)
     
     if st != '':
         topn.append(tn+1)
         
     return ds, wordcount, ts, alllens, newdoc, topn, tokens

# 39 topics
topics = ['Academic disciplines', 'Business', 'Communication', 'Concepts', 'Culture', 'Economy', 'Education', 'Energy',
'Engineering', 'Entertainment', 'Entities', 'Ethics', 'Food and drink', 'Geography', 'Government', 'Health',
'History', 'Human behavior', 'Humanities', 'Information', 'Internet', 'Knowledge', 'Language', 'Law', 'Life‎',
'Mass media', 'Mathematics', 'Military', 'Nature', 'People', 'Philosophy', 'Politics', 'Religion', 'Science',
'Society', 'Sports', 'Technology', 'Time', 'Universe']

ts = []

tn = 0

cs = []

for l in topics:
    
    tn = tn+1
    
    tops = wikipedia.search(l, results=50) # Take first 50 results

    for i in tops:
        
        try:
            bti = wikipedia.page(i, auto_suggest=False).content
        except wikipedia.DisambiguationError as e:
            s = e.options[1]
            try:
                bti = wikipedia.page(s, auto_suggest=False).content
            except wikipedia.DisambiguationError as e2:
                    s2 = e2.options[1]
                    #s2 = random.choice(e2.options) # Cause of the differing lengths
                    bti = wikipedia.page(s2, auto_suggest=False).content
            except wikipedia.PageError:
                continue
 
        document = bti
        test = nltk.sent_tokenize(document)

        stemmer = WordNetLemmatizer()

        ci = ' '.join(test[0:5]) # Change depending on how many sentences
        ci = clean(ci)[4][0]          
        cs.append(ci)

# Some statistics for the data
cssplit = [d.split() for d in cs]
cslen = [len(i) for i in cssplit]
csmean = np.mean(cslen)
plt.hist(cslen)
np.percentile(cslen,75)
lamml = [min(cslen), max(cslen), np.mean(cslen), np.std(cslen)]
    
cs = [' '.join(i) for i in cs]

# Creating corpus
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2')
with open('LargeCor4.txt', 'a') as f: # Change name if new corpus
    for line in cs:
        f.write(line)
        f.write('\n')
