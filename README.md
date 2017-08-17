# weather-report-automation

Download, parse and write XML data to a CSV file

---

<i>script.py</i> downloads METAR data in XML format and parses it to extract observation time and temperature in Celsius. The parsed observation time and temperature readings are then added to a CSV file. I created this script using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation. <i>crontab.txt</i> provides an example of how this automation can be set up.

---

<h3>Output:</h3>

`d a t e / t i m e , d e g r e e s _ c e l s i u s`<br>`2 0 1 7 - 0 8 - 1 7 - 1 4 : 5 1 : 0 0 , 2 5 . 6`

---

<h3>Necessary Installations:</h3>

* [`python3`](https://docs.python.org/3/)

  * [`os`](https://docs.python.org/3/library/os.html)
  
  * [`csv`](https://docs.python.org/3/library/csv.html)
  
  * [`urllib2`](https://docs.python.org/2/library/urllib2.html)

  * [`xml`](https://docs.python.org/3/library/xml.html)
  
  * [`re`](https://docs.python.org/3/library/re.html)

---

<h3>Crontab:</h3>

`0 * * * * python ./script.py`

---

This script was originally created as a final project for CSC271 (Software I: Utilities and Internals), but it has undergone changes since then.
