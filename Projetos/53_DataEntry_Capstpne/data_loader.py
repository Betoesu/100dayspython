from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import time

# Número de tentativas que o programa vai tentar entrar no site
MAX_TENTATIVAS_CONEXAO = 5
WEBSITE_ENDPOINT = 'https://appbrewery.github.io/Zillow-Clone/'

def load_soup() -> BeautifulSoup:
    """
    Carrega o HTML do site e retorna um objeto BeautifulSoup
    
    :return: HTML Soup
    :rtype: BeautifulSoup
    """

    tentativas = 0

    #Maneira de evitar que o código pare antes de tentar abrir o site ao meno 5 vezes
    while  tentativas < MAX_TENTATIVAS_CONEXAO:
        try:
            response = requests.get(WEBSITE_ENDPOINT, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text,"html.parser")
            
        except RequestException as error:    
            tentativas += 1
            print(f"Tentativa {tentativas} falhou: ", error)
            time.sleep(2)
        

    raise Exception("Não foi possível acessar o site após várias tentativas")        
