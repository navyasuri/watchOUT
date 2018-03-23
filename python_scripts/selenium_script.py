from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import selenium
import codecs
import getpass
import time
from selenium.webdriver.common.action_chains import ActionChains
import ast
import json


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

# MFA authentication page
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
iframe = browser.find_element_by_tag_name("iframe")
ac = ActionChains(browser)
ac.move_to_element_with_offset(iframe, 410, 60).click().perform()

time.sleep(8)

# Go to calendar page
browser.get('https://students.nyuad.nyu.edu/calendars/')

time.sleep(5)

# Get the token and fetch json file
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

js_scripts = soup.find_all('script', attrs={'type': 'text/javascript'})
token = ''
for script in js_scripts:
	c = script.contents
	for line in c:
		s = str(line)
		if ('var token' in s):
			s = s[s.find('var token')+13:s.find('var token')+13+32]
			print(s)
			token = s

# Fetch json
browser.get('https://events.nyuad.nyu.edu/live/json/events/?lw_auth='+token);
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
html = str(html)
print(html)

s_html = html.split('}')

event_list = []

x = s_html[0][1:] + "}"
print(x)
y = json.loads(str(x[x.find('[')+1:]))
print(type(y))
print(y)
event_list.append(y)

for i in range(1,len(s_html)-1):
	x = s_html[i][1:] + "}"
	print(x)
	y = json.loads(str(x))
	print(type(y))
	print(y)
	event_list.append(y)

print(event_list[0])

result = []

for i in event_list:
	
	d = {}
	startdt = i['date_utc'].split(' ')
	try:
		enddt = i['date2_utc'].split(' ')
	except:
		enddt = [startdt[0], ""]	 
	d['title'] = i['title']
	d['startDate'] = startdt[0]
	d['endDate'] = enddt[0]
	d['startTime'] = startdt[1]
	d['endTime'] = enddt[1]
	d['location'] = i['location']
	if not isinstance(i['description'],str):
		d['description'] = i['description']
	else:
		d['description'] = i['title']
	d['organizer'] = i['group']
	result.append(d)

for i in result:
	print(i, '\n\n')

# Result is the full JSON file

# fp = open('myJSON.txt', 'w')
# fp.write(result)
# fp.close()

with open('myJSON.json', 'w') as fp:
    json.dump(result, fp)

# events = soup.find_all('div', attrs={'class': 'details'})
# # print(events)

# # for event in events:
# # 	print(event.txt)

# for event in events:
# 	c = event.contents
# 	for line in c:
# 		s = str(line)
# 		if (s!='\n'):
# 			print(s)

# 			# date

# 			if ('span class="italic"' in s):


# 	# print(c)
# 	# print(type(c[1]))

# 	d = {}
	
# 	d['title'] = string
# 	d['date'] = year-month-day
# 	d['startTime'] = hh:mm:ss
# 	d['endTime'] = hh:mm:ss
# 	d['location'] = string
# 	d['description'] = string
# 	d['organizer'] = string
# 	result.append(d)












