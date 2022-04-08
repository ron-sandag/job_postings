#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from SD_Neighborhood_Mapping import find_geolocation_ZIP_Code


# In[3]:


def find_ZIP_Code(row):
    if pd.isnull(row['ZIP Code']):
        return find_geolocation_ZIP_Code(row['Location'])
    else:
        return row['ZIP Code']


# In[4]:


# Import our .csv file
df = pd.read_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_Posting_Data_With_Job_Sectors.csv')

# Create a column of ZIP codes
df['ZIP Code'] = df['Location'].str.extract(r'(\d{5})')
#print(df[df['ZIP Code'].isna()].count())

# Use 'Location' column to find additional ZIP codes
df['ZIP Code'] = df.apply(find_ZIP_Code, axis=1)

#temp = df.apply(find_ZIP_Code, axis=1)
#print(temp)
#print(df)


# # Group each column by ZIP Code

# In[6]:


def find_job_sector(df, sector):
    return sector == df['Job Sector']


# In[7]:


# Count job postings, grouped by ZIP code
count = df.groupby(['ZIP Code']).size()
zip_code_count = pd.Series(count, name='Job Openings')

# Find median salary, grouped by ZIP code
median = df.groupby(['ZIP Code'])['Annual Salary'].median()
zip_code_median_salary = pd.Series(median, name='Median Salary')



# Group "Agriculture Forestry Fishing and Hunting" jobs
sector = "Agriculture Forestry Fishing and Hunting"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
# Check this line
count = df.groupby(['ZIP Code'])[sector].sum()
agriculture_forestry_fishing_and_hunting_count = pd.Series(count, name=sector + " jobs")

# Group "Mining Quarrying and Oil and Gas Extraction" jobs
sector = "Mining Quarrying and Oil and Gas Extraction"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
mining_oil_and_gas_count = pd.Series(count, name=sector + " jobs")

# Group "Utilities" jobs
sector = "Utilities"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
utilities_count = pd.Series(count, name=sector + " jobs")

# Group "Construction" jobs
sector = "Construction"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
construction_count = pd.Series(count, name=sector + " jobs")

# Group "Manufacturing" jobs
sector = "Manufacturing"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
manufacturing_count = pd.Series(count, name=sector + " jobs")

# Group "Manufacturing" jobs
sector = "Manufacturing"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
manufacturing_count = pd.Series(count, name=sector + " jobs")

# Group "Wholesale Trade" jobs
sector = "Wholesale Trade"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
wholesale_trade_count = pd.Series(count, name=sector + " jobs")

# Group "Retail Trade" jobs
sector = "Retail Trade"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
retail_trade_count = pd.Series(count, name=sector + " jobs")

# Group "Transportation and Warehousing" jobs
sector = "Transportation and Warehousing"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
transportation_and_warehousing_count = pd.Series(count, name=sector + " jobs")

# Group "Information" jobs
sector = "Information"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
information_count = pd.Series(count, name=sector + " jobs")

# Group "Finance and Insurance" jobs
sector = "Finance and Insurance"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
finance_and_insurance_count = pd.Series(count, name=sector + " jobs")

# Group "Real Estate and Rental and Leasing" jobs
sector = "Real Estate and Rental and Leasing"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
real_estate_and_rental_and_leasing_count = pd.Series(count, name=sector + " jobs")

# Group "Professional Scientific and Technical Services" jobs
sector = "Professional Scientific and Technical Services"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
professional_scientific_and_technical_count = pd.Series(count, name=sector + " jobs")

# Group "Management of Companies and Enterprises" jobs
sector = "Management of Companies and Enterprises"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
management_of_companies_count = pd.Series(count, name=sector + " jobs")

# Group "Administration & Support Waste Management and Remediation" jobs
sector = "Administration & Support Waste Management and Remediation"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
admin_and_waste_management_count = pd.Series(count, name=sector + " jobs")

# Group "Educational Services" jobs
sector = "Educational Services"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
educational_services_count = pd.Series(count, name=sector + " jobs")

# Group "Health Care and Social Assistance" jobs
sector = "Health Care and Social Assistance"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
health_care_and_social_assistance_count = pd.Series(count, name=sector + " jobs")

# Group "Arts Entertainment and Recreation" jobs
sector = "Arts Entertainment and Recreation"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
arts_entertainment_and_recreation_count = pd.Series(count, name=sector + " jobs")

# Group "Accommodation and Food Services" jobs
sector = "Accommodation and Food Services"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
accommodation_and_food_services_count = pd.Series(count, name=sector + " jobs")

# Group "Public Administration" jobs
sector = "Public Administration"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
public_administration_count = pd.Series(count, name=sector + " jobs")

# Group "Other Services (excluding Public Administration)" jobs
sector = "Other Services (excluding Public Administration)"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
other_count = pd.Series(count, name=sector + " jobs")


#TEMP STUFF
# Group "fast food" jobs
sector = "fast food"
df[sector] = df.apply(lambda x: find_job_sector(x, sector), axis=1)
count = df.groupby(['ZIP Code'])[sector].sum()
fast_food_count = pd.Series(count, name=sector + " jobs")



#print(zip_code_count)
#print(zip_code_median_salary)


# In[8]:


# Create dataframe from this information
zip_code_aggregates_df = pd.concat([zip_code_count, 
                        zip_code_median_salary,
                        agriculture_forestry_fishing_and_hunting_count,
                        mining_oil_and_gas_count,
                        utilities_count,
                        construction_count,
                        manufacturing_count,
                        wholesale_trade_count,
                        retail_trade_count,
                        transportation_and_warehousing_count,
                        information_count,
                        finance_and_insurance_count,
                        real_estate_and_rental_and_leasing_count,
                        professional_scientific_and_technical_count,
                        management_of_companies_count,
                        admin_and_waste_management_count,
                        educational_services_count,
                        health_care_and_social_assistance_count,
                        arts_entertainment_and_recreation_count,
                        accommodation_and_food_services_count,
                        public_administration_count,
                        other_count,
                        fast_food_count,
                        ], axis=1)


# In[9]:


# Create Neighborhood attribute
import os
from SD_Neighborhood_Mapping import find_SD_neighborhood

zip_code_aggregates_df['Neighborhood'] = zip_code_aggregates_df.index.to_series().apply(find_SD_neighborhood)
#print(zip_code_aggregates_df)
zip_code_aggregates_df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Zip_Code_Aggregates.csv')


# In[10]:


# Create District aggregate DataFrame
neighborhood_aggregates_df = zip_code_aggregates_df.groupby(['Neighborhood']).sum()

# The Median Salary column is incorrect, so we drop it and reaggregate
neighborhood_aggregates_df.pop('Median Salary')
neighborhood_aggregates_df['Median Salary'] = zip_code_aggregates_df.groupby(['Neighborhood'])['Median Salary'].mean()
#print(neighborhood_aggregates_df)


# In[11]:


# Add a location column for geolocating in PowerBI
neighborhood_aggregates_df['Location ZIP Code'] = neighborhood_aggregates_df.index.to_series().apply(find_geolocation_ZIP_Code)
#print(neighborhood_aggregates_df)


# In[12]:


# Remove Neighborhoods that have less than 5 job postings
neighborhood_aggregates_df = neighborhood_aggregates_df[neighborhood_aggregates_df["Job Openings"] > 4]
#display(neighborhood_aggregates_df)


# In[13]:


# Save to .csv File

neighborhood_aggregates_df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\Neighborhood_Aggregates.csv')




