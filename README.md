# metar-bot

Download and parse XML data from METAR, write to a CSV file or standard output

---

Both <i>bot.py</i> and <i>script.py</i> download METAR data for an airport in XML format and parses it to extract specific data. 

<i>bot.py</i> parses the data to extract observation time and temperature in Celsius. After using simple regular expressions to rid of some unwanted pieces of information, the readings are added to a CSV file. 

<i>script.py</i> parses the data to extract station ID and temperature in Celsius. After converting the temperature to Fahrenheit, the readings are printed to standard output.

I created both of these using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation. [Click here](https://github.com/magarenzo/weather-report-automation/blob/master/README.md#crontab) for an example.

---

<h3>Output:</h3>

<h5><i>bot.py</i>:</h5>
`d a t e / t i m e , d e g r e e s _ c e l s i u s`<br>`2 0 1 7 - 0 8 - 1 7 - 1 4 : 5 1 : 0 0 , 2 5 . 6`

<h5><i>script.py</i>:</h5>
`82.04 degrees Fahrenheit at KJFK`

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

`30 * * * * python ./bot.py`<br>`45 23 * * * mv ./data.csv ./recorded_data.csv`

---

This script was originally created as a final project for CSC271 (Software I: Utilities and Internals). It has undergone some changes since then.
