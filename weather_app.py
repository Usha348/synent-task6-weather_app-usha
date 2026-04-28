import requests

api_key="ebe47724745a9bdacbf982546a65b8f5"

city=input("Enter the city name: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response=requests.get(url)

data=response.json()

if data["cod"]==200:
    temp=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    weather=data["weather"][0]["description"]

    print("Temperature:", temp, "°C")
    print("Humidity:", humidity)
    print("Weather:", weather)
else:
    print("city not found")