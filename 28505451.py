#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-*- coding: utf-8 -*-


# In[1]:


# bibliothèques

from sklearn.neighbors import DistanceMetric 
from sklearn.feature_extraction.text import CountVectorizer 
from time import perf_counter as pf 
import nltk
import string 
import glob
import re


# In[2]:


# fonctions

def lire_fichier(chemin):
    """ouverture et lecture du document."""
    fichier = open(chemin, encoding='utf-8') 
    chaine = fichier.read()
    fichier.close()
    return chaine

def calcul_distance():
    """calcul de distance"""
    for nom_distance in ["jaccard", "euclidean", "canberra","braycurtis","hamming","dice", "matching", "kulsinski", "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "manhattan", "chebyshev"]:
        distance = DistanceMetric.get_metric(nom_distance)
        V = CountVectorizer(encoding='utf-8')
        X = V.fit_transform([section1, section2]).toarray()
        print(nom_distance)
        print(distance.pairwise(X))
        distance_elem1VS2 = distance.pairwise(X)[0][1]
        print(distance_elem1VS2)


# In[6]:





# In[ ]:





# In[ ]:




