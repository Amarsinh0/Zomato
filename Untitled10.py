#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



# In[23]:


df=pd.read_csv("archive (11).zip",encoding='latin')


# In[24]:


df.head()


# In[25]:


df.info()


# In[26]:


df.describe()


# In[27]:


df.columns


# # data analysis- missing values
# #Explore about catagoriacal variables
# #explore about find relationship 

# In[33]:


df.isnull().sum()


# In[36]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[40]:


df.shape


# In[90]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False, cmap=None)


# In[43]:


#check data types
df.dtypes


# In[57]:


df.columns


# CT=df.City.value_counts().index
# print(CT)

# In[64]:


country_values=df.City.value_counts().values


# In[71]:


plt.pie(country_values[:3],labels=CT[:3],autopct='1%.2f%%')


# # observation: zomato maximum transection are from new delhi then Noida then gurgaon

# In[82]:


ratings=df.groupby(['Aggregate rating','Rating color','Rating text',]).size().reset_index().rename(columns={0:'rating count'})
ratings


# # conclusions
# 1. when rating is 4.5 to 4.9 -- Excellent
# 2. when rating is 4.0 to 3.4 -- Very good
# 3. when rating is  3.0 to 3.4 -- average
# 4. when rating is 2.0 to 2.4 -- poor

# In[84]:


ratings.head()


# In[107]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(14,4)
sns.barplot(x="Aggregate rating",y="rating count",hue='Rating color',data=ratings, palette=['blue','red','orange','yellow','green','brown'])


# In[108]:


# obseravtins
# max value in beatween 2.5 to 3.4


# In[110]:


sns.countplot(x='Rating color',data=ratings, palette=['blue','red','orange','yellow','green','brown'])


# In[121]:


## find the cities that has given 0 rating
df[df['Rating color']=='White'].groupby('City').size().reset_index().head(5)


# In[124]:


df[['City','Currency']].groupby(['City','Currency']).size().reset_index()


# In[ ]:


#online deliveries options


# In[126]:


df[df["Has Online delivery"]=='Yes'].City.value_counts()


# #observation :
# Online delivary are avilable in New delhi

# In[134]:


df.sort_values(['Cuisines'],ascending = False).head(5) 


# In[ ]:




