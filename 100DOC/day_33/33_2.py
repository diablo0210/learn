import requests

my_lat = 28.459497
my_lng = 77.026634

parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)