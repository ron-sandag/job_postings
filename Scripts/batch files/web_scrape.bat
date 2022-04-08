@ECHO OFF 
TITLE Execute web scrape python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\ProgramData\Anaconda3\Scripts\activate.bat" base
:: Section 2: Execute python script.
ECHO ============================
ECHO Python indeed_scrape.py
ECHO ============================
python "C:\Users\rla\OneDrive - San Diego Association of Governments\Desktop\Web Scraping Job Postings Project\Scripts\indeed_scrape.py"

ECHO ============================
ECHO End
ECHO ============================

PAUSE