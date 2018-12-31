import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import pandas as pd

def scrape() -> pd.DataFrame:

    """
    Logs into Follett Aspen and scrapes HTML table containing grades and course information
    """
    
    #opening chrome in headless mode (no GUI) and going to aspen: https://duo.com/decipher/driving-headless-chrome-with-python
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://ma-concord.myfollett.com/aspen/logon.do')

    #username & password - values stored as bash environment variables (can be replaced with string)
    username_field = browser.find_element_by_name('username').send_keys(os.getenv('ASPEN_USERNAME'))
    password_field = browser.find_element_by_name('password').send_keys(os.getenv('ASPEN_PASSWORD'))

    #          ___________
    #click on | Log On -> |
    #          ‾‾‾‾‾‾‾‾‾‾‾      
    print('\n __________________ \n|logging into Aspen|\n ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ') #login takes ~5 seconds; indicating functionality
    browser.find_element_by_id('logonButton').click()

    #go to academics tab
    browser.get('https://ma-concord.myfollett.com/aspen/portalClassList.do?navkey=academics.classes.list')

    #read all tables from the html and save 25th table (contains the grades)
    grades = pd.read_html(browser.page_source)[24]
    print(' _________________  \n|grades downloaded|\n ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ')

    browser.quit()
    return grades

def reindex(grades): 

    """
    Renames rows and columns of grades table

    Arg:
        grades (DataFrame): a dataframe of grades obtained using scrape() and processed using process()
    """
    #generate col rename dict
    col_rename = {}

    new_col_names = ['Description', 'Term Performance']
    col_names = list(grades)

    for i in range(len(col_names)):
        col_rename[col_names[i]] = new_col_names[i]

    grades = grades.drop(0) #drop the first row containing description and performance as they are now col names
    
    #genrate row rename dict
    row_rename = {}

    row_names = list(grades.index)
    i = 0
    for name in row_names: 
        row_rename[name] = i
        i += 1

    grades = grades.rename(columns=col_rename, index=row_rename)

    return grades


def process(grades):

    """
    Delete classes (rows) which don't give grades from data table

    Arg:
        grades (DataFrame): a dataframe of grades obtained using the scrape() function
    """
    # concise way to do this found at https://stackoverflow.com/a/45681254 & https://stackoverflow.com/a/43399866
    grades = grades[~grades[2].str.contains('Directed Study')]
    grades = grades[~grades[2].str.contains('Health/Fitness')]
    grades = grades[~grades[2].str.contains('Advisory')]

    # same across all aspen accounts so can be hard-coded in
    columns_to_delete = [0, 1, 3, 4, 5, 6, 8, 9, 10] #everything except course name and term performance
    grades = grades.drop(columns_to_delete, axis=1)

    return grades

grades = scrape()
grades = process(grades)
grades = reindex(grades)

# name csv based only on day so that new data from the same day overwrites the old data
csv_name = 'CSVs/' + str(datetime.datetime.now()).split('.')[0].split(' ')[0] + '.csv'
grades.to_csv(csv_name)