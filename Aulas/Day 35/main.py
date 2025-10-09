import requests

MY_LAT = -12.400760
MY_LNG = -46.427250
API_KEY = "21f2644aea1c72b65b49c8f6980e224e"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"


parametros = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY
}

resposta = requests.get(API_URL, params=parametros)
data = resposta.json()
print(data)
