# import smtplib

# my_email = "p07692063@gmail.com"
# password = "gucnvqnohjkgogfa"

# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:

#     connection.starttls()

#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="p07692063@yahoo.com",
#                         msg="Subject:Hello\n\n" \
#                         "This is the body of my email")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# dayWeek = now.weekday()
# print(dayWeek)

# dateBirth = dt.datetime(year=2006,month=12,day=14)
# print(dateBirth)

import pandas as pd

caminhoFrases = "./Aulas/Day 32/quotes.txt"

with open(caminhoFrases,mode="r") as frases:
        
        frase = frases.read()
        print(frase).strip()
        