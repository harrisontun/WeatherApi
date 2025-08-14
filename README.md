# WeatherApi
Simple Flask-based REST API that will fetch weather data from Noaa.gov

# Installation
`pip install flask geopy noaa-sdk`

# Usage
Start the server by running
`python Weather.py`

# Endpoints
/<location> - Will return the current weather from that location
/requests - Will return a log of the last 10 requests
