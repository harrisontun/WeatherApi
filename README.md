# WeatherApi
Simple Flask-based REST API that will fetch weather data from Noaa.gov

# Installation
`pip install flask geopy noaa-sdk`

# Usage
Start the server by running
`python Weather.py`

# Endpoints
`/<location>` 
Will fetch and display the current weather at that location.
Example: `http://127.0.0.1:5000/Miami`
Returns an HTML page with weather data such as temperature, precipitation, etc.

/requests 
Will fetch a log of the last 10 requests
Example: `http://127.0.0.1:5000/requests`
Returns a log of the last 10 requests including status, error message, timestamp, etc.
