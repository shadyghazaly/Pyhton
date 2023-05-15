#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'D:\DA\Projects\5. London Housing Data.csv')


# In[3]:


data.head()


# In[5]:


data.shape


# In[6]:


data.count()


# In[8]:


data.isnull().sum()


# In[9]:


data.head(3)


# In[10]:


import seaborn as sns


# In[11]:


import matplotlib.pyplot as plt


# In[13]:


sns.heatmap(data.isnull())
plt.show


# In[17]:


data.dtypes


# In[18]:


data.date = pd.to_datetime(data.date)


# In[19]:


data.dtypes


# In[20]:


data.head()


# In[52]:


data['Year'] = data.date.dt.year


# In[29]:


data.head()


# In[32]:


data['Month'] = data.date.dt.month


# In[33]:


data.head()


# In[42]:


data.drop('Month' , axis = 1 , inplace = True)


# In[50]:


data.insert(1, 'Month', data.date.dt.month )


# In[53]:


data.head()


# In[54]:


data.drop(['Month' , 'Year'] , axis =1 , inplace = True)


# In[55]:


data.head()


# In[60]:


data[data.no_of_crimes == 0].value_counts().sum()


# In[61]:


data['Year'] = data.date.dt.year


# In[62]:


data.head()


# In[64]:


df = data[data.area == 'england']


# In[76]:


df.groupby('Year').average_price.mean()


# In[91]:


data.groupby('area').no_of_crimes.mean().sort_values()


# In[92]:


data.head()


# In[103]:


data[data.average_price < 100000].area.value_counts().sort_values()


# In[ ]:


# Thanks


# In[ ]:




