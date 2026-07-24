from datetime import datetime
from config import WEATHER_API_KEY
import requests
from langchain.tools import tool

@tool
def get_current_time():
    """
    Returns the current date and time as a string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@tool
def weather_tool(location):
    """
    Return current weather information for a given location using the OpenWeatherMap API.
    """
    api_key = WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current temperature in {location} is {temperature}°C with {description}."
    else:
        return f"Could not retrieve weather data for {location}. Please check the location name and try again."