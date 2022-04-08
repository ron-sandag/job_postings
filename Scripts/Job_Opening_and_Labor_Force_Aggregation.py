#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


neighborhood_job_count = pd.read_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Neighborhood_Aggregates.csv')
labor_force_count = pd.read_excel(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\neighborhood and labor force collapsed.xlsx')

neighborhood_job_count.set_index('Neighborhood', inplace=True)
labor_force_count.set_index('Neighborhood', inplace=True)
#print(neighborhood_job_count)
#print(labor_force_count)


# In[7]:


# Create a new DataFrame containing the job openings and labor force by neighborhood
neighborhood_job_count = neighborhood_job_count[['Job Openings', 'Location ZIP Code']].copy()
job_count_and_labor_force = neighborhood_job_count.merge(labor_force_count, left_index=True, right_index=True, how='inner')

# Find the ratio of jobs vs labor force 
job_count_and_labor_force['Jobs Over Labor Force Ratio'] = job_count_and_labor_force['Job Openings'] / job_count_and_labor_force['Labor Force']

job_count_and_labor_force['Percentage'] = job_count_and_labor_force['Jobs Over Labor Force Ratio'] * 100
#display(job_count_and_labor_force)


# In[8]:


# Save the DataFrame as a CSV
job_count_and_labor_force.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Job_Count_and_Labor_Force_Aggregate.csv')


# In[ ]:




