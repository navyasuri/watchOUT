import json

fp = open("events.json", 'r')
fdata = fp.read()
fj = json.loads(fdata)

template = '''
BEGIN:VCALENDAR
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
END:VCALENDAR
'''
event = fj[2]
data = {
    'title': event['title'], 
    'start': event['startDate'].replace('-', '') + 'T' + event['startTime'].replace(':', '').replace('.', '')[:-2], 
    'end': event['endDate'].replace('-', '') + 'T' + event['endTime'].replace(':', '').replace('.', '')[:-2], 
    'location': event['location'], 
    'description': event['description'], 
    'alarm': 'watch out'
}

fp.close()
res = template.format(**data).strip()
resol = res.replace('\n', '')

print(res)

newf = open('mycal.ics', 'w')
newf.write(resol)
newf.close()