# WeatherAPI
Grabs Weather data from openweathermap.org
# Weather API to Insights

A mini data analytics project that fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/api) for multiple Australian cities, cleans and analyzes it, and produces simple visual insights.

## Features
- Connects to a public REST API using Python's `requests` library
- Parses JSON into a pandas DataFrame
- Analyzes temperatures, humidity, and pressure
- Visualizes results with matplotlib
- Produces ready-to-use PNG charts

## Tech Stack
- Python 3
- requests
- pandas
- matplotlib

## How to Run
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Clone this repo.
3. Install dependencies:
   ```bash
   pip install requests pandas matplotlib
