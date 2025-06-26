from typing import Any
from mcp.server.fastmcp import FastMCP
import requests
import os

# Initialize FastMCP server
mcp = FastMCP("weather", dependencies=["requests"])

# Convert Celsius to Fahrenheit.
def temperature_conversion(celsius, unit):
	"""
	Returns temperature in Fahrenheit (float) or Celsius (float).
	"""
	if unit == "imperial":
		fahrenheit = (celsius * 9/5) + 32
		return fahrenheit
	else:
		return celsius

# Get the current weather for a city.
@mcp.tool()
def get_weather(city: str, unit: str = "imperial") -> dict[str, Any]:
	"""
	Get current weather for a city.
	"""

	# Get the API key from environment variables.
	api_key = os.getenv("OPENWEATHER_API_KEY")

	# Get the latitude and longitude of the city.
	geo_url = (
		f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
	)
	geo_data = requests.get(geo_url).json()
	lat = geo_data[0]["lat"]
	lon = geo_data[0]["lon"]

	# Get the current weather for the location.
	weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
	weather_data = requests.get(weather_url).json()
	temperature = weather_data["main"]["temp"]
	description = weather_data["weather"][0]["main"]

	return {
		"city": city,
		"latitude": lat,
		"longitude": lon,
		"temperature": temperature_conversion(temperature, unit),
		"description": description,
	}

# Run the MCP server.
if __name__ == "__main__":
	mcp.run()
