# weather-report-automation

Download, parse and write XML data to a CSV file

---

<i>script.py</i> downloads METAR data and parses it to extract observation time and temperature in Celsius. The parsed observation time and temperature readings are then added to a CSV file. I created this script using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation. <i>crontab.txt</i> provides an example of how this automation can be set up.

---

<h3>Necessary Installations:</h3>

* [`python3`](https://docs.python.org/3/)

  * [`time`](https://docs.python.org/3/library/time.html)

  * [`datetime`](https://docs.python.org/3/library/datetime.html)

  * [`urllib2`](https://docs.python.org/2/library/urllib2.html)

  * [`xml`](https://docs.python.org/3/library/xml.html)

  * [`csv`](https://docs.python.org/3/library/csv.html)

---

<h3>To Do:</h3>

* Clean up parsed data

---

Created as a final project for CSC271 (Software I: Utilities and Internals).
