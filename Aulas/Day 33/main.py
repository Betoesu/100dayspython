# import requests

# resposta = requests.get(url="http://api.open-notify.org/iss-now.json")
# resposta.raise_for_status() 

# data = resposta.json()
# longitude = resposta.json()["iss_position"]["longitude"]
# latitude = resposta.json()["iss_position"]["latitude"]

# iss_position = (longitude,latitude)

import requests
from datetime import datetime
MY_LAT = -12.400760
MY_LONG = -46.427250

parametros = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

resposta = requests.get("https://api.sunrise-sunset.org/json", params=parametros, )
resposta.raise_for_status() #Retorna o erro em numeros Ex: 404
data = resposta.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)