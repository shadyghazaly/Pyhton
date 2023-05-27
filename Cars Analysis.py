#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# Reading the data file

# In[2]:


car = pd.read_csv(r'D:\\DA\\Projects\\Data sets\\2. Cars Data1.csv')


# Exploring the data

# In[3]:


car.head()


# In[4]:


car.shape


# In[5]:


car.tail()


# Data Cleaning

# Finding null values and removing them

# In[6]:


car.isnull()


# In[7]:


car.isnull().sum()


# So there are some null values , lets replace them

# In[8]:


car.dropna(inplace = True)


# In[9]:


car.isnull().sum()


# Now we replaced all the null values with the mean

# different types of makes and their count

# In[10]:


car.head(2)


# In[11]:


make_counts = car['Make'].value_counts().reset_index()
make_counts.columns = ['Make', 'Count']
print(make_counts)


# top 5 makes

# In[12]:


car['Make'].value_counts().nlargest(5)


# Now we will show the records were the Origin is Asia

# In[13]:


car.head(2)


# In[14]:


car[car.Origin.isin(['Asia'])]

removing the rows where the weight is heavier than 4000
# In[ ]:





# In[15]:


car['Weight'].dtype


# In[16]:


car['Weight'] = car['Weight'].astype(float)


# In[17]:


car['Weight'] = pd.to_numeric(car['Weight'], errors='coerce')


# In[18]:


car['Weight'].dropna(inplace = True)


# In[19]:


car['Weight'].isnull().sum()


# We had to reformat the Weight column as the dtype was not float so we couldn't use the > operator

# In[20]:


car[~(car['Weight'] > 4000)]


# In[21]:


car


# getting the most power efficient cars

# In[22]:


car.nlargest(5,'MPG_City')


# The most Fuel consuming  cars

# In[24]:


car.nsmallest (5,'MPG_City')


# Getting the top 5 makes according to the average in HP 

# In[33]:


car.groupby('Make')['Horsepower'].mean().nlargest(5).round(decimals=2)


# Getting the lowest 5 makes according to the average in Fuel consumption 

# In[32]:


car.groupby('Make')['MPG_Highway'].mean().nlargest(5).round(decimals = 2)


# Getting the highest 5 makes according to the average in Fuel consumption 

# In[34]:


car.groupby('Make')['MPG_Highway'].mean().nsmallest(5).round(decimals=2)


# In[35]:


car.groupby('Make')['Invoice'].mean().nsmallest(5).round(decimals=2)


# Now we can't do any aggregation on the invoice column because it's not numeric so let's convert it and remove the $ sign and ,

# In[38]:


car['Invoice'] = car['Invoice'].str.replace('$', '').astype(float)


# In[41]:


car.head()


# In[40]:


car['Invoice'] = car['Invoice'].str.replace(',', '').str.replace('$', '').astype(float)


# Now the cheapest average makes

# In[42]:


car.groupby('Make')['Invoice'].mean().nsmallest(5).round(decimals=2)


# Now the most expensive average make

# In[43]:


car.groupby('Make')['Invoice'].mean().nlargest(5).round(decimals=2)


# Tallest Cars

# In[45]:


car.nlargest(5,'Length')


# Shortest Cars

# In[47]:


car.nsmallest(5,'Length')


# In[48]:


car.head()


# the heaviest car

# In[49]:


car.nlargest(3,'Weight')


# The lightest Cars

# In[50]:


car.nsmallest(3,'Weight')


# In[ ]:




