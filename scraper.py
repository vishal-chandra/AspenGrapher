import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import pandas as pd

'''
Logs into Follett Aspen and scrapes HTML table containing grades and course information
(work in progress)
'''
def scrape() -> pd.DataFrame:
    #opening chrome in headless mode and going to aspen: https://duo.com/decipher/driving-headless-chrome-with-python
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://ma-concord.myfollett.com/aspen/logon.do')

    #username
    username_field = browser.find_element_by_name('username')
    #set username as bash environment variable for security on github - can be replaced with string
    username_field.send_keys(os.getenv('ASPEN_USERNAME'))

    #password
    password_field = browser.find_element_by_name('password')
    #set password as bash environment variable for security on github- can be replaced with string
    password_field.send_keys(os.getenv('ASPEN_PASSWORD'))

    #click on "Log On ->"
    login_button = browser.find_element_by_id('logonButton')
    login_button.click()

    #go to academics tab
    browser.get('https://ma-concord.myfollett.com/aspen/portalClassList.do?navkey=academics.classes.list')

    #save all tables from the html, then pick out 25th table (contains the grades)
    grades = pd.read_html(browser.page_source)[24]

    browser.quit()

    return grades

grades = scrape()
# delete classes (rows) which don't give grades from data table
# concise way to do this found at https://stackoverflow.com/a/45681254 & https://stackoverflow.com/a/43399866
grades = grades[~grades[2].str.contains('Directed Study')]
grades = grades[~grades[2].str.contains('Health/Fitness')]
grades = grades[~grades[2].str.contains('Advisory')]

# same across all aspen accounts so can be hard-coded in
columns_to_delete = [0, 1, 3, 4, 5, 6, 8, 9, 10] #everything except course name and term performance
grades = grades.drop(columns_to_delete, axis=1)


csv_name = 'CSVs/' + str(datetime.datetime.now()).split('.')[0] + '.csv'
grades.to_csv(csv_name)