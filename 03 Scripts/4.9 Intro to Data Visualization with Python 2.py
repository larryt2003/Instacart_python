#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


# # ords_prod_customers merged upload

# In[2]:


df_ords_prod_customers = pd.read_pickle(os.path.join('C:\\Users\\bukola\\Desktop\\Lanre Comp\\Documents\\CF\\Instacart Basket Analysis', '02 Data' , 'ords_prods_customer.pkl'))



# In[4]:


df_ords_prod_customers.head()


# In[5]:


#Creating Bar chart

df_ords_prod_customers['orders_day_of_week'].value_counts().plot.bar()


# In[6]:


# Sort by Index
df_ords_prod_customers['orders_day_of_week'].value_counts().sort_index().plot.bar()


# In[8]:


df_ords_prod_customers['orders_day_of_week'].value_counts().sort_index().plot.bar(color =['purple','green','yellow','brown','pink','red','blue'])


# In[54]:


bar2.figure.savefig(os.path.join('C:\\Users\\bukola\\Desktop\\Lanre Comp\\Documents\\CF\\Instacart Basket Analysis', '02 Data'))


# In[11]:


df_ords_prod_customers['prices'].plot.hist(bins = 25)


# In[10]:


#scatterplot  code 
sns.scatterplot(x = 'prices', y = 'prices',data = df_ords_prod_customers)


# In[14]:


#histogram 
df_ords_prod_customers.loc[df_ords_prod_customers['prices'] >100, 'prices'] = np.nan


# In[15]:


df_ords_prod_customers['prices'].max()


# In[16]:


df_ords_prod_customers['prices'].plot.hist(bins = 25)


# In[56]:


bar2.figure.savefig(os.path.join('C:\\Users\\bukola\\Desktop\\Lanre Comp\\Documents\\CF\\Instacart Basket Analysis', '02 Data'))


# In[18]:


np.random.seed(4)


# #creating a list holding True/False values to the test np.random.rant() <=70
# 
# dev = np.random.rand(len(df_ords_prod_customers)) <= 0.7

# In[20]:


dev = np.random.rand(len(df_ords_prod_customers)) <= 0.7


# In[21]:


np.random.rand()


# # store 70% of the sample in the dataframe big
# big = df_ords_prod_customers[dev]

# In[26]:


big = df_ords_prod_customers[dev]


# # store 30% of the sample in the dataframe small
# small = df_ords_prod_customers[~dev]

# In[27]:


small = df_ords_prod_customers[~dev]


# In[29]:


#subsset base on price and order days of week
df_2 = small[['orders_day_of_week','prices']]


# In[30]:


# create line chart
line = sns.lineplot(data = df_2, x = 'orders_day_of_week',y = 'prices')


# In[31]:


# 
df_ords_prod_customers['order_hour_of_day'].max()


# In[38]:


#histogram of the “order_hour_of_day” column for sales team 
df_ords_prod_customers['order_hour_of_day'].plot.hist(bins = 23)


# The histogram chart shows that most of the sales order are between the hour 7 and 16 hours of the day. all though the sales order were all through the hours in the day with a low order with 0hrs to 5 and at his peak at 10hrs with a gradual decline from 17 hours.  

# In[39]:


# Bar chat within the loyalty flag  
df_ords_prod_customers['loyalty_flag'].value_counts().sort_index().plot.bar()


# In[58]:


bar3.figure.savefig(os.path.join('C:\\Users\\bukola\\Desktop\\Lanre Comp\\Documents\\CF\\Instacart Basket Analysis', '02 Data'))


# In[40]:


df_3 = big[['order_hour_of_day','prices']]


# In[42]:


# create line chart showing expendicture 
line = sns.lineplot(data = df_3, x = 'order_hour_of_day',y = 'prices')


# #There are differences in expenditure in relation to hours of days. Between 0 and 5 hours of the day the prices reach their peaks although there is a sharp decline in prices but still rise to their peak and a sharp decline at the 7th hour and decline to the lowest at the 10th hour of the day with a gradual rise and falls back to start at 0 hours with 7.82 price.

# In[48]:


df_3 = big[['age','num_of_dependants']]


# In[49]:


# create line chart showing connection between age and dependents 
line = sns.lineplot(data = df_3, x = 'age',y = 'num_of_dependants')


# Although there isn't much difference in the age in relation to the number of dependents, it shows that those between the ages of 60 and 80 tend to have more dependents than those between the ages of 0 to 50 years. The distribution has been zigzag.   

# In[50]:


# scatteplot showing connection between age and spending power (income).
sns.scatterplot(x = 'age', y = 'income',data = df_ords_prod_customers)


# #The scatterplot shows the distribution of income among the ages. It shows that most of the ages earn below 2000,000, and individuals between 0 and 40 years below 400001 while a few individuals between the age of 41 and above earn beyond 4000,001.
