import requests
import pandas as pd


api_key = ""
city = 'Yangon'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

weather_raw_data = requests.get(url).json()
print(type(weather_raw_data))

print(weather_raw_data['main']['temp_max'])
print(weather_raw_data['main']['temp_min'])
print(weather_raw_data['weather'][0]['description'])