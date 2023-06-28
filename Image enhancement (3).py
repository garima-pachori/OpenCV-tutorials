#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import cv2
from matplotlib import pyplot as plt


# In[14]:


def add_noise(img):
    row,col=img.shape
    number_of_pixels=random.randint(300,10000)
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord][xcord]=255
    number_of_pixels=random.randint(300,10000)
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[ycord][xcord]=255
        
    return img
        


# In[15]:


import cv2
import matplotlib.pyplot as plt
image=cv2.imread('policeman-1.jpg')
plt.imshow(image)
plt.show()


# In[16]:


image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()


# In[17]:


img=cv2.imread('policeman-1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('Withnoise.jpg',add_noise(img))
noise_image=cv2.imread('Withnoise.jpg')
plt.imshow(noise_image)
plt.show()


# In[18]:


median=cv2.medianBlur(noise_image,5)
plt.imshow(median)
plt.show()


# In[ ]:




