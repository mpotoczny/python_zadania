import json
import urllib.request
from urllib.request import Request

lokalizacja = input("Podaj lokalizację (po angielsku): ")

url1 = f'https://www.metaweather.com/api/location/search/?query={lokalizacja}'

zapytanie1 = Request(url1)

with urllib.request.urlopen(zapytanie1) as req:
    zawartosc1 = json.loads(req.read())

# print(zawartosc1)

if len(zawartosc1) == 0:
    raise ValueError("Brak takiej lokalizacji w bazie.")

# print(zawartosc1[0]['title'])
# print(zawartosc1[0]['woeid'])

id_lokalizacji = zawartosc1[0]['woeid']

url2 = f' https://www.metaweather.com/api/location/{id_lokalizacji}'
zapytanie2 = Request(url2)

with urllib.request.urlopen(zapytanie2) as req:
    zawartosc2 = json.loads(req.read())

nazwa_lokalizacji = zawartosc2['title']
data = zawartosc2['consolidated_weather'][0]['applicable_date']

the_temp = zawartosc2['consolidated_weather'][0]['the_temp']
wind_speed = zawartosc2['consolidated_weather'][0]['wind_speed']
wind_direction = zawartosc2['consolidated_weather'][0]['wind_direction']
air_pressure = zawartosc2['consolidated_weather'][0]['air_pressure']
humidity = zawartosc2['consolidated_weather'][0]['humidity']
visibility = zawartosc2['consolidated_weather'][0]['visibility']

print()
pogoda = ( f'Pogoda dla lokalizacji {nazwa_lokalizacji.upper()} na dzień {data}: \n'
         f'Temperatura: {the_temp:.2f}\n'
         f'Prędkość wiatru: {wind_speed:.2f}\n'
         f'Kierunek wiatru: {wind_direction:.2f}\n'
         f'Ciśnienie atmosferyczne: {air_pressure}\n'
         f'Wilgotność: {humidity}\n' )

print(pogoda)

