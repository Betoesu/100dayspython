import requests
import os 
from dotenv import load_dotenv
import json

from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ACCOUNT_SID_TWILIO = os.getenv("account_sid_twilio")
AUTH_TOKEN_TWILIO = os.getenv("auth_token_twilio")




parametros = {
    "function": "TIME_SERIES_DAILY",
    "apikey": "URQWV8OJ46IZI8LN",
    "symbol": STOCK_NAME,

}
resposta = requests.get(url=STOCK_ENDPOINT, params=parametros)
stock_data = resposta.json()["Time Series (Daily)"] 
data_list = [value for (key,value) in stock_data.items()]
print(data_list)

valor_ontem = data_list[0]
valor_fechamento_ontem = valor_ontem["4. close"]
print(valor_fechamento_ontem)


valor_antes_de_ontem = data_list[1]
valor_fechamento_antes_de_ontem = valor_ontem["4. close"]
print(valor_fechamento_antes_de_ontem)

diferenca = (float(valor_fechamento_ontem) - float(valor_fechamento_antes_de_ontem))

up_down = None
if diferenca > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diferenca_percentual = round(diferenca/float(valor_fechamento_ontem),4) * 100
    
    
    
if abs (diferenca_percentual) >= 0:
    parametros_news = {
        "q": COMPANY_NAME,
        "apiKey": "a7e93189a43846c590e193785592ba56",
    }

    resposta_news = requests.get(url=NEWS_ENDPOINT,params=parametros_news)
    news = resposta_news.json()["articles"]
    
    first_three_news = news[:3]

    formatted_articles = [f"\n{STOCK_NAME}:{up_down}{abs(diferenca_percentual)}%\nHeadline: {article["title"]}." for article in first_three_news]

    client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)
    for article in formatted_articles:
        if len(article) > 150:
            article = article[:150 - 3] + "..."
        print(len(article))
        message = client.messages.create(
                body=article,
                from_="+12293049667",
                to="+5561996370945"
            )
        print(message.status)

