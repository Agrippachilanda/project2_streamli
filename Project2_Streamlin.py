import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.read_csv('student_performance_data.csv')


df['Gender'].value_counts().plot(kind='bar', xlabel='Gender', ylabel = 'frequency', title='Student distribution by gender')


major_counts = df['Major'].value_counts()

st.subheader('Number of Candidates Registered for Each Major')
fig, ax = plt.subplots()
plt.figure(figsize=(8, 6))
ax.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Candidates Registered for Each Major')
plt.axis('equal')
st.pyplot(fig)
#Calculate max, min, and mean GPA for each gender

gpa_stats = df.groupby('Gender')['GPA'].agg(['max', 'min', 'mean']).reset_index()


gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']

gpa_stats = df.groupby('Gender')['GPA'].agg(['max', 'min', 'mean']).reset_index()

gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']

gpa_stats = df.groupby('Major')['GPA'].agg(['max', 'min', 'mean']).reset_index()

gpa_stats.columns = ['Gender', 'Max GPA', 'Min GPA', 'Mean GPA']


mean_gpa = df.groupby('Major')['GPA'].mean().reset_index()

mean_gpa = mean_gpa.sort_values('Major')


st.subheader('Mean GPA per Major')
fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))
ax.plot(mean_gpa['Major'], mean_gpa['GPA'], marker='o')
plt.title('Mean GPA per Major')
plt.xlabel('Major')
plt.ylabel('Mean GPA')
plt.xticks(rotation=45)  
plt.grid()
plt.tight_layout()  
st.pyplot(fig)

crosstab_gender_major = pd.crosstab(df['Gender'], df['Major'])
