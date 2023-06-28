#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread('apple.jpg', 0)
imginv = 255 - im

fig = plt.figure(figsize=(15, 5))

ax = fig.add_subplot(121)
plt.title('Original', fontsize=18)
plt.imshow(im, cmap='gray')

ax = fig.add_subplot(122)
plt.imshow(imginv, cmap='gray')
ax.set_title('Inverse Transform', fontsize=18)

plt.show()


# In[11]:


import cv2
import matplotlib.pyplot as plt
import numpy as np

im=cv2.imread('apple.jpg',0)
log=0.6*(np.log(1+np.float32(im)))
fig=plt.figure(figsize=(15,5))
ax=fig.add_subplot(121)
plt.title('Original',fontsize=18)
plt.imshow(im,cmap='gray')
ax=fig.add_subplot(122)
plt.imshow(log,cmap='gray')
ax.set_title('log Transform',fontsize=18)


# In[ ]:




