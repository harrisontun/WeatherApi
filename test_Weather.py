import unittest
from unittest.mock import patch, Mock
from Weather import app, request_log

class WeatherApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        request_log.clear()  # Clean log before each test

    @patch('Weather.render_template')
    @patch('Weather.get_coordinates')
    @patch('Weather.NOAA')
    def test_valid_location(self, mock_noaa_class, mock_get_coordinates, mock_render_template):
        # Mock coordinates
        mock_get_coordinates.return_value = (41.8781, -87.6298)

        # Mock NOAA forecast response
        mock_noaa_instance = Mock()
        mock_noaa_instance.points_forecast.return_value = {
            "properties": {
                "periods": [
                    {
                        "name": "Today",
                        "temperature": 75,
                        "temperatureUnit": "F",
                        "detailedForecast": "Sunny and warm",
                        "windSpeed": "10 mph",
                        "probabilityOfPrecipitation": {"value": 15}
                    }
                ]
            }
        }
        mock_noaa_class.return_value = mock_noaa_instance

        # Mock render_template to avoid actual HTML rendering
        mock_render_template.return_value = "<html>Mocked Weather Page</html>"

        response = self.client.get("/Chicago")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mocked Weather Page", response.get_data(as_text=True))
        self.assertEqual(len(request_log), 1)
        self.assertEqual(request_log[0]["status"], "Success")

    @patch('Weather.get_coordinates')
    def test_invalid_location(self, mock_get_coordinates):
        # Mock invalid location
        mock_get_coordinates.return_value = (None, None)

        response = self.client.get("/InvalidCity")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["Error"], "Invalid Location")
        self.assertEqual(len(request_log), 1)
        self.assertEqual(request_log[0]["status"], "Failure")

    def test_requests_log_endpoint(self):
        # Add mock data to log
        request_log.append({
            "location": "TestCity",
            "status": "Success",
            "errorMsg": "",
            "timestamp": "2025-08-13 12:00:00"
        })

        response = self.client.get("/requests")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("requests", data)
        self.assertEqual(len(data["requests"]), 1)
        self.assertEqual(data["requests"][0]["location"], "TestCity")

if __name__ == "__main__":
    unittest.main()
