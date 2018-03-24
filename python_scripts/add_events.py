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
with open('python_scripts/events.json', 'r') as jfile:
    text = jfile.read()
    jjson = json.loads(text)

for e in jjson:
    event = {
      'summary': e['title'],
      'location': e['location'],
      'description': e['description'],
      'start': {
        'dateTime': e['startDate'] + 'T' + e['startTime'],
        'timeZone': 'Asia/Dubai',
      },
      'end': {
        'dateTime': e['endDate'] + 'T' + (e['endTime'] if e['endTime'] else e['startTime']) ,
        'timeZone': 'Asia/Dubai',
      },
    }
#


    event = GCAL.events().insert(calendarId='nyuadeventful@gmail.com', body=event).execute()
#print 'Event created: %s' % (event.get('htmlLink'))
#}
