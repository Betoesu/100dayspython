from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

#Aqui eu carrego dados mais sensíveis no .env e trago para ca
load_dotenv()
EMAIL = os.getenv("email")
SENHA = os.getenv("password")

#Aqui estabeleço o site que desejo ir e as minhas informações(headers) para que eu não pareça um bot
url = "https://www.amazon.com.br/Sapatilha-Neoprene-Flex%C3%ADvel-Aqu%C3%A1tica-Cachoeira/dp/B0C3SC8DZW/ref=sr_1_3_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=19LV1OEYQ04N6&dib=eyJ2IjoiMSJ9.2LzZFVTBxsX5Z6niTK0CDYgvoxdV3BjjMU8Ghu6sOTPMB7O9fYlH9sbV5GOcTYjaBb_BBVZHufMF_NfF3DQsZkrmdcSdJdDKNzUEm58U5y5yyxCEw56ShrswANLN9Y9Y8of4bJ0GgVFPLfuGLMk87K_GxdMgBCskpQO10k00FupKAOwcoPh8gAiIPmhhhOtCrR5o5Y98FIyA4ooMqjCMcB-kWIBmpG5gHUsGV6gCkvPtib6hSEP8Vjk7J4BYpRS9du1TAv9jX_XSNBUTIKOI7QBw40cldiZbfIc3kw8ZOQY.vEQ2VbHhIeM7y2NkGYO3oaEKecn_ekQKg9pFwdMyKfQ&dib_tag=se&keywords=sapatilha%2Btrilha%2Be%2Bcachoeira&qid=1761745210&sprefix=sapatilha%2Btrilha%2Be%2Bcachoeira%2Caps%2C637&sr=8-3-spons&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"
header = {"Accept-Language" : "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,it;q=0.6,es;q=0.5",
          "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}


#Aqui entro no site e pego o preço e o nome do item que desejo
response = requests.get(url, headers=header)
amazon_webpage = response.content
soup = BeautifulSoup(amazon_webpage,"html.parser")

int_price = soup.find(name="span", class_="a-price-whole")
decimal_price = soup.find(name="span", class_="a-price-fraction")

price = float(int_price.getText().replace(",",".") + decimal_price.getText())
print(price)

name_product = soup.find(name="span", id="productTitle").get_text().strip()
print(name_product)

PRECO_DESEJADO = 60

#Aqui mando um email caso o preço esteja abaixo do meu desejado
if price <= PRECO_DESEJADO:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=EMAIL,password=SENHA)
    connection.sendmail(from_addr=EMAIL,to_addrs="pedrosarmento1412@gmail.com",msg=f"Subject: DESCONTO\n\n {name_product} ESTÁ POR R${price}\n {url}".encode('utf8'))
    