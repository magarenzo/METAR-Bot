# METAR Bot

Download and parse XML data from METAR

## About

Both <i>bot.py</i> and <i>script.py</i> download METAR data for an airport in XML format and parses to extract specific data. 

[<i>bot.py</i>](src/bot.py) parses the data to extract observation time and temperature in Celsius. After using simple regular expressions to rid of some unwanted pieces of information, the readings are added to a CSV file. 

[<i>script.py</i>](src/script.py) parses the data to extract station ID and temperature in Celsius. After converting the temperature to Fahrenheit, the readings are printed to standard output.

I created both of these using [Metar](https://packages.debian.org/wheezy/metar).

I use [Crontab](http://crontab.org/) for scheduling daily automation

## Output

### bot.py

`d a t e / t i m e , d e g r e e s _ c e l s i u s`<br>`2 0 1 7 - 0 8 - 1 7 - 1 4 : 5 1 : 0 0 , 2 5 . 6`

### script.py

`82.04 degrees Fahrenheit at KJFK`

## Crontab

`30 * * * * python ./bot.py`<br>`45 23 * * * mv ./data.csv ./recorded_data.csv`

## Dependencies

* [`os`](https://docs.python.org/3/library/os.html)
  
* [`csv`](https://docs.python.org/3/library/csv.html)
  
* [`urllib2`](https://docs.python.org/2/library/urllib2.html)

* [`xml`](https://docs.python.org/3/library/xml.html)
  
* [`re`](https://docs.python.org/3/library/re.html)

## Owner

Michael A. Agarenzo

This was originally created as a final project for CSC271 (Software I: Utilities and Internals) and it has undergone some changes since then
