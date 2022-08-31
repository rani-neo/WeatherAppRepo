import requests
import time

city = "sydney"


api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=930a99833ac6433d1c93865169ee9299"
response = requests.get(api)
data  = response.json()
temp = round(data["main"]["temp"] - 273.15)
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
sun_rise = time.strftime("%I:%M:%p",time.gmtime(data["sys"]["sunrise"]-21600))
sun_set= time.strftime("%I:%M:%p",time.gmtime(data["sys"]["sunset"]-21600))
# print(temp)
# print(pressure)
print(sun_rise)
print(sun_set)