##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import datetime as dt
import random
import pandas as pd
import smtplib

caminhoBirthdays = "./Projetos/32_Birthday_Wisher/birthdays.csv"

hoje = dt.datetime.now()
tuplaHoje = (hoje.month,hoje.day)

dadosAniversario = pd.read_csv(caminhoBirthdays)

dicionarioAniversario = 
