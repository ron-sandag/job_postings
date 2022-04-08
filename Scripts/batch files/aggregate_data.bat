@ECHO OFF 
TITLE Execute web scrape python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\ProgramData\Anaconda3\Scripts\activate.bat" base
:: Section 2: Execute data aggregation scripts.
ECHO ============================
ECHO Python Job_Posting_Aggregation_by_Neighborhood.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\Job_Posting_Aggregation_by_Neighborhood.py"
ECHO ============================
ECHO Python Job_Posting_Aggregation_by_Job_Sector.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\Job_Posting_Aggregation_by_Job_Sector.py"
ECHO ============================
ECHO Python Job_Opening_and_Labor_Force_Aggregation.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\Job_Opening_and_Labor_Force_Aggregation.py"
ECHO ============================
ECHO End
ECHO ============================

PAUSE