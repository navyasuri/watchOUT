import json

fp = open('events.json' , 'r')
fdata = fp.read()
fj = json.loads(fdata)

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

j = 1
for event in fj:

	data = {
	    'title': event['title'], 
	    'start': event['startDate'].replace('-', '') + 'T' + event['startTime'].replace(':', '').replace('.', '')[:-2], 
	    'end': event['endDate'].replace('-', '') + 'T' + event['endTime'].replace(':', '').replace('.', '')[:-2], 
	    'location': event['location'], 
	    'description': event['description'], 
	    'alarm': 'watch out'
	}

	res = template.format(**data)

	outfile = 'icals\cal_eventId_' + str(j) + '.ics'
	newf = open(outfile, 'w', encoding='utf-8')
	newf.write(res)
	newf.close()
	j+=1

fp.close()