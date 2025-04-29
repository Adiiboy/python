#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df_bgmi=pd.read_csv (hash)
df_bgmi


# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv")
df_bgmi


# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
df_bgmi  


# In[35]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
x=df_bgmi["Matches_Played"]
y= df_bgmi ["Kills"]
plt.scatter(x,y)
df_bgmi


# In[36]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
x=df_bgmi["Matches_Played"]
y= df_bgmi ["Kills"]
plt.scatter(x,y)
plt.xlabel("matched palyed")
plt.ylabel("kills")
df_bgmi


# In[45]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
x=df_bgmi["Matches_Played"]
y= df_bgmi ["Kills"]
plt.scatter(x,y)
plt.xlabel("matched palyed")
plt.ylabel("kills")
plt.figure(figsize= (20,60))
df_bgmi


# In[52]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
x=df_bgmi["Matches_Played"]
y= df_bgmi ["Kills"]
plt.scatter(x,y, c="r" , marker = "*" , s= 100, alpha = 0.2)
plt.xlabel("matched palyed")
plt.ylabel("kills")
plt.figure(figsize= (20,60))
df_bgmi


# In[57]:


import matplotlib.pyplot as plt
import pandas as pd
df_bgmi=pd.read_csv("C:\\Users\\adity\\Documents\\archive\\Pubg_Stats.csv",nrows = 100)
x=df_bgmi["Matches_Played"]
y= df_bgmi ["Kills"]
plt.scatter(x,y, c="r" , marker = "*" , s= 100, alpha = 0.2)
plt.title(" match and kills")
plt.xlabel("matched palyed")
plt.ylabel("kills")
plt.figure(figsize= (20,60))
df_bgmi


# In[ ]:




