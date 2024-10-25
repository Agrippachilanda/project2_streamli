#!/usr/bin/env python
# coding: utf-8

# In[82]:


import streamlit as st
import pandas as pd
import numpy as pd
import matplotlib.pyplot as plt


# In[84]:


#get_ipython().system('ls')


# In[86]:


df= pd.read_csv('student_performance_data.csv')


# In[88]:


df


# In[29]:





# In[33]:





# In[39]:


df['Gender'].value_counts().plot(kind='bar', xlabel='Gender', ylabel = 'frequency', title='Student distribution by gender')


# In[ ]:





# In[57]:


major_counts = df['Major'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Candidates Registered for Each Major')
plt.axis('equal') 
st.pyplot()
#plt.show()Calculate max, min, and mean GPA for each gender
gpa_stats = data.groupby('gender')['gpa'].agg(['max', 'min', 'mean']).reset_index()


gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']


print(gpa_stats)


# In[64]:


gpa_stats = df.groupby('Gender')['GPA'].agg(['max', 'min', 'mean']).reset_index()

gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']

gpa_stats


# In[66]:


gpa_stats = df.groupby('Major')['GPA'].agg(['max', 'min', 'mean']).reset_index()

gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']

gpa_stats


# In[68]:


mean_gpa = df.groupby('Major')['GPA'].mean().reset_index()

mean_gpa = mean_gpa.sort_values('Major')

plt.figure(figsize=(10, 6))
plt.plot(mean_gpa['Major'], mean_gpa['GPA'], marker='o')
plt.title('Mean GPA per Major')
plt.xlabel('Major')
plt.ylabel('Mean GPA')
plt.xticks(rotation=45)  
plt.grid()
plt.tight_layout()  
plt.show()


# In[72]:


crosstab_gender_major = pd.crosstab(df['Gender'], df['Major'])
print(crosstab_gender_major)


# In[80]:


#crosstab_age_attendance = pd.crosstab(df['Age'], df['AttendanceRate'])
#print(crosstab_age_attendance)


# In[ ]:




