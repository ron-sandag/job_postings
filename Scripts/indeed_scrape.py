#!/usr/bin/env python
# coding: utf-8

# # In this notebook, we will scrape job posting data from Indeed for Employment data

# The majority of this project is based on this article by Bonnie Ma:
# https://towardsdatascience.com/web-scraping-job-postings-from-indeed-com-using-selenium-5ae58d155daf
# 
# First, we import selenium and specify the driver path

# In[26]:


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import datetime
import os.path
import random

import pandas as pd

#specify driver path
DRIVER_PATH = '/Users/rla/OneDrive - San Diego Association of Governments/Desktop/edgedriver_win64/msedgedriver'
service = Service(DRIVER_PATH)
driver = webdriver.Edge(service = service)


# Next, we need navigate to our target website (Indeed.com) and perform a search with the correct settings before we can begin scraping.

# In[27]:


#click on the "Find Jobs" button to get search results
#initial_search_button = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')
#initial_search_button.click()

#assign the correct search settings

#set the search radius to "within 50 miles" to cover San Diego County
#filter_radius_button = driver.find_element(By.ID, "filter-radius")
#filter_radius_button.click()
#radius_menu = driver.find_element(By.ID, "filter-radius-menu")
#fifty_mile_radius_button = radius_menu.find_element(By.XPATH, ".//li[6]")
#fifty_mile_radius_button.click()


# In[28]:


#navigate to indeed.com
# This webpage already has the search settings we are looking for
driver.get('https://indeed.com/jobs?q=&l=San+Diego%2C+CA&radius=50&sort=date')
driver.implicitly_wait(10)


# In[29]:


def convert_text_to_date(post_date, debug=False):
    if debug:
        print(post_date)
    if post_date is None:
        return None
    x = re.search(r"Today|Just posted|Posted", post_date)
    if x == None:
        return datetime.datetime.now().date()
    if (x):
        days_past = 0
    else:
        x = re.search(r"\d+", post_date)
        days_past = int(x.group())

    current_datetime = datetime.datetime.now()
    delta = datetime.timedelta(days=days_past)
    final_date =(current_datetime-delta).date() 
    return final_date


# In[30]:


#begin scraping data

def web_scraper():
    
    #close the pop-up that appears
    try:
        close_popup = driver.find_element(By.ID, "popover-x")
    except:
        print("No pop-up found. Continuing")
    else:
        close_popup.click()

    titles=[]
    names=[]
    locations=[]
    remotes=[]
    salaries=[]
    full_times=[]
    part_times=[]
    post_dates=[]

    #begin iterating through result pages

    print("Begin scraping page")
    
    try:
        #let the driver wait 15 seconds to locate the element
        # TODO: incorporate random wait time
        driver.implicitly_wait(random.randrange(15,40))
        job_card = driver.find_elements(By.XPATH, '//div[@class="job_seen_beacon"]')
    except:
        driver.navigate().refresh()

    for job in job_card:
        #extract the job title
        title = job.find_element(By.XPATH, './/td[@class="resultContent"]/div/h2/span').text
        titles.append(title)

        #extract the company name
        name = job.find_element(By.XPATH, './/span[@class="companyName"]').text
        names.append(name)    

        #extract the company location
        location = job.find_element(By.XPATH, './/div[@class="companyLocation"]').text
        locations.append(location)

        #extract remote workplace information
        x = re.search(r"Remote", location)
        if (x):
            remotes.append(True)
        else:
            remotes.append(False)

        #extract metadata information
        try:
            metadata = job.find_element(By.XPATH, './/td[@class="resultContent"]/div[3]').text
            metadata = metadata.split("\n")
        except:
            metadata = None

        #extract salary from metadata
        salary=None
        for data in metadata:
            if '$' in data:
                salary = data
        salaries.append(salary)

        #extract job type from metadata
        full_time=False
        part_time=False
        for data in metadata:
            if "Full-time" in data:
                full_time = True
            if "Part-time" in data:
                part_time = True
        full_times.append(full_time)
        part_times.append(part_time)

        #extract the job posting date
        post_date = job.find_element(By.XPATH, '(.//span[@class="date"])[last()]').text
        
        # Convert posted info into actual date
        final_date = convert_text_to_date(post_date)
        post_dates.append(final_date)

    print("Finished scraping page")
    
    #put all the data into a DataFrame
    job_postings_df = pd.DataFrame()
    job_postings_df['Job Title'] = titles
    job_postings_df['Company Name'] = names
    job_postings_df['Location'] = locations
    job_postings_df['Remote'] = remotes
    job_postings_df['Salary'] = salaries
    job_postings_df['Full Time'] = full_times
    job_postings_df['Part Time'] = part_times
    job_postings_df['Date Posted'] = post_dates

    # Check to see if cumulative job posting file exists
    file_path = r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_posting_data_current.csv'
    flag = os.path.isfile(file_path)
    
    if flag:
        #open the cumulative CSV file as a DataFrame
        old_df = pd.read_csv(file_path)
        #append the DataFrames together
        combined_job_posting_df = old_df.append(job_postings_df)
    else:
        combined_job_posting_df = job_postings_df
    
    #save the new DataFrame as a CSV file
    print("Saving data")
    combined_job_posting_df.to_csv(file_path, index=False)

    #click for the next page of results
    next_page_exists = True
    try:
        next_page = driver.find_element(By.XPATH, '//a[@aria-label="Next"]//span[@class="np"]')
        print("Continuing to next page\n")
        next_page.click()
    except:
        print("Unable to find next page arrow\n")
        next_page_exists = False
    return next_page_exists
    


# In[31]:


# TESTING
next_page_exists = True
current_page = 1
while next_page_exists:
    print("Scraping page " + str(current_page))
    next_page_exists = web_scraper()
    current_page += 1


# In[6]:


print("Scraping finished")


# In[ ]:




