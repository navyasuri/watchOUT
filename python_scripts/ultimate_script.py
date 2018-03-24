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
from requests import get


###########################################
	# StudentPortal LOGIN is below
###########################################


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


###########################################
	# Student Portal Scraper is below
###########################################


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


###########################################
	# OrgSync Scraper is below
###########################################

response = get("https://api.orgsync.com/api/v3/communities/751/events?key=GGsN7qUoYx1G_v8B3CmLWHP0AmdnvK0ATTpcjYGL-3s&upcoming=true&page=1&per_page=100&after=2018-03-23T12%3A51%3A04.349Z&before=2020-03-23T12%3A51%3A04.349Z&include_opportunities=true")

#print(response.json())
rj = response.json()

for i in rj['data']:
    if len(i['dates']) == 1:
        d = {}
        startdt = i['dates'][0]['starts_at'].split('T')
        enddt = i['dates'][0]['ends_at'].split('T')
        d['title'] = i['title']
        d['startDate'] = startdt[0]
        d['endDate'] = enddt[0]
        d['startTime'] = startdt[1][:-1]
        d['endTime'] = enddt[1][:-1]
        d['location'] = i['location']
        d['description'] = i['description']
        d['organizer'] = i['portal']['name']
        result.append(d)

    else:
        x = 0
        while x<len(i['dates']):
            d = {}
            startdt = i['dates'][x]['starts_at'].split('T')
            enddt = i['dates'][x]['ends_at'].split('T')
            d['title'] = i['title']
            d['startDate'] = startdt[0]
            d['endDate'] = enddt[0]
            d['startTime'] = startdt[1][:-1]
            d['endTime'] = enddt[1][:-1]
            d['location'] = i['location']
            d['description'] = i['description']
            d['organizer'] = i['portal']['name']
            result.append(d)
            x += 1
            

###########################################
	# NYUAD Website Scraper is below
###########################################


response = get("https://nyuad.nyu.edu/en/events.eventslist.upcoming.json")

#print(response.json())
rj = response.json()

for i in rj['result']:
    d = {}
    startdt = i['startDate'].split('T')
    try:
        enddt = i['endDate'].split('T')
    except:
        enddt = [startdt[0], ""]
    d['title'] = i['eventTitle']
    d['startDate'] = startdt[0]
    d['endDate'] = enddt[0]
    d['startTime'] = startdt[1][:-1]
    d['endTime'] = enddt[1][:-1]
    d['location'] = "unknown"
    d['description'] = i['eventTitle']
    d['organizer'] = "unknown"
    for e in result:
        if e['title'] == d['title']:
            if e['startDate'] == e['endDate']:
                # it's a duplicate so we will not add this element, just continue
                continue
    result.append(d)


#################################################
	# Combine everything and write to JSON
#################################################

sorted_result = sorted(result, key = lambda k: k['startDate'])

with open('events.json', 'w') as fp:
    json.dump(sorted_result, fp)
