[![spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
# medaCy
:hospital: Clinical Notes Model for medaCy (BERT+CRF) :hospital:

This repository contains a versioned, medaCy compatible Model for information extraction from clinical notes.

![alt text](https://nlp.cs.vcu.edu/images/Edit_NanomedicineDatabase.png "Nanoinformatics")

# Description
This is the light-weight version (no metamap) of medaCy's model for extracting 9 unique entities from clinical notes:

`Drug, Strength, Duration, Route, Form, ADE, Dosage, Reason, Frequency`

This model was trained using the
[ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)
pre-trained embeddings with CRF.

# Results
Model generalization ability is evaluated over 202 patient clinical note files not seen during training. *Strict* indicates exact matches of spans, *Lenient* indicates a fuzzy matching of spans (model predictions are off by single characters).

| Entity (Count)    |   Precision |   Recall |    F1 |   F1_Min |   F1_Max |
|-------------------|-------------|----------|-------|----------|----------|
| ADE (1584)        |       0.49  |    0.327 | 0.387 |    0.342 |    0.466 |
| Dosage (6902)     |       0.941 |    0.951 | 0.946 |    0.936 |    0.961 |
| Drug (26800)      |       0.904 |    0.891 | 0.898 |    0.883 |    0.905 |
| Duration (970)    |       0.836 |    0.8   | 0.816 |    0.768 |    0.861 |
| Form (11010)      |       0.937 |    0.939 | 0.938 |    0.931 |    0.954 |
| Frequency (10293) |       0.878 |    0.952 | 0.914 |    0.9   |    0.926 |
| Reason (6400)     |       0.653 |    0.513 | 0.571 |    0.554 |    0.598 |
| Route (8989)      |       0.929 |    0.932 | 0.93  |    0.925 |    0.937 |
| Strength (10921)  |       0.956 |    0.955 | 0.955 |    0.95  |    0.961 |
| system (83869)    |       0.894 |    0.896 | 0.893 |    0.889 |    0.902 |

# Training Data
N2C2 2018 Shared Task
The data used to induce this model is protected by HIPAA privacy regulations and thus cannot be published.

Authors
=======
Andriy Mulyar and Bridget McInnes

Acknowledgments
===============
- [VCU Natural Language Processing Lab](https://nlp.cs.vcu.edu/)     ![alt text](https://nlp.cs.vcu.edu/images/vcu_head_logo "VCU")
- [Nanoinformatics Vertically Integrated Projects](https://rampages.us/nanoinformatics/)
