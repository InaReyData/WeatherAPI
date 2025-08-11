# weather_api_project.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --------------------
# 1. CONFIGURATION
# --------------------
API_KEY = "d01f0dbcdc25d6a45f9f0092fa0bf576"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Cities to analyze
cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]

# --------------------
# 2. FETCH DATA FROM API
# --------------------
weather_data = []

for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Get Celsius temperatures
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    weather_data.append({
        "City": city,
        "Temperature (°C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Pressure (hPa)": data["main"]["pressure"],
        "Weather": data["weather"][0]["description"],
        "Date": datetime.utcfromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
    })

# --------------------
# 3. CREATE DATAFRAME
# --------------------
df = pd.DataFrame(weather_data)

print("\n--- RAW WEATHER DATA ---\n")
print(df)

# --------------------
# 4. SIMPLE ANALYSIS
# --------------------
warmest_city = df.loc[df["Temperature (°C)"].idxmax(), "City"]
coldest_city = df.loc[df["Temperature (°C)"].idxmin(), "City"]

print(f"\nWarmest city right now: {warmest_city}")
print(f"Coldest city right now: {coldest_city}")

# --------------------
# 5. VISUALIZATION
# --------------------
plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Temperature (°C)"], color="skyblue")
plt.title("Current Temperatures by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("temperature_chart.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Humidity (%)"], color="lightgreen")
plt.title("Current Humidity by City")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("humidity_chart.png")
plt.show()
