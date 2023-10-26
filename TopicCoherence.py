import math
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

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

# seeing the top words for each model on each corpus
def gtw(m,c,r):
    itw = atw[m][c][r]
    print(models[m])
    print('Corpus',c+1)
    print('Run',r+1)
    print(itw)
    
gtw(0,0,2)

# Graph for UMASS

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
