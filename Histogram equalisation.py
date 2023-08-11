#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[5]:


img=cv2.imread("Apple.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(imgGray)


# In[3]:


dst=cv2.equalizeHist(imgGray)
dst=cv2.cvtColor(dst,cv2.COLOR_GRAY2BGR)
plt.imshow(dst)


# In[ ]:




