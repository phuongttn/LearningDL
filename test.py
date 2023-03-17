#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image 
import os 
import numpy as np
import shutil 
import torch

#get the current Path of working folder 
current_path = os.getcwd()
print(current_path)

#copy file panda to the current working folder 
shutil.copy('/Users/phuonglinh/Downloads/panda.jpeg', current_path)

#convert to tensor 3d and resize it. 
panda = np.array(Image.open('panda.jpeg').resize((224,224)))
panda_tensor = torch.from_numpy(panda)
panda_tensor.size()

#display image 
import matplotlib.pyplot as plt
plt.imshow(panda_tensor)


# In[ ]:




