import sys
sys.path.append("..")
import unittest
from unittest.mock import Mock, patch
import requests
from src.api_interaction import retrieve_iss_position

class TestRetrieveISSPosition(unittest.TestCase):

    @patch('requests.get')
    def test_retrieve_iss_position_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "iss_position": {
                "latitude": "40.7128",
                "longitude": "-74.0060"
            }
        }
        mock_get.return_value = mock_response

        latitude, longitude = retrieve_iss_position()

        self.assertEqual(latitude, "40.7128")
        self.assertEqual(longitude, "-74.0060")

    @patch('requests.get')
    def test_retrieve_iss_position_request_error(self, mock_get):
        # Simulate a RequestException
        mock_get.side_effect = requests.exceptions.RequestException("Mocked Request Error")

        latitude, longitude = retrieve_iss_position()

        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

    @patch('requests.get')
    def test_retrieve_iss_position_json_error(self, mock_get):
        # Prepare a mock response with invalid JSON
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Mocked JSON Error")
        mock_get.return_value = mock_response

        latitude, longitude = retrieve_iss_position()

        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

if __name__ == '__main__':
    unittest.main()