from flask import Flask, render_template
from geopy.geocoders import Nominatim
from noaa_sdk import NOAA
import time

app = Flask(__name__)
geolocator = Nominatim(user_agent="WeatherApi")

request_log = []

# Returns (lat, long) tuple from a given location
def get_coordinates(location):
    coords = geolocator.geocode(location)
    if coords:
        return coords.latitude, coords.longitude
    else:
        return None, None

# Appends requests to log
def log_request(location, status, errorMsg):
    request_log.append({
        "location": location, 
        "status": status, 
        "errorMsg": errorMsg, 
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

# Ignore favicon.ico browser requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Main route to get weather from given location
@app.route("/<location>", methods=["GET"])
def get_weather(location):
    lat, long = get_coordinates(location)
    if lat and long:
        n = NOAA()
        # Fetch forecast from NOAA SDK
        res = n.points_forecast(lat, long, type='forecast')
        log_request(location, "Success", "")
        weather = res["properties"]["periods"][0]

        # Render weather data using an HTML template
        return render_template(
            'index.html', 
            location = location, 
            temperature = weather["temperature"], 
            forecast = weather["detailedForecast"], 
            unit = weather["temperatureUnit"], 
            windSpeed = weather["windSpeed"], 
            precipitation = weather["probabilityOfPrecipitation"]["value"]), 200
    else:
        log_request(location, "Failure", "Invalid Location")
        return {"Error": "Invalid Location"}, 404

# Return 10 most recent requests in log
@app.route("/requests", methods=["GET"])
def get_requests():
    return {"requests": request_log[-10:]}

if __name__ == '__main__':
    app.run(debug=True)