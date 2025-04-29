#!/usr/bin/env python
# coding: utf-8

# # IMPORTING LIBERARY

# In[4]:


import pandas as pd
pd.__version__


# In[5]:


lst=[1,2,3,4,5,6]
print(lst)


# In[31]:


series= pd.Series(lst)
print(series)
print(type(series))


# In[32]:


empty =pd.Series([])
empty


# In[34]:


a= pd.Series(['q','w','e','r','t'],[1,2,3,4,5])
a


# In[35]:


a= pd.Series(['q','w','e','r','t'],[1,2,3,4,5], name= 'alphabate')
a


# In[36]:


scale_series=pd.Series(0.5)
scale_series


# In[37]:


scale_series=pd.Series(0.5,index=[1,2,3])
scale_series


# # with dictionary

# In[38]:


dict_series=pd.Series({'q':1,'w':2,'e':3,'r':4,'t':5})
dict_series


# In[39]:


dict_series[0]


# In[41]:


dict_series[0:3]


# In[42]:


max(dict_series)


# In[44]:


dict_series =pd.Series({'q':[1,5,6],'w':[4,3,2],'e':[3,5,6],'r':[6,7,4],'t':[1,2,5]})
dict_series


# # Data frame

# 

# In[4]:


import pandas as pd
df=pd.DataFrame()
print(df)


# In[5]:


lst=[1,2,3,43,4,5]
df=pd.DataFrame(lst)
df


# In[8]:


lst=[[1,2,3,4,5],[6,7,8,0,9]]
df=pd.DataFrame(lst)
df


# In[9]:


lst=({'q':1,'w':2,'e':3,'r':4,'t':5},
     {'q':7,'w':4,'e':8,'r':6,'t':9})
df=pd.DataFrame(lst)
df


# In[10]:


a={'roll no.':pd.Series([1,2,3,4,5]),
  'math':pd.Series([67,78,46,89,75]),
  'phys':pd.Series([78,56,45,89,67])}
df=pd.DataFrame(a)
df


# # csv files

# In[20]:


import pandas as pd
df=pd.read_csv(r"D:\\download\\Car_sales.csv")
print(df)


# In[17]:


df.columns


# In[21]:


df.shape


# In[22]:


df.size


# In[23]:


df.head()


# In[24]:


df.head(2)


# In[26]:


df.tail()


# In[27]:


df.head(7)


# In[28]:


df.describe()


# In[29]:


df.info()


# In[42]:


df.isnull()


# In[45]:


df.isnull().sum()


# In[46]:


df.isnull().sum().sum()


# In[47]:


df.shape


# In[55]:


df2=df.dropna(axis = 1)
df2


# In[51]:


df.shape


# In[59]:


df.dropna(how='any')
df


# In[60]:


df.dropna(how='all')


# In[9]:


df.fillna({'Width':49,'Engine size':1.9})


# In[7]:


import pandas as pd
df=pd.read_csv(r"D:\\download\\Car_sales.csv")


# In[11]:


df.replace(to_replace=36,value='30')


# In[12]:


df.replace(4,'40')


# In[20]:


df.replace(to_replace=[16.919], value='A')


# In[26]:


df.replace(to_replace=[140], value='B')


# In[27]:


df.replace(to_replace=[140], value='B')


# In[31]:


df.replace(to_replace=[140,225,225,210,150], value=['A','B','C','D','E'])


# In[33]:


df.replace('[A-Za-z]',0,regex=True)


# In[37]:


df.replace(to_replace=39.384,method = 'ffill')


# In[ ]:




