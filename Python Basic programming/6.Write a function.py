#!/usr/bin/env python
# coding: utf-8

# ### 6.Write a function

# In[1]:


def leap(year):
    y = False
    if y % 400 == 0:
        y = True
    elif y % 100 == 0:
        y = False
    elif year % 4 == 0:
        y = True
    
    return y
    
year = int(input())
leap(year)

