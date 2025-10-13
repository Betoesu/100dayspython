import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = -12.400760
MY_LNG = -46.427250
WHEATER_API_KEY = "21f2644aea1c72b65b49c8f6980e224e"
WHEATER_API_URL = "https://api.openweathermap.org/data/2.5/forecast" 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


parametros = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": WHEATER_API_KEY,
    "cnt": 4,
}


resposta = requests.get(WHEATER_API_URL, params=parametros)
resposta.raise_for_status()
clima_data = resposta.json()


vai_chover = False
for n_dict in range(0,4):
    id_weather = clima_data["list"][n_dict]["weather"][0]["id"]
    
    if id_weather < 700:
        vai_chover = True
if vai_chover:
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
    body="Vai chover hoje, Leve um Guarda Chuva☂️",
    from_="+12293049667",
    to="+5561996370945",
)

    print(message.status)
    
