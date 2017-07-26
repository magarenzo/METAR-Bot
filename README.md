# weather-report-automation
Download, parse and write XML data to a spreadsheet

---

Python script that downloads and parses data in XML format. Data can then be written to a spreadsheet.

---

This system was specifically made to download the latest weather report from JFK airport once an hour in XML format. Python script downloads the data and parses it to extract observation time and temperature in Celsius. After parsed, the temperature reading of each hour within a single day is added to a spreadsheet. System creates one spreadsheet for each day it is running. Crontab used for scheduling all automation.

---

Created as a final project for CSC271.
