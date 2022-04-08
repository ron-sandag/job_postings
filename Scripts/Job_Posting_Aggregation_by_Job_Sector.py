#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[18]:


df = pd.read_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Neighborhood_Aggregates.csv')

# Drop irrelevant columns
df = df.drop(['Job Openings', 'Median Salary', 'Location ZIP Code'], axis=1)

# Create a transpose of the Neighborhood aggregates file for visualization 
# based on Job Sectors instead of district
df = df.transpose()

# Set the neighborhoods to be the header of the DataFrame
df.columns = df.iloc[0]

# Remove neighborhood row
df = df.drop(index=df.index[[0]])

# Rename Neighborhood header to "Job Sector"
df.index.names = ['Job Sector']

#display(df)


# In[20]:


# Create a column of total job_openings

df['Job Openings'] = df.sum(axis=1)

#display(df)


# In[21]:


# Save job sector data
df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Job_Sector_Aggregates.csv')



