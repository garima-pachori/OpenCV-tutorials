#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img=cv2.imread('apple.jpg')
kernel=np.ones((5,5),np.uint8)
plt.imshow(img)


# In[3]:


erosion=cv2.erode(img,kernel)
plt.imshow(erosion)


# In[4]:


dilation=cv2.dilate(img,kernel)
plt.imshow(dilation)


# In[ ]:




