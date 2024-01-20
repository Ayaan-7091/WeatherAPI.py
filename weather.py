import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY="bce8f81170fb157c484394cdbb54db16"

city = input("Enter city name : ")

# url = "https://api.openweathermap.org/data/2.5/weather?q=London,&APPID=bce8f81170fb157c484394cdbb54db16"
url = BASE_URL + "q=" + city + ",&APPID="+API_KEY


response = requests.get(url).json()
# print(response)

temp = response['main']['temp']
temp_min = response['main']['temp_min']
temp_max = response['main']['temp_max']
weather = response['weather'][0]['main']
description = response['weather'][0]['description']
feels_like = response['main']['feels_like']
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']

print(f"Weather in Mumbai: {weather}, {description}")

print(f"The temperature in {city}: {temp} K")
print(f"Temperature in {city} feels like: {feels_like} k")
print(f"Minimum temperature: {temp_min}k")
print(f"Maximum temperature: {temp_max}k")


print(f"Humidity: {humidity} %")
print(f"Wind-speed: {wind_speed}m/s")

