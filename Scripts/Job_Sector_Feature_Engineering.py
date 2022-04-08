#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_Posting_Data_With_Annual_Salary.csv")
#print(df)


# In[3]:


#print(df.iloc[4066])


# In[4]:


# Create a new column of job terms to search for
df['Job Terms'] = df.apply(lambda row: " " + row['Job Title'] + " " + 
                           row['Company Name'] + " ", axis=1)
#print(df['Job Terms'])

# In[11]:


# CREATE A KEYWORD : JOB_SECTOR DICT
job_sector_dict = {
    "agriculture" : "Agriculture Forestry Fishing and Hunting",
    "farm" : "Agriculture Forestry Fishing and Hunting",
    "farmer" : "Agriculture Forestry Fishing and Hunting",
    "ranch" : "Agriculture Forestry Fishing and Hunting",
    "crop" : "Agriculture Forestry Fishing and Hunting",
    "herd" : "Agriculture Forestry Fishing and Hunting",
    "harvest" : "Agriculture Forestry Fishing and Hunting",
    "greenhouse" : "Agriculture Forestry Fishing and Hunting",
    "trimmer" : "Agriculture Forestry Fishing and Hunting",
    "livestock" : "Agriculture Forestry Fishing and Hunting",
    "breeding" : "Agriculture Forestry Fishing and Hunting",
    "farming" : "Agriculture Forestry Fishing and Hunting",
    "cultivation" : "Agriculture Forestry Fishing and Hunting",
    "forestry" : "Agriculture Forestry Fishing and Hunting",
    "forest" : "Agriculture Forestry Fishing and Hunting",
    "arborist" : "Agriculture Forestry Fishing and Hunting",
    "tree" : "Agriculture Forestry Fishing and Hunting",
    "phc" : "Agriculture Forestry Fishing and Hunting",
    "forester" : "Agriculture Forestry Fishing and Hunting",
    "fishing" : "Agriculture Forestry Fishing and Hunting",
    "fish" : "Agriculture Forestry Fishing and Hunting",
    "fishery" : "Agriculture Forestry Fishing and Hunting",
    "fisheries" : "Agriculture Forestry Fishing and Hunting",
    "catch" : "Agriculture Forestry Fishing and Hunting",
    "hunting" : "Agriculture Forestry Fishing and Hunting",
    "wildlife" : "Agriculture Forestry Fishing and Hunting",
    
    "mining" : "Mining Quarrying and Oil and Gas Extraction",
    "mine" : "Mining Quarrying and Oil and Gas Extraction",
    "drilling" : "Mining Quarrying and Oil and Gas Extraction",
    "gold" : "Mining Quarrying and Oil and Gas Extraction",
    "coal" : "Mining Quarrying and Oil and Gas Extraction",
    "lease operator" : "Mining Quarrying and Oil and Gas Extraction",
    "quarrying" : "Mining Quarrying and Oil and Gas Extraction",
    "landman" : "Mining Quarrying and Oil and Gas Extraction",
    "quarry" : "Mining Quarrying and Oil and Gas Extraction",
    "blasting" : "Mining Quarrying and Oil and Gas Extraction",
    "pit" : "Mining Quarrying and Oil and Gas Extraction",
    "oil" : "Mining Quarrying and Oil and Gas Extraction",
    "gas" : "Mining Quarrying and Oil and Gas Extraction",
    "extraction" : "Mining Quarrying and Oil and Gas Extraction",
    "pipeline" : "Mining Quarrying and Oil and Gas Extraction",
    "natural" : "Mining Quarrying and Oil and Gas Extraction",
    "petroleum" : "Mining Quarrying and Oil and Gas Extraction",
    "resources" : "Mining Quarrying and Oil and Gas Extraction",
    
    "utilities" : "Utilities",
    "utility" : "Utilities",
    "meter" : "Utilities",
    "wind" : "Utilities",
    "turbine" : "Utilities",
    "splicer" : "Utilities",
    "electric" : "Utilities",
    "electrician" : "Utilities",
    "water" : "Utilities",
    "plumbing" : "Utilities",
    "plumber" : "Utilities",
    "solar" : "Utilities",
    
    "construction" : "Construction",
    "construct" : "Construction",
    "building" : "Construction",
    "fixture" : "Construction",
    "estimator" : "Construction",
    "installer" : "Construction",
    "installation" : "Construction",
    "installers" : "Construction",
    "bath" : "Construction",
    "shower" : "Construction",
    "safety" : "Construction",
    "joiner" : "Construction",
    "painter" : "Construction",
    "painters" : "Construction",
    "drywall" : "Construction",
    "home" : "Construction",
    "osp" : "Construction",
    "project manager" : "Construction",
    "roofing" : "Construction",
    "demolition" : "Construction",
    "carpenter" : "Construction",
    "general laborer" : "Construction",
    "mason" : "Construction",
    "welder" : "Construction",
    "masonry" : "Construction",
    "foreman" : "Construction",
    "renovation" : "Construction",
    
    "manufacturing" : "Manufacturing",
    "manufacturer" : "Manufacturing",
    "joiner" : "Manufacturing",
    "supply chain" : "Manufacturing",  
    "fabricator" : "Manufacturing", 
    "production" : "Manufacturing",
    "manufacture" : "Manufacturing",
    "solder" : "Manufacturing",
    "assembler" : "Manufacturing",
    "assembly" : "Manufacturing",
    "materials" : "Manufacturing",
    "supply" : "Manufacturing",
    "quality" : "Manufacturing",
    "plant operator" : "Manufacturing",
    "packing" : "Manufacturing",
    "packaging" : "Manufacturing",
    "label" : "Manufacturing",
    "labeling" : "Manufacturing",
    "industry" : "Manufacturing",
    "industrial" : "Manufacturing",
    "machinist" : "Manufacturing",
    "machining" : "Manufacturing",
    "machine" : "Manufacturing",
    "melter" : "Manufacturing",
    "bench" : "Manufacturing",
    
    "wholesale" : "Wholesale Trade",
    "production manager" : "Wholesale Trade",
    "sales" : "Wholesale Trade",
    "purchasing" : "Wholesale Trade",
    "buyer" : "Wholesale Trade",
    "merchandiser" : "Wholesale Trade",
    "trade" : "Wholesale Trade",
    "operations" : "Wholesale Trade",
    
    "retail" : "Retail Trade",
    "client" : "Retail Trade",
    "assisstant manager" : "Retail Trade",
    "salesperson" : "Retail Trade",
    "sales person" : "Retail Trade",
    "store manager" : "Retail Trade",
    "store" : "Retail Trade",
    "general manager" : "Retail Trade",
    "associate" : "Retail Trade",
    "stockroom" : "Retail Trade",
    "sales agent" : "Retail Trade",
    "fulfillment" : "Retail Trade",
    "customer" : "Retail Trade",
    "service" : "Retail Trade",
    "services" : "Retail Trade",
    "storekeeper" : "Retail Trade",
    "cashier" : "Retail Trade",
    
    "transportation" : "Transportation and Warehousing",
    "transport" : "Transportation and Warehousing",
    "warehouse" : "Transportation and Warehousing",
    "logistics" : "Transportation and Warehousing",
    "warehouse" : "Transportation and Warehousing",
    "warehousing" : "Transportation and Warehousing",
    "package" : "Transportation and Warehousing",
    "shipping" : "Transportation and Warehousing",
    "freight" : "Transportation and Warehousing",
    "transportation" : "Transportation and Warehousing",
    "moving" : "Transportation and Warehousing",
    "devlivery" : "Transportation and Warehousing",
    "shipyard" : "Transportation and Warehousing",
    "driver" : "Transportation and Warehousing",
    "courier" : "Transportation and Warehousing",
    "shipper" : "Transportation and Warehousing",
    "handler" : "Transportation and Warehousing",
    
    "information" : "Information",
    "data" : "Information",
    "it" : "Information",
    "cloud" : "Information",
    "network" : "Information",
    "net" : "Information",
    "systems" : "Information",
    "developer" : "Information",
    "website" : "Information",
    "software" : "Information",
    "computer" : "Information",
    "UX" : "Information",
    "test" : "Information",
    "firmware" : "Information",
    "analyst" : "Information",
    
    "finance" : "Finance and Insurance",
    "insurance" : "Finance and Insurance",
    "accounts" : "Finance and Insurance",
    "business" : "Finance and Insurance",
    "account" : "Finance and Insurance",
    "program" : "Finance and Insurance",
    "fiscal" : "Finance and Insurance",
    "claims" : "Finance and Insurance",
    "finance" : "Finance and Insurance",
    "loan" : "Finance and Insurance",
    "marketing" : "Finance and Insurance",
    "tax" : "Finance and Insurance",
    "insurance" : "Finance and Insurance",
    "financial" : "Finance and Insurance",
    "capital" : "Finance and Insurance",
    "bank" : "Finance and Insurance",
    "credit" : "Finance and Insurance",
    "accounting" : "Finance and Insurance",
    "branch" : "Finance and Insurance",
        
    "real estate" : "Real Estate and Rental and Leasing",
    "rental" : "Real Estate and Rental and Leasing",
    "lease" : "Real Estate and Rental and Leasing",
    "leasing" : "Real Estate and Rental and Leasing",
    "mortgage" : "Real Estate and Rental and Leasing",
    "property" : "Real Estate and Rental and Leasing",
    "community manager" : "Real Estate and Rental and Leasing",
    "residential" : "Real Estate and Rental and Leasing",
    "home inspector" : "Real Estate and Rental and Leasing",
    
    "science" : "Professional Scientific and Technical Services",
    "technical" : "Professional Scientific and Technical Services",
    "controller" : "Professional Scientific and Technical Services",
    "laboratory" : "Professional Scientific and Technical Services",
    "fleet" : "Professional Scientific and Technical Services",
    "research" : "Professional Scientific and Technical Services",
    "lab" : "Professional Scientific and Technical Services",
    "specimen" : "Professional Scientific and Technical Services",
    "engineering" : "Professional Scientific and Technical Services",
    "technology" : "Professional Scientific and Technical Services",
    "environmental" : "Professional Scientific and Technical Services",
    "scientist" : "Professional Scientific and Technical Services",
    "field service technician" : "Professional Scientific and Technical Services",
    "engineer" : "Professional Scientific and Technical Services",
    "environmental Inspector" : "Professional Scientific and Technical Services",
    "technician" : "Professional Scientific and Technical Services",

    "manager" : "Management of Companies and Enterprises",
    "consultant" : "Management of Companies and Enterprises",
    "office" : "Management of Companies and Enterprises",
    "executive" : "Management of Companies and Enterprises",
    "human resources" : "Management of Companies and Enterprises",
    "administrative" : "Management of Companies and Enterprises",
    "talent acquisition" : "Management of Companies and Enterprises",
    "bookkeeper" : "Management of Companies and Enterprises",
    "receptionist" : "Management of Companies and Enterprises",
    "revenue" : "Management of Companies and Enterprises",
    "management" : "Management of Companies and Enterprises",
    "payroll" : "Management of Companies and Enterprises",
    "billing" : "Management of Companies and Enterprises",
    "clerk" : "Management of Companies and Enterprises",
    "coordinator" : "Management of Companies and Enterprises",
    "cLERK" : "Management of Companies and Enterprises",
    "manager" : "Management of Companies and Enterprises",
    "director" : "Management of Companies and Enterprises",
    "secretary" : "Management of Companies and Enterprises",
    "communications" : "Management of Companies and Enterprises",
    "supervisor" : "Management of Companies and Enterprises",
    
    "administration" : "Administration & Support Waste Management and Remediation",
    "waste" : "Administration & Support Waste Management and Remediation",
    "wastewater" : "Administration & Support Waste Management and Remediation",
    "trash" : "Administration & Support Waste Management and Remediation",
    "recycling" : "Administration & Support Waste Management and Remediation",
    "cleaning" : "Administration & Support Waste Management and Remediation",
    "clean" : "Administration & Support Waste Management and Remediation",
    "grounds" : "Administration & Support Waste Management and Remediation",
    "maintenance" : "Administration & Support Waste Management and Remediation",
    "groundskeeper" : "Administration & Support Waste Management and Remediation",
    "inspector" : "Administration & Support Waste Management and Remediation",
    "compliance" : "Administration & Support Waste Management and Remediation",
    "administrator" : "Administration & Support Waste Management and Remediation",
    
    "education" : "Educational Services",
    "educational" : "Educational Services",
    "instruction" : "Educational Services",
    "library" : "Educational Services",
    "learning" : "Educational Services",
    "admissions" : "Educational Services",
    "college" : "Educational Services",
    "university" : "Educational Services",
    "academic" : "Educational Services",
    "uc" : "Educational Services",
    "teacher" : "Educational Services",
    "dean" : "Educational Services",
    "instructor" : "Educational Services",
    "tutor" : "Educational Services",
    "tutoring" : "Educational Services",
    "school" : "Educational Services",
    "lecturer" : "Educational Services",
    
    "healthcare" : "Health Care and Social Assistance",
    "medical" : "Health Care and Social Assistance",
    "med" : "Health Care and Social Assistance",
    "behavior" : "Health Care and Social Assistance",
    "patient" : "Health Care and Social Assistance",
    "dental" : "Health Care and Social Assistance",
    "ultrasound" : "Health Care and Social Assistance",
    "optometry" : "Health Care and Social Assistance",
    "x-ray" : "Health Care and Social Assistance",
    "ambulance" : "Health Care and Social Assistance",
    "pharmacy technician" : "Health Care and Social Assistance",
    "nurse" : "Health Care and Social Assistance",
    "lvn" : "Health Care and Social Assistance",
    "veterinarian" : "Health Care and Social Assistance",
    "social" : "Health Care and Social Assistance",
    "welfare" : "Health Care and Social Assistance",
    "case" : "Health Care and Social Assistance",
    "park" : "Health Care and Social Assistance",
    "counselor" : "Health Care and Social Assistance",
    "crisis" : "Health Care and Social Assistance",
    "youth" :  "Health Care and Social Assistance",
    "intervention" : "Health Care and Social Assistance",
    "advocate" :  "Health Care and Social Assistance",
    "case manager" : "Health Care and Social Assistance",
    "social worker" : "Health Care and Social Assistance",
    "case investigator" : "Health Care and Social Assistance",
    
    "art" : "Arts Entertainment and Recreation",
    "arts" : "Arts Entertainment and Recreation",
    "graphic" : "Arts Entertainment and Recreation",
    "graphics" : "Arts Entertainment and Recreation",
    "design" : "Arts Entertainment and Recreation",
    "entertainment" : "Arts Entertainment and Recreation",
    "sport" : "Arts Entertainment and Recreation",
    "music" : "Arts Entertainment and Recreation",
    "musician" : "Arts Entertainment and Recreation",
    "media" : "Arts Entertainment and Recreation",
    "artist" : "Arts Entertainment and Recreation",
    "designer" : "Arts Entertainment and Recreation",
    "amusement" : "Arts Entertainment and Recreation",
    "theater" : "Arts Entertainment and Recreation",
    "theatre" : "Arts Entertainment and Recreation",
    "theatrical" : "Arts Entertainment and Recreation",
    "dance" : "Arts Entertainment and Recreation",
    "dancer" : "Arts Entertainment and Recreation",
    "performer" : "Arts Entertainment and Recreation",
    "audio visual" : "Arts Entertainment and Recreation",
    "av" : "Arts Entertainment and Recreation",
    "stage" : "Arts Entertainment and Recreation",
    "stagehand" : "Arts Entertainment and Recreation",
    
    "accomodation" : "Accommodation and Food Services",
    "food" : "Accommodation and Food Services",
    "cashier" : "Accommodation and Food Services",
    "serving" : "Accommodation and Food Services",
    "kitchen" : "Accommodation and Food Services",
    "dairy" : "Accommodation and Food Services",
    "crew member" : "Accommodation and Food Services",
    "dishwasher" : "Accommodation and Food Services",
    "barista" : "Accommodation and Food Services",
    "chef" : "Accommodation and Food Services",
    "cook" : "Accommodation and Food Services",
    "server" : "Accommodation and Food Services",
    "host" : "Accommodation and Food Services",
    "maid" : "Accommodation and Food Services",
    "hotel" : "Accommodation and Food Services",
    "lodging" : "Accommodation and Food Services",
    "motel" : "Accommodation and Food Services",
    "hospitality" : "Accommodation and Food Services",
    "shift leader" : "Accommodation and Food Services",
    "server" : "Accommodation and Food Services",
    
    "security" : "Other Services (excluding Public Administration)",
    "law" : "Other Services (excluding Public Administration)",
    "legal" : "Other Services (excluding Public Administration)",
    "litigation" : "Other Services (excluding Public Administration)",
    "justice" : "Other Services (excluding Public Administration)",
    "litigation" : "Other Services (excluding Public Administration)",
    "firm" : "Other Services (excluding Public Administration)",
    "contracts" : "Other Services (excluding Public Administration)",
    "ip" : "Other Services (excluding Public Administration)",
    "lawyer" : "Other Services (excluding Public Administration)",
    "attorney" : "Other Services (excluding Public Administration)",
    "attorneys" : "Other Services (excluding Public Administration)",
    "auditor" : "Other Services (excluding Public Administration)",
    "paralegal" : "Other Services (excluding Public Administration)",
    "defender" : "Other Services (excluding Public Administration)",
    "counsel" : "Other Services (excluding Public Administration)",
    "security" : "Other Services (excluding Public Administration)",
    "guard" : "Other Services (excluding Public Administration)",
    "protective" : "Other Services (excluding Public Administration)",
    "police" : "Other Services (excluding Public Administration)",
    "correctional" : "Other Services (excluding Public Administration)",
    "parole" : "Other Services (excluding Public Administration)",
    "surveillance" : "Other Services (excluding Public Administration)",
    "enforcement" : "Other Services (excluding Public Administration)",
    "investigations" : "Other Services (excluding Public Administration)",
    "border patrol" : "Other Services (excluding Public Administration)",
    "interdiction" : "Other Services (excluding Public Administration)",
    "sherriff" : "Other Services (excluding Public Administration)",
    "deputy" : "Other Services (excluding Public Administration)",
    "cadet" : "Other Services (excluding Public Administration)",
    "bailiff" : "Other Services (excluding Public Administration)",
    "investigator" : "Other Services (excluding Public Administration)",
    "inspector" : "Other Services (excluding Public Administration)",
    "personal" : "Other Services (excluding Public Administration)",
    "care" : "Other Services (excluding Public Administration)",
    "support" : "Other Services (excluding Public Administration)",
    "therapy" : "Other Services (excluding Public Administration)",
    "dispatcher" : "Other Services (excluding Public Administration)",
    "helper" : "Other Services (excluding Public Administration)",
    
    "public" : "Public Administration",
    "policy" : "Public Administration",
    "affairs" : "Public Administration",
    "relations" : "Public Administration",
    "communication" : "Public Administration",
    "advocate" : "Public Administration",
    "coordinator" : "Public Administration",
    "city" : "Public Administration",
    "county" : "Public Administration",
    "community" : "Public Administration",
    "neighborhood" : "Public Administration",
    "state" : "Public Administration",
    "organizer" :"Public Administration",
    "program manager" : "Public Administration",
    "government" : "Public Administration",
    
    #"""___________________TEMP JOB SECTOR________________"""
    
    "Fast Food" : "Fast Food",
    "crew" : "Fast Food",
    "team" : "Fast Food",
    "restaurant" : "Fast Food",
    "mcdonald's" : "Fast Food",
    "mcdonald" : "Fast Food",
    "burger" : "Fast Food",
    "jack in the box" : "Fast Food",
    "kitchen" : "Fast Food",
    "salad" : "Fast Food",
    "cashier" : "Fast Food",
    "barista" : "Fast Food",
    "food" : "Fast Food",
    "foods" : "Fast Food",
    "server" : "Fast Food",
    "sandwich" : "Fast Food",
    "snack" : "Fast Food",
    "cart" : "Fast Food",
    "cook" : "Fast Food",
    "beverage" : "Fast Food",
    "chicken" : "Fast Food",
    "hospitality" : "Fast Food",
    "bakery" : "Fast Food",
    "concessions" : "Fast Food",
    "subs" : "Fast Food",
    "tea" : "Fast Food",
    "bagels" : "Fast Food",
    "deli" : "Fast Food",
    "sonic" : "Fast Food",
    "drive ins" : "Fast Food",
    "drive in" : "Fast Food",
    "pizza" : "Fast Food",
    "bakers" : "Fast Food",
    "general manager" : "Fast Food",
    "pretzels" : "Fast Food",
    "cafe" : "Fast Food",
    "shift leader" : "Fast Food",
    "yougurtland" : "Fast Food",
    
    
}


# In[12]:


# Set the Job Sector column
df["Job Sector Score"] = ''
df["Job Sector Score"] = df["Job Sector Score"].apply(dict)
#print(df)



# In[14]:


def find_and_input_job_sector(job_sector_dict, df):
    for keyword, job_sector in job_sector_dict.items():
        # Find job postings based on job title or company name containing a keyword 
        mask = (df["Job Terms"].str.contains(" " + keyword + " "))

        # Fill in the job sector based on the criteria above
        
        for cell in df.loc[mask, 'Job Sector Score']:
            if job_sector not in cell:
                cell.update({job_sector : 1})
            else:
                cell[job_sector] += 1
    return df


# In[15]:


df = find_and_input_job_sector(job_sector_dict, df)


# In[16]:


#display(df['Job Sector Score'])


# In[17]:


# TEMP keep this data to look at in Excel
df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Aggregates\temp_job_sector_scores.csv', index=False)


# In[18]:


# Remove the Job Terms column
df.drop(['Job Terms'], axis=1, inplace=True)


# In[19]:


def get_job_sector(row):
    job_scores_dict = row.loc['Job Sector Score']
    
    if job_scores_dict:
        return max(job_scores_dict, key=job_scores_dict.get)
    else:
        return None

df['Job Sector'] = df.apply(lambda row: get_job_sector(row), axis=1)

# Drop the Job Sector Score column
df.drop(['Job Sector Score'], axis=1, inplace=True)

#display(df)


# In[20]:


# Save this data
df.to_csv(r'C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Data\Job_Posting_Data_with_Job_Sectors.csv', index=False)





