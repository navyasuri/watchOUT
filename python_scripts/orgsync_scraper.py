import requests
from requests import get

response = get("https://api.orgsync.com/api/v3/communities/751/events?key=GGsN7qUoYx1G_v8B3CmLWHP0AmdnvK0ATTpcjYGL-3s&upcoming=true&page=1&per_page=100&after=2018-03-23T12%3A51%3A04.349Z&before=2020-03-23T12%3A51%3A04.349Z&include_opportunities=true")

#print(response.json())
rj = response.json()

result = []

for i in rj['data']:
    if len(i['dates']) == 1:
        d = {}
        startdt = i['dates'][0]['starts_at'].split('T')
        enddt = i['dates'][0]['ends_at'].split('T')
        d['title'] = i['title']
        d['date'] = startdt[0]
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
            d['date'] = startdt[0]
            d['startTime'] = startdt[1][:-1]
            d['endTime'] = enddt[1][:-1]
            d['location'] = i['location']
            d['description'] = i['description']
            d['organizer'] = i['portal']['name']
            result.append(d)
            x += 1
    
fp = open('myJSON.txt', 'w')
fp.write(result)
fp.close()
