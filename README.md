# How Short Is Short

We conducted research to estimate an upper bound for short text lengths in short text topic modelling. Three short text topic models and LDA were run on ten corpora. The code used to create the data is available [here](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/CorporaCreation.py). The BTM was [implemented](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/BTM.py) in Python using the [bitermplus](https://pypi.org/project/bitermplus/) package. The GPU-PDMM, GSDMM, and LDA were implemented using the [implementation](https://github.com/qiang2100/STTM) by Qiang *et al.*. UMASS topic coherence was calculated using [this code](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/TopicCoherence.py). We include here the top words found by the best and worst performing models on each dataset.

[Corpus 1](www.google.com) <br/>
[Corpus 2](www.google.com) <br/>
[Corpus 3](www.google.com) <br/>
[Corpus 4](www.google.com) <br/>
[Corpus 5](www.google.com) <br/>
[Corpus 6](www.google.com) <br/>
[Corpus 7](www.google.com) <br/>
[Corpus 8](www.google.com) <br/>
[Corpus 9](www.google.com) <br/>
[Corpus 10](www.google.com) <br/>

We also created word clouds for each topic using [this code](this).
