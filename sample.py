from geolocation.main import GoogleMaps
import requests,json
import datetime
import numpy as np
import matplotlib.pyplot as plt
import mpld3



address = "Los Angeles"

google_maps = GoogleMaps(api_key='AIzaSyBCCeBBAs_GOkEphWvfpdw0VaeR-SrH-F4') 

location = google_maps.search(location=address) # sends search to Google Maps.
my_location = location.first()
print(my_location.lat)
print(my_location.lng)
url = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng)
print url
r = requests.get(url)
parseString = json.loads(r.text)

current= parseString['currently']
t= parseString['hourly']
list1=t['data']
curr= parseString['currently']
print curr

tem= curr['temperature']
currsum= curr['summary']
wind= curr['windSpeed']
print tem
print wind

#print list1

temp=[]
summary=[]
time=[]
hum=[]



for i in list1:
	temp.append(i['temperature'])
for i in list1:
	time.append(i['time'])
for i in list1:
	summary.append(i['summary'])
for i in list1:
	hum.append(i['humidity'])

#item= [t['data'][i] for i in  ]
date1=[]
for i in time:
	date1.append(datetime.datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d %H:%M:%S'))
print len(temp)
print len(summary)

width= 0.35
ind= np.arange(2)
fig, ax = plt.subplots()
rects1 = ax.bar(ind, temp, width, color='r', label='temperature')
rects2 = ax.bar(ind+width, hum, width, color='y', label='humidity')


ax.set_xticks(ind+width)
ax.set_xticklabels(time)


ax.legend(loc=0)
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
mpld3.save_html(fig,'./outbar.html')

#print date1
 # returns all locations.
