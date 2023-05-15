#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[12]:


data = pd.read_csv(r"D:\\DA\\Projects\\vehicles.csv") 


# In[10]:


data.head()


# In[66]:


data.count()


# In[16]:


data.isnull().sum()


# In[17]:


import seaborn as sns


# In[18]:


import matplotlib.pyplot as plt


# In[22]:


sns.heatmap(data.isnull())
plt.show


# In[25]:


data.groupby('Region').sum().head()


# In[28]:


data.groupby('Region')['Confirmed'].sum()


# In[46]:


data.groupby('Region')['Confirmed'].sum().sort_values( ascending = False).head(10)


# In[36]:


data.head()


# In[48]:


data.groupby('Region')['Confirmed','Recovered'].sum().head()


# In[49]:


data[data.Confirmed < 10].tail(10)


# In[50]:


data[data.Confirmed < 10]


# In[63]:


data = data[~(data.Confirmed < 10)]


# In[56]:


data[data.Confirmed < 11]


# In[60]:


data.count()


# In[67]:


# now the original data is recorded again to avoid any missing data


# In[74]:


data.groupby('Region').Deaths.sum().sort_values().head(35)


# In[76]:


data[data.Region == 'India']


# In[77]:


data[data.Region == 'Egypt']


# In[82]:


data.sort_values( by = [ 'Confirmed']).head()


# In[86]:


data.sort_values( by = [ 'Deaths']).head()


# In[92]:


data.sort_values( by = [ 'Deaths'] , ascending = False).head(10)


# In[91]:


data.sort_values( by = ['Recovered'] , ascending = False).head(10)


# In[ ]:




