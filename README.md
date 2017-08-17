# weather-report-automation

Download, parse and write XML data to a CSV file

---

<i>script.py</i> downloads METAR data in XML format and parses it to extract observation time and temperature in Celsius. The parsed observation time and temperature readings are then added to a CSV file. I created this script using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation. <i>crontab.txt</i> provides an example of how this automation can be set up.

---

<h3>Output:</h3>

`2 0 1 7 - 0 8 - 1 7 T 1 2 : 5 1 : 0 0 Z`<br>`2 2 . 8`


---

<h3>Necessary Installations:</h3>

* [`python3`](https://docs.python.org/3/)

  * [`urllib2`](https://docs.python.org/2/library/urllib2.html)

  * [`xml`](https://docs.python.org/3/library/xml.html)

  * [`csv`](https://docs.python.org/3/library/csv.html)

---

<h3>To Do:</h3>

* Clean up parsed data

---

This script was originally created as a final project for CSC271 (Software I: Utilities and Internals), but it has undergone changes since then.
