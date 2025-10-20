from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID_TWILIO = os.getenv("account_sid_twilio")
AUTH_TOKEN_TWILIO = os.getenv("auth_token_twilio")

print("Conectando Twilio...")

client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)
message = client.messages.create(
    body="Mensagem de teste dentro do projeto principal!",
    from_="+12293049667",
    to="+5561996370945"
)
print("Status:", message.status)
print("SID:", message.sid)
