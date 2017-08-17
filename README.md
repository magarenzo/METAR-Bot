# metar-bot

Download and parse XML data from METAR, write to a CSV file

---

<i>script.py</i> downloads METAR data from an airport in XML format and parses it to extract observation time and temperature in Celsius. Those parsed readings are then added to a CSV file. I created this script using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation. [Click here](https://github.com/magarenzo/weather-report-automation/blob/master/README.md#crontab) for an example.

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

`30 * * * * python ./bot.py`<br>`45 23 * * * rm ./data.csv`

---

This script was originally created as a final project for CSC271 (Software I: Utilities and Internals). It has undergone some changes since then.
