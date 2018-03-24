from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import os

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = build('calendar', 'v3', http=creds.authorize(Http()))

#for each x in JSON:
# jfile = json.loads(open('../events.json', 'r'))
jjson = []
res = []
with open('python_scripts/events.json', 'r') as jfile:
    text = jfile.read()
    jjson = json.loads(text)

template = '''BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
BEGIN:VEVENT
SUMMARY:{title}
DTSTART;TZID=Asia/Dubai:{start}
DTEND;TZID=Asia/Dubai:{end}
LOCATION:{location}
DESCRIPTION: {description}
STATUS:CONFIRMED
SEQUENCE:3
BEGIN:VALARM
TRIGGER:-PT10M
DESCRIPTION:{alarm}
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR'''

for e in jjson[:10]:
    og = e
    event = {
      'summary': e['title'],
      'location': e['location'],
      'description': e['description'],
      'start': {
        'dateTime': e['startDate'] + 'T' + e['startTime'],
        'timeZone': 'Asia/Dubai',
      },
      'end': {
        'dateTime': e['endDate'] + 'T' + e['endTime'] ,
        'timeZone': 'Asia/Dubai',
      },
    }

    data = {
	    'title': event['title'],
	    'start': event['startDate'].replace('-', '') + 'T' + event['startTime'].replace(':', '').replace('.', '')[:-2],
	    'end': event['endDate'].replace('-', '') + 'T' + event['endTime'].replace(':', '').replace('.', '')[:-2],
	    'location': event['location'],
	    'description': event['description'],
	    'alarm': 'watch out'
	}

	fdata = template.format(**data)

    event = GCAL.events().insert(calendarId='nyuadeventful@gmail.com', body=event).execute()
    og['link'] = event.get('htmlLink')
    og['cal'] = fdata
    res.append(og)



with open('linked_events.json', 'w', encoding='utf-8') as fin:
    json.dump(res, fin)
#}
