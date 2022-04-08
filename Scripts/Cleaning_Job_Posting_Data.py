#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import re
import os


# In[5]:


# Check to see if current job posting file exists to combine with cumulative data
cumulative_job_posting_df = pd.read_csv(r"C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_posting_data_cumulative.csv")

file_path = r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_posting_data_current.csv'

flag = os.path.isfile(file_path)

if flag:
    #open the cumulative CSV file as a DataFrame
    new_job_posting_df = pd.read_csv(file_path)
    #append the DataFrames together
    total_job_posting_df = pd.concat([cumulative_job_posting_df, new_job_posting_df])
else:
    #If the current file doesn't exist, we just use the cumulative file
    total_job_posting_df = cumulative_job_posting_df

# Show the new cumulative data set
#print(total_job_posting_df)


# In[6]:


# Drop rows with blank "job title" or "company name"

total_job_posting_df.dropna(subset=['Job Title', 'Company Name'], inplace=True)


# In[7]:


# Format the "job title" and "company name" columns
total_job_posting_df['Job Title'] = total_job_posting_df['Job Title'].str.replace('/', ' ')
total_job_posting_df['Job Title'] = total_job_posting_df['Job Title'].str.replace('-', ' ')
total_job_posting_df['Job Title'] = total_job_posting_df['Job Title'].str.lower()

total_job_posting_df['Company Name'] = total_job_posting_df['Company Name'].str.replace('/', ' ')
total_job_posting_df['Company Name'] = total_job_posting_df['Company Name'].str.replace('-', ' ')
total_job_posting_df['Company Name'] = total_job_posting_df['Company Name'].str.lower()
#print(total_job_posting_df)


# # Here, we remove the duplicate rows, (ignoring the "Date Posted" b/c the same job can be posted on multiple days)
# 

# In[8]:


#Find duplicate job postings
total_job_posting_df.loc[total_job_posting_df.duplicated(subset=['Job Title', 'Company Name', 'Location'])]


# In[9]:


# Remove duplicate job postings
total_job_posting_df.drop_duplicates(subset=['Job Title', 'Company Name', 'Location', 'Remote', 'Salary', 'Full Time', 'Part Time'],inplace=True, keep='last')
#print(str(len(total_job_posting_df)) + " unique job postings")


# In[10]:


# Save the new cumulative data set
total_job_posting_df.to_csv(r"C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_posting_data_cumulative.csv", index=False)


# In[11]:


job_salaries = total_job_posting_df['Salary']
#print(job_salaries)


# In[12]:


total_job_posting_df['Salary Type'] = total_job_posting_df['Salary'].str.split().str[-1]
#display(total_job_posting_df['Salary Type'].unique())


# In[13]:


# First, remove commas from Salary
total_job_posting_df['Salary'] = total_job_posting_df['Salary'].str.replace(',','')
#print(total_job_posting_df)


# In[14]:


def get_salary_raw_number(row):
    # See if the salary data is a string
    if isinstance(row, str):
        # Find the word "Estimated"
        estimated = row.find("Estimated")
        if estimated != -1:
            # Find the raw number for salary $##.#K
            raw_number = re.search('(\d+(\.\d{1,2})?)K', row).group()
            raw_number = raw_number[:-1]
            raw_number = 1000 * float(raw_number)
        else:
            raw_number = re.search('(\d+)', row).group()
            raw_number = float(raw_number)
    else:
        return None
    return raw_number


# In[15]:


# Get salary number to compute yearly salary

total_job_posting_df['Salary (Raw Number)'] = total_job_posting_df['Salary'].apply(lambda x: get_salary_raw_number(x))
#print(total_job_posting_df)


# In[16]:


def compute_yearly_salary(x):
    yearly_salary = None
    if x['Salary Type'] == "hour":
        yearly_salary = 2087 * int(x['Salary (Raw Number)'])
    elif x['Salary Type'] == "day":
        yearly_salary = 261 * int(x['Salary (Raw Number)'])
    elif x['Salary Type'] == "week":
        yearly_salary = 52 * int(x['Salary (Raw Number)'])
    elif x['Salary Type'] == "month":
        yearly_salary = 12 * int(x['Salary (Raw Number)'])
    elif x['Salary Type'] == "year":
        yearly_salary = int(x['Salary (Raw Number)'])
    else:
        yearly_salary = None
    return yearly_salary
        


# In[17]:


total_job_posting_df['Annual Salary'] = total_job_posting_df.apply(compute_yearly_salary, axis=1)
                                       


# In[18]:


# Drop the unneccessary column
total_job_posting_df.pop('Salary (Raw Number)')


# In[19]:


# Save the .csv file
total_job_posting_df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_Posting_Data_With_Annual_Salary.csv', index=False)


# In[ ]:




