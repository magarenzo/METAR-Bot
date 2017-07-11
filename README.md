# csc271-final
Final project for CSC271 (Software I)

System that downloads the latest weather report from JFK airport once an hour in XML format. Python script downloads the data and parses it to extract observation time and temperature in Celsius. After parsed, the temperature reading of each hour within a single day is added to a spreadsheet. System creates one spreadsheet for each day it is running. Crontab used for scheduling automation.
