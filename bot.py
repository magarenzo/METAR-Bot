#!/usr/bin/python

import os.path
import csv
import urllib2
import xml.etree.ElementTree as elementTree
import re

path = './data.csv'

# If file does not exist, create it and add the header
value = os.path.exists(path)
if (value == False):
        f = open(path, 'w+')
        with open(path, 'w') as f:
                writer = csv.writer(f, delimiter=' ')
                writer.writerow('date/time,degrees_celsius')

# Download XML data
url = urllib2.urlopen('http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KJFK&mostRecent=true&hoursBeforeNow=1')
body = url.read()

# Extract XML data
data = elementTree.fromstring(body)
d = data.findall('data')

# Parse for wanted XML data, remove unwanted characters, and append to existing CSV file
for i in d:
        for j in i:
                with open(path, 'a') as f:
                        writer = csv.writer(f, delimiter=' ')
                        time = j.find('observation_time').text
                        time = re.sub('T', '-', time)
                        time = re.sub('Z', '', time)
                        temp = j.find('temp_c').text
                        writer.writerow(time + ',' + temp)
