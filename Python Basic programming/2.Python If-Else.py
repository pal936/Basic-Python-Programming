#!/usr/bin/env python
# coding: utf-8

# ### 2.Python If-Else

# In[1]:


p = int(input())
if p % 2 != 0:
    print("Weird")
else:
    if p >= 2 and p <= 5:
        print("Not Weird")
    elif p >= 6 and p <= 20:
        print("Weird")
    elif p > 20:
        print("Not Weird")

