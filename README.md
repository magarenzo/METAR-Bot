# weather-report-automation

Download, parse and write XML data to a spreadsheet

---

<i>script.py</i> downloads the data and parses it to extract observation time and temperature in Celsius. After parsed, the temperature reading of each hour within a single day is added to a spreadsheet. System creates one spreadsheet for each day it is running. I created this script using [urllib2](https://docs.python.org/2/library/urllib2.html) and [OpenPyXL](https://openpyxl.readthedocs.io/en/default/).

I use [Crontab](http://crontab.org/) for scheduling daily automation. <i>crontab.txt</i> provides an example of how this automation can be set up.

---

<h3>Necessary Installations:</h3>

[`python2`](https://docs.python.org/2/)

[`urllib2`](https://docs.python.org/2/library/urllib2.html)

[`openpyxl`](https://openpyxl.readthedocs.io/en/default/)

---

Created for a final project assignment for CSC271 (Software I: Utilities and Internals).
