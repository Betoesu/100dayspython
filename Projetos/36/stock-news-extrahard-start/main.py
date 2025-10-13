STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, date

#Datetime
dia_atual = datetime.now().day
mes_atual = datetime.now().month
ano_atual = datetime.now().year

ontem = f"{ano_atual}-{mes_atual}-{dia_atual-3}"
antes_de_ontem = f"{ano_atual}-{mes_atual}-{dia_atual-4}"

#Informações da Api de Trading
load_dotenv()
api_key = os.environ['API_KEY']
parametros = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,

}
resposta = requests.get(url="https://www.alphavantage.co/query", params=parametros)
data = resposta.json()
print(data)
print(data["Time Series (Daily)"][ontem]["4. close"])



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

