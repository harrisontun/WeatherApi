# WeatherApi
Simple Flask-based REST API that will fetch weather data from Noaa.gov </br>

# Installation
`pip install flask geopy noaa-sdk`</br>

# Usage
Start the server by running 
`python Weather.py`

# Endpoints
`/<location>` </br>
Will fetch and display the current weather at that location.</br>
Example: `http://127.0.0.1:5000/Miami`</br>
Returns an HTML page with weather data such as temperature, precipitation, etc.</br>

`/requests` </br>
Will fetch a log of the last 10 requests</br>
Example: `http://127.0.0.1:5000/requests`</br>
Returns a log of the last 10 requests including status, error message, timestamp, etc.</br>

# Notes
The Location input must be a valid location ie. "Denver", "Dallas,TX".<br/>
Internation locations are not covered. <br/>
Favicon requests `/favicon.ico` are ignored
