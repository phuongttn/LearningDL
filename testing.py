#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Scalar (0-D Tensor)
import torch
x = torch.rand(5)
print(x)
print(x.size())


# In[5]:


#Vector 1D - Tensor 
temp = torch.FloatTensor([23,24,24.5,26,27.2,23.0])
print(temp)
print(temp.size())

