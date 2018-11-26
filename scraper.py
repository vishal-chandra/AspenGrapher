import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import pandas as pd

#opening chrome in headless mode and going to aspen: https://duo.com/decipher/driving-headless-chrome-with-python
chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(chrome_options=chrome_options)
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

#close chrome
browser.quit()

print(grades)