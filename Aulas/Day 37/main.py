import requests
from datetime import datetime

USERNAME = "betoesu"
TOKEN = "asdfn32sadsad"
ID = "grafico1"

pixela_url = "https://pixe.la/v1/users"

parametros_do_usuario = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# resposta = requests.post(url=pixela_url, json=parametros)
# print(resposta.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

parametros_do_grafico = {
    "id": ID,
    "name": "Grafico de Treino",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}


# resposta =  requests.post(url=graph_url, json=parametros_do_grafico, headers=headers)
# print(resposta.text)

pixel_url = f"{pixela_url}/{USERNAME}/graphs/{ID}"

today = datetime(year=2025,month=10,day=12)


parametros_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120",
}


# resposta = requests.post(url=pixel_url, json=parametros_pixel, headers=headers )
# print(resposta.text)