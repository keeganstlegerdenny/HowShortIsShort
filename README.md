# How Short Is Short

We conducted research to estimate an upper bound for short text lengths in short text topic modelling. Three short text topic models and LDA were run on ten corpora. The code used to create the data is available [here](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/CorporaCreation.py). The BTM was [implemented](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/BTM.py) in Python using the [bitermplus](https://pypi.org/project/bitermplus/) package. The GPU-PDMM, GSDMM, and LDA were implemented using the [implementation](https://github.com/qiang2100/STTM) by Qiang *et al.*.

## Data

We include word clouds [here](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/WordClouds.md) for each of the 39 topics used to create the data. A list of the datasets is included below. Clicking on each link provides the top words for the best and worst performing model for that corpus.

[Corpus 1](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C1.md) <br/>
[Corpus 2](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C2.md) <br/>
[Corpus 3](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C3.md) <br/>
[Corpus 4](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C4.md) <br/>
[Corpus 5](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C5.md) <br/>
[Corpus 6](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C6.md) <br/>
[Corpus 7](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C7.md) <br/>
[Corpus 8](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C8.md) <br/>
[Corpus 9](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C9.md) <br/>
[Corpus 10](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/C10.md) <br/>

This selection was based on UMASS and PMI coherence scores for each model. The LDA is not necessarily the best performer on the last four corpora but it was still included as a baseline.

## UMASS coherence over the corpora

UMASS topic coherence was calculated using [this code](https://github.com/keeganstlegerdenny/HowShortIsShort/blob/main/TopicCoherence.py), adapted from [this implementation](https://github.com/CAIR-ZA/GPyM_TM) by Mazarura *et al.*.

![Poster_UMASS](https://github.com/keeganstlegerdenny/HowShortIsShort/assets/76593758/880d77cd-a760-479c-970e-438587b54375)

## PMI coherence over the corpora

The same [STTM](https://github.com/qiang2100/STTM) implementation by Qiang *et al.* was used to calculate PMI coherence scores.

![Poster_PMI](https://github.com/keeganstlegerdenny/HowShortIsShort/assets/76593758/41fbe0ae-a7c2-4bc7-97f9-5220548729fd)
