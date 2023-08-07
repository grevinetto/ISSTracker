import requests

# Retrieve ISS latitude and longitude

def retrieve_iss_position():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()

        data = response.json()
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        return latitude, longitude

    except requests.exceptions.RequestException as e:
        print("Error making the HTTP request:", e)
        return None, None

    except ValueError as e:
        print("Error parsing JSON data:", e)
        return None, None
    
    except requests.exceptions.Timeout:
        print("Request took too long to be processed")
        return None, None
    