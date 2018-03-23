import requests
import json
from requests import get

response = get("https://nyuad.nyu.edu/en/events.eventslist.upcoming.json")

#print(response.json())
rj = response.json()

result = []

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

for i in result:
    print('\n', i, '\n')