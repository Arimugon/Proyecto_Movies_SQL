#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import csv
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None) 
import re


# In[2]:


def cambio_delate(x):
    
    x=x.lower()
    
    if 'deleted' in x:
        return 'YES'
    
    else:
        return 'NO'
    


# In[3]:


def cambio_behind(x):
    
    x=x.lower()
    
    if 'behind' in x:
        return 'YES'
    
    else:
        return 'NO'


# In[4]:


def cambio_comen(x):
    
    x=x.lower()
    
    if 'comentaries' in x:
        return 'YES'
    
    else:
        return 'NO'


# In[5]:


def cambio_trailers(x):
    
    x=x.lower()
    
    if 'trailers' in x:
        return 'YES'
    
    else:
        return 'NO'


# In[ ]:




