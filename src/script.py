#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as elementTree
import re

# Download XML data
url = urllib2.urlopen('http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KJFK&mostRecent=true&hoursBeforeNow=1')
body = url.read()

# Extract XML data
data = elementTree.fromstring(body)
d = data.findall('data')

# Parse for wanted XML data, remove unwanted characters, and append to existing CSV file
for i in d:
        for j in i:
                location = j.find('station_id').text
                temp = j.find('temp_c').text
                cel = float(temp)
                fah = 9.0/5.0 * cel + 32.0
                print fah,'degrees Fahrenheit at',location
