from __future__ import print_function
import googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = build('calendar', 'v3', http=creds.authorize(Http()))

#for each event in JSON:
event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2018-03-27T09:00:00-07:00',
    'timeZone': 'Asia/Dubai',
  },
  'end': {
    'dateTime': '2018-03-27T17:00:00-07:00',
    'timeZone': 'Asia/Dubai',
  },
}

event = GCAL.events().insert(calendarId='nyuadeventful@gmail.com', body=event).execute()
#print 'Event created: %s' % (event.get('htmlLink'))
#}
