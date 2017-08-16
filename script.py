#!/usr/bin/python

import time
import datetime as dateTime
import urllib2
import xml.etree.ElementTree as elementTree
import csv

localtime = time.localtime(time.time())

# Download XML data
url = urllib2.urlopen('http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KJFK&mostRecent=true&hoursBeforeNow=1')
body = url.read()

# Extract and parse XML data; Add data to copied template
data = elementTree.fromstring(body)
d = data.findall('data')

for i in d:
    for j in i:
        hour = dateTime.datetime.now().hour
        hour += 2
        # Create a CSV writer object and write to the file
        with open('data.csv', 'w') as csvfile:
                dataWriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                dataWriter.writerow(j.find('observation_time').text)
                dataWriter.writerow(j.find('temp_c').text)
root@magarenzo:/home/mike/weather-report-automation#
