@ECHO OFF 
TITLE Execute web scrape python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\ProgramData\Anaconda3\Scripts\activate.bat" base
:: Section 2: Execute data cleaning script.
ECHO ============================
ECHO Python Cleaning_Job_Posting_Data.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\Cleaning_Job_Posting_Data.py"
ECHO ============================
ECHO Python Job_Sector_Feature_Engineering.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\Job_Sector_Feature_Engineering.py"
ECHO ============================
ECHO End
ECHO ============================

PAUSE