import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -12.400760 # Your latitude
MY_LONG = -46.427250 # Your longitude
MEU_EMAIL = "p07692063@gmail.com"
MINHA_SENHA = "gucnvqnohjkgogfa"


def IsCloseToMe():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude >= MY_LAT-5 and iss_latitude <= MY_LAT+5 and iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5:
        return True
    else:
        return False



def IsDark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data = response_sun.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    

    time_now = datetime.now()
    hour_now = time_now.hour


    if hour_now >= sunset and hour_now <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if IsDark() and IsCloseToMe():
        print("Message send")
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=MEU_EMAIL,password=MINHA_SENHA)
        connection.sendmail(from_addr=MEU_EMAIL,to_addrs="pedrosarmento1412@gmail.com",msg="Subject: OLHE PARA CIMA!!!\n\n Um drone da ISS está passando por cima de você")





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



