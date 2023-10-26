import math
import numpy as np
import os
import matplotlib.pyplot as plt
import bitermplus as btm
import pandas as pd
from matplotlib.transforms import Affine2D

cortest = 'c1'
tststs = cortest+'.topwords'

# Change current directory to get corpora
print(os.getcwd())
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2')

ds = []

for i in range(0,6):
    ii = i+1
    ci = 'c'+str(ii)
    cori = 'Cor'+str(ii)+'b.txt'
    ci = open(cori)
    ds.append([d.split() for d in ci])
    
cl = open('LargeCor.txt')
ds.append([d.split() for d in cl])
cl2 = open('LargeCor2.txt')
ds.append([d.split() for d in cl2])
cl3 = open('LargeCor3.txt')
ds.append([d.split() for d in cl3])
cl4 = open('LargeCor4.txt')
ds.append([d.split() for d in cl4])

"""
c1 = open('Cor1b.txt')
d1 = [d.split() for d in c1]
c2 = open('Cor2b.txt')
d2 = [d.split() for d in c2]
c3 = open('Cor3b.txt')
d3 = [d.split() for d in c3]
c4 = open('Cor4b.txt')
d4 = [d.split() for d in c4]
c5 = open('Cor5b.txt')
d5 = [d.split() for d in c5]
c6 = open('Cor6b.txt')
d6 = [d.split() for d in c6]

ds = [d1,d2,d3,d4,d5,d6]
"""

# Change current directory to get top words
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/results')

ms = ['LDA','BTM','GPU','DMM']
runs = ['a','b','c']
atwpmi = [[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
          [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]]

ending = ['.topWords','.topWords.Coherence']

for ii in range(0,2):
    
    endi = ending[ii]
    
    for i in range(0,4): # Model
    
        cm = ms[i]
    
        for l in range(0,10): # Corpus
        
            if l<6:
                ll = l+1
            
            mtw = []
        
            for k in range(0,3): # Run
                
                if l<6:
    
                    twi = 'c'+str(ll)+cm+'40'+runs[k]+endi
                    ci = open(twi)
                    mtw.append([d.split() for d in ci])
                
                else:
                
                    lci=l-6
                    lcs=['Lc','Lc2','Lc3','Lc4']
                
                    if l>7:
                        runsb = ['','a','b']
                        twi = lcs[lci]+cm+'40'+runsb[k]+endi
                        ci = open(twi)
                        mtw.append([d.split() for d in ci])
                
                    else:
                        runsb = ['a','b','c'] # Only GPU is ''
                        twi = lcs[lci]+cm+'40'+runsb[k]+endi
                        ci = open(twi)
                        mtw.append([d.split() for d in ci])
                
                
        
            atwpmi[ii][i][l] = mtw
            
atw = atwpmi[0]
apmi = atwpmi[1]
apmi2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

for i in range(0,4):
    
    for k in range(0,10):
        
        runs = []
        
        for l in range(0,3):
            
            ind = float(apmi[i][k][l][3][1])
            runs.append(ind)
            
        apmi2[i][k] = runs
            


"""
# All LDA
LDA1 = open('c1LDA40.topWords')
LDA1 = [d.split() for d in LDA1]
LDA2 = open('c2LDA40.topWords')
LDA2 = [d.split() for d in LDA2]
LDA3 = open('c3LDA40.topWords')
LDA3 = [d.split() for d in LDA3]
LDA4 = open('c4LDA40.topWords')
LDA4 = [d.split() for d in LDA4]
LDA5 = open('c5LDA40.topWords')
LDA5 = [d.split() for d in LDA5]
LDA6 = open('c6LDA40.topWords')
LDA6 = [d.split() for d in LDA6]

LDAS = [LDA1,LDA2,LDA3,LDA4,LDA5,LDA6]


# All BTM
BTM1 = open('c1BTM40.topWords')
BTM1 = [d.split() for d in BTM1]
BTM2 = open('c2BTM40.topWords')
BTM2 = [d.split() for d in BTM2]
BTM3 = open('c3BTM40.topWords')
BTM3 = [d.split() for d in BTM3]
BTM4 = open('c4BTM40.topWords')
BTM4 = [d.split() for d in BTM4]
BTM5 = open('c5BTM40.topWords')
BTM5 = [d.split() for d in BTM5]
BTM6 = open('c6BTM40.topWords')
BTM6 = [d.split() for d in BTM6]

BTMS = [BTM1,BTM2,BTM3,BTM4,BTM5,BTM6]

# All GPU
GPU1 = open('c1GPU40.topWords')
GPU1 = [d.split() for d in GPU1]
GPU2 = open('c2GPU40.topWords')
GPU2 = [d.split() for d in GPU2]
GPU3 = open('c3GPU40.topWords')
GPU3 = [d.split() for d in GPU3]
GPU4 = open('c4GPU40.topWords')
GPU4 = [d.split() for d in GPU4]
GPU5 = open('c5GPU40.topWords')
GPU5 = [d.split() for d in GPU5]
GPU6 = open('c6GPU40.topWords')
GPU6 = [d.split() for d in GPU6]

GPUS = [GPU1,GPU2,GPU3,GPU4,GPU5,GPU6]
"""

# Function for UMASS
def gch(cp,tpw):
    ch = []
    ntw = len(tpw)
    ndoc = len(cp)

    for t in range(0,ntw): #calculate coherence
               
        for vj in range(0,10): #each word in topic t
          
            Dvj = 0
            for d in range(0,ndoc): 
                if (tpw[t][vj] in cp[d]): #check how many docs contain word vj
                    Dvj += 1
                
            for vi in range(0,vj): 
                Dvjvi = 0
                for d in range(0,ndoc): 
                
                    if (tpw[t][vj] in cp[d]) and (tpw[t][vi] in cp[d]): #check how many docs contain both word vj and vi
                        Dvjvi += 1
            
                ch.append(math.log((Dvjvi+1)/float(Dvj),10))

    avch = np.sum(ch)/ntw
    return avch

allch = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

for j in range(0,4): # Model
    
    for i in range(0,10): # Corpus
        
        chk = []
    
        for k in range(0,3): # Run
            
            chk.append(gch(ds[i],atw[j][i][k]))
            
        allch[j][i] = chk

"""
allch.append([[-39.6587,-41.4597,-42.4704], [-41.7674,-39.5738,-40.3185], [-39.9997,-41.9912,-41.7366], 
              [-39.913,-40.0562,-39.4353], [-38.978,-40.1816,-38.2071], [-38.553,-38.2077,-37.8107], 
              [-34.9734,-35.5518,-36.108], [-35.9981,-34.8726,-34.0047]])
"""


means = []
maxes = []
mins = []
diffs = []
maxdiffs = []
mindiffs = []

for i in range(0,4):
    
    means.append([np.mean(a) for a in allch[i]])
    maxes.append([np.max(a) for a in allch[i]])
    mins.append([np.min(a) for a in allch[i]])
    maxdiffs.append([abs(np.max(a)-np.mean(a)) for a in allch[i]])
    mindiffs.append([abs(np.min(a)-np.mean(a)) for a in allch[i]])


# Getting PMI
os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/results')



models = ['LDA','BTM','GPU','DMM']

# seeing the top words for each model on each corpus
def gtw(m,c,r):
    itw = atw[m][c][r]
    print(models[m])
    print('Corpus',c+1)
    print('Run',r+1)
    print(itw)
    
gtw(0,0,2)

# Graph for UMASS
#003f5c
#7a5195
#ef5675
#ffa600

x = range(1,11)
fig, ax = plt.subplots()
# LDA
ax.plot(x,means[0],label='LDA',color='darkorange')
ax.errorbar(x,means[0],yerr=[mindiffs[0],maxdiffs[0]],color='darkorange',capsize=3)
# BTM
ax.plot(x,means[1], label='BTM',color='mediumseagreen')
ax.errorbar(x,means[1],yerr=[mindiffs[1],maxdiffs[1]],color='mediumseagreen',capsize=3)
# GPU-PDMM
ax.plot(x,means[2], label='GPU-PDMM',color='cornflowerblue')
ax.errorbar(x,means[2],yerr=[mindiffs[2],maxdiffs[2]],color='cornflowerblue',capsize=3)
# GSDMM
ax.plot(x,means[3], label='GSDMM',color='orchid')
ax.errorbar(x,means[3],yerr=[mindiffs[3],maxdiffs[3]],color='orchid',capsize=3)
ax.legend()
plt.xticks(np.arange(1,11))
plt.xlabel('Corpus')
plt.ylabel('Topic coherence (UMASS)')

os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Figures')
plt.savefig('Poster_UMASS.png', dpi=300, bbox_inches='tight')
#plt.savefig('UMASS_with_8_Corpora.png', dpi=300, bbox_inches='tight')
plt.show()


# Graph for PMI

"""
pmi = np.transpose([[0.6448,0.8665,1.0232,0.9795],
                    [0.6302,0.9521,0.9649,0.9992],
                    [0.5425,0.8820,0.9111,0.9200],
                    [0.5227,0.7401,0.8170,0.9096],
                    [0.4866,0.7692,0.7562,0.8882],
                    [0.4867,0.8094,0.6832,0.8568],
                    [0.5623,0.7251,0.6362,0.5629],
                    [0.5513,0.5655,0.4959,0.4514],
                    [0.6790,0.5832,0.6939,0.5810]])
"""

pmi = apmi2

pmeans = []
pmaxes = []
pmins = []
pdiffs = []
pmaxdiffs = []
pmindiffs = []

for i in range(0,4):
    
    pmeans.append([np.mean(a) for a in pmi[i]])
    pmaxes.append([np.max(a) for a in pmi[i]])
    pmins.append([np.min(a) for a in pmi[i]])
    pmaxdiffs.append([abs(np.max(a)-np.mean(a)) for a in pmi[i]])
    pmindiffs.append([abs(np.min(a)-np.mean(a)) for a in pmi[i]])

“#7eb0d5”, “#b2e061”, “#bd7ebe”, “#ffb55a”

x = range(1,11)
fig, ax = plt.subplots()
# LDA
ax.plot(x,pmeans[0], label='LDA',color='darkorange')
ax.errorbar(x,pmeans[0],yerr=[pmindiffs[0],pmaxdiffs[0]],color='darkorange',capsize=3)
# BTM
ax.plot(x,pmeans[1], label='BTM',color='mediumseagreen')
ax.errorbar(x,pmeans[1],yerr=[pmindiffs[1],pmaxdiffs[1]],color='mediumseagreen',capsize=3)
# GPU-PDMM
ax.plot(x,pmeans[2], label='GPU-PDMM',color='cornflowerblue')
ax.errorbar(x,pmeans[2],yerr=[pmindiffs[2],pmaxdiffs[2]],color='cornflowerblue',capsize=3)
# GSDMM
ax.plot(x,pmeans[3], label='GSDMM',color='orchid')
ax.errorbar(x,pmeans[3],yerr=[pmindiffs[3],pmaxdiffs[3]],color='orchid',capsize=3)

ax.legend()
plt.xticks(np.arange(1,11))
plt.xlabel('Corpus')
plt.ylabel('Topic coherence (PMI)')

os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Figures')
plt.savefig('Poster_PMI.png', dpi=300, bbox_inches='tight')
#plt.savefig('PMI_with_8_Corpora.png', dpi=300, bbox_inches='tight')
plt.show()


pmipaste = list(np.around(np.array(np.transpose(pmeans)),4))
