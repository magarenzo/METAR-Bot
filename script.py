#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as elementTree
import csv

# Download XML data
url = urllib2.urlopen('http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KJFK&mostRecent=true&hoursBeforeNow=1')
body = url.read()

# Extract and parse XML data
data = elementTree.fromstring(body)
d = data.findall('data')

# Append parsed XML data to existing CSV file
for i in d:
        for j in i:
                with open('./data.csv', 'a') as f:
                        writer = csv.writer(f, delimiter=' ', quotechar='|')
                        writer.writerow(j.find('observation_time').text)
                        writer.writerow(j.find('temp_c').text)
