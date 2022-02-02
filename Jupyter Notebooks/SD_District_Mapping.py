#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Turn the ZIP code information into districts

# In[2]:



zip_code_mapping = {
"91901" : "Alpine",
"91906" : "Campo",
    # Bonita Zip Code (for geo location) = 91902  
"91902" : "Bonita",
"91908" : "Bonita",
    # Chula vista Zip Code (for geo location) = 91910
"91909" : "Chula Vista",
"91910" : "Chula Vista",
"91911" : "Chula Vista",
"91913" : "Chula Vista",
"91914" : "Chula Vista",
"91915" : "Chula Vista",
"91921" : "Chula Vista",
"91916" : "Descanso",
"91932" : "Imperial Beach",
"91935" : "Jamul",
    # La Mesa Zip Code (for geo location) = 91942
"91941" : "La Mesa",
"91942" : "La Mesa",
"91944" : "La Mesa",
    # Lemon Grove Zip Code (for geo location) = 91945
"91945" : "Lemon Grove",
"91946" : "Lemon Grove",
"91950" : "National City",
    # Spring Valley Zip Code (for geo location) = 91978
"91976" : "Spring Valley",
"91977" : "Spring Valley",
"91978" : "Spring Valley",
"91987" : "Tecate",
"92007" : "Cardiff",
    # Carlsbad Zip Code (for geo location) = 92008
"92008" : "Carlsbad",
"92009" : "Carlsbad",
"92010" : "Carlsbad",
"92011" : "Carlsbad",
"92018" : "Carlsbad",
"92014" : "Del Mar",
    # El Cajon Zip Code (for geo location) = 92020
"92019" : "El Cajon",
"92020" : "El Cajon",
"92021" : "El Cajon",
"92022" : "El Cajon",
"92024" : "Encinitas",
    # Escondido Zip Code (for geo location) = 92025
"92025" : "Escondido",
"92026" : "Escondido",
"92027" : "Escondido",
"92029" : "Escondido",
"92033" : "Escondido",
    # Fallbrook Zip Code (for geo location) = 92028
"92028" : "Fallbrook",
"92088" : "Fallbrook",
"92036" : "Julian",
"92037" : "La Jolla",
"92040" : "Lakeside",
    # Oceanside Zip Code (for geo location) = 92054
"92049" : "Oceanside",
"92051" : "Oceanside",
"92052" : "Oceanside",
"92054" : "Oceanside",
"92055" : "Oceanside",
"92056" : "Oceanside",
"92057" : "Oceanside",
"92058" : "Oceanside",
"92059" : "Pala",
"92061" : "Pauma Valley",
"92064" : "Poway",
"92065" : "Ramona",
"92067" : "Rancho Santa Fe",
    # San Marcos Zip Code (for geo location) = 92069
"92069" : "San Marcos",
"92078" : "San Marcos",
"92096" : "San Marcos",
"92070" : "Santa Ysabel",
    # Santee Zip Code (for geo location) = 92071
"92071" : "Santee",
"92072" : "Santee",
"92074" : "Poway",
"92075" : "Solana Beach",
    # Vista Zip Code (for geo location) = 92083
"92081" : "Vista",
"92083" : "Vista",
"92084" : "Vista",
"92085" : "Vista",
"92082" : "Valley Center",
    # La Jolla Zip Code (for geo location) = 92037
"92092" : "La Jolla",
"92093" : "La Jolla",
"92101" : "Downtown",
"92102" : "Golden Hill",
"92103" : "Hillcrest, Mission Hills",
"92104" : "North Park",
"92105" : "City Heights",
"92106" : "Point Loma",
"92107" : "Ocean Beach",
"92108" : "Mission Valley",
"92109" : "Pacific Beach, Mission Beach",
"92110" : "Morena",
"92111" : "Linda Vista",
"92113" : "Logan Heights",
"92114" : "Encanto",
"92115" : "College",
"92116" : "Kensington, Normal Heights",
"92117" : "Clairemont",
"92118" : "Coronado",
"92119" : "San Carlos",
"92120" : "Allied Gardens, Del Cerro",
"92121" : "Sorrento Valley",
"92122" : "University City",
"92123" : "Serra Mesa",
"92124" : "Tierrasanta",
"92126" : "Mira Mesa",
    # Rancho Bernardo Zip Code (for geo location) = 92127
"92127" : "Rancho Bernardo",
"92128" : "Rancho Bernardo",
"92129" : "Penasquitos",
"92130" : "Carmel Valey",
"92131" : "Scripps Ranch",
"92132" : "Downtown",
"92134" : "Balboa Park",
"92135" : "Coronado",
"92136" : "Logan Heights",
"92139" : "Paradise Hills",
"92140" : "Midway",
"92145" : "Miramar",
"92152" : "Point Loma",
"92154" : "Otay Mesa",
"92155" : "Coronado",
"92161" : "La Jolla",
"92170" : "Downtown",
"92173" : "San Ysidro",
"92175" : "College",
"92178" : "Coronado",
"92179" : "Otay Mesa",
"92182" : "College",
"92192" : "University City",
"92195" : "College",   
}


# In[3]:


district_geolocation_mapping = {
"Allied Gardens, Del Cerro" : "92120",
"Alpine" : "91901",
"Balboa Park" : "92134",
"Bonita" : "91902",
"Campo" : "91906",
"Cardiff" : "92007",
"Carlsbad" : "92008",
"Carmel Valey" : "92130",
"Chula Vista" : "91910",
"City Heights" : "92105",
"Clairemont" : "92117",
"College" : "92115",
"Coronado" : "92118",
"Del Mar" : "92014",
"Descanso" : "91916",
"Downtown" : "92101",
"El Cajon" : "92020",
"Encanto" : "92114",
"Encinitas" : "92024",
"Escondido" : "92025",
"Fallbrook" : "92028",
"Golden Hill" : "92102",
"Hillcrest, Mission Hills" : "92103",
"Imperial Beach" : "91932",
"Jamul" : "91935",
"Julian" : "92036",
"Kensington, Normal Heights" : "92116",
"La Jolla" : "92037",
"La Mesa" : "91942",
"Lakeside" : "92040",
"Lemon Grove" : "91945",
"Linda Vista" : "92111",
"Logan Heights" : "92113",
"Midway" : "92140",
"Mira Mesa" : "92126",
"Miramar" : "92145",
"Mission Valley" : "92108",
"Morena" : "92110",
"National City" : "91950",
"North Park" : "92104",
"Ocean Beach" : "92107",
"Oceanside" : "92054",
"Otay Mesa" : "92154",
"Pacific Beach, Mission Beach" : "92109",
"Pala" : "92059",
"Paradise Hills" : "92139",
"Pauma Valley" : "92061",
"Penasquitos" : "92129",
"Point Loma" : "92106",
"Poway" : "92064",
"Ramona" : "92065",
"Rancho Bernardo" : "92127",
"Rancho Santa Fe" : "92067",
"San Carlos" : "92119",
"San Marcos" : "92069",
"San Ysidro" : "92173",
"Santa Ysabel" : "92070",
"Santee" : "92071",
"Scripps Ranch" : "92131",
"Serra Mesa" : "92123",
"Solana Beach" : "92075",
"Sorrento Valley" : "92121",
"Spring Valley" : "91978",
"Tecate" : "91987",
"Tierrasanta" : "92124",
"University City" : "92122",
"Valley Center" : "92082",
"Vista" : "92083",
}


# In[4]:


def find_SD_district(zip_code):
    if zip_code in zip_code_mapping:
        return zip_code_mapping[zip_code]
    else:
        return None


# In[5]:


def find_geolocation_ZIP_Code(location):
    for district, ZIP_Code in district_geolocation_mapping.items():
        district_index = location.find(district)
        if district_index != -1:
            return ZIP_Code


# In[6]:


#location = "Encinitas"

#temp = find_geolocation_ZIP_Code(location)
#print(temp)


# In[7]:


#print(find_SD_district("32120"))
#print(find_geolocation_ZIP_Code("Chula Vista"))


# In[8]:


# Save the zip_code_mapping dict as .csv
zip_code_mapping_df = pd.DataFrame.from_dict(zip_code_mapping, orient='index')
print(zip_code_mapping_df)

zip_code_mapping_df.to_csv('../Zip_Code_Mappings.csv')


# In[ ]:




