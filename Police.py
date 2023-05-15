#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'D:\DA\Projects\3. Police Data.csv')


# In[3]:


data.tail(3)


# In[4]:


data.isnull().sum()


# In[5]:


data.drop( columns = 'country_name' , inplace = True)


# In[6]:


data.tail()


# In[7]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# In[8]:


data[data.search_conducted].driver_gender.value_counts()


# In[9]:


data.groupby('driver_gender').search_conducted.sum()


# In[10]:


data.head()


# In[13]:


data.stop_duration.value_counts()


# In[14]:


data.stop_duration = data.stop_duration.map({'0-15 Min' : 7.5 , '16-30 Min' : 23 , '30+ Min' : 45 })


# In[18]:


data.stop_duration.value_counts()


# In[19]:


data


# In[20]:


data['stop_duration'].mean()


# In[21]:


data.head()


# In[27]:


data.groupby('violation').driver_age.describe()


# In[ ]:




