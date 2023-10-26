import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os



# Word clouds for all topics

c6b = open('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2/LargeCor4.txt')
d6b = [d for d in c6b]
t6b = open('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Code/CreateCorp2/C6tb.txt')
td6b = [int(d) for d in t6b]


os.chdir('/Users/keeganstlegerdenny/Documents/Postgraduate/ResearchReport/Figures')

for i in range(1,40):
    
    sd6 = [d6b[l] for l in range(0,1944) if td6b[l] == 15]
    # 1
    # 36
        
    d6bt = ''.join(sd6)
    
    #wc = WordCloud(max_words=150,background_color='white',colormap='viridis').generate(d6bt)
    wc = WordCloud(max_words=150,background_color='white',colormap='YlGn',contour_color='red').generate(d6bt)
    plt.figure(dpi=300)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("wc_C6_T"+str(i)+".png",bbox_inches='tight')
    plt.savefig("WC_poster_2.png",bbox_inches='tight')
    plt.show()
