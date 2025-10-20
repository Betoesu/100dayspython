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
today = datetime.now()


parametros_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Quanto tempo teve de exercício físico hoje? "),
}


resposta = requests.post(url=pixel_url, json=parametros_pixel, headers=headers )
print(resposta.text)

update_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{ID}/{parametros_pixel['date']}"


new_pixel_update = {
    "quantity": "140"
}
# resposta = requests.put(url=update_pixel_url, json=new_pixel_update, headers=headers)
# print(resposta.text)

delete_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{ID}/{parametros_pixel['date']}"

# resposta = requests.delete(url=delete_pixel_url, headers=headers)
# print(resposta.text)