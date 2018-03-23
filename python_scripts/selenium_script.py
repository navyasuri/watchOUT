from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import selenium
import codecs
import getpass
import time
import sys
from sys import stdin
#print(sys.stdin)


# Set login info
myusername=input("username: ")
mypassword=getpass.getpass("password: ")

# Open browser
browser = webdriver.Chrome()
browser.get('https://students.nyuad.nyu.edu')

# Login using selenium
username = browser.find_element_by_name("j_username")
password = browser.find_element_by_name("j_password")
username.send_keys(myusername)
password.send_keys(mypassword)
browser.find_element_by_name("_eventId_proceed").click()

time.sleep(8)

# Now in the MFA authentication page
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
iframe = browser.find_element_by_tag_name("iframe")
ac = ActionChains(browser)
ac.move_to_element_with_offset(iframe, 410, 60).click().perform()

time.sleep(8)

# Go to calendar page
browser.get('https://students.nyuad.nyu.edu/calendars/')

time.sleep(5)
