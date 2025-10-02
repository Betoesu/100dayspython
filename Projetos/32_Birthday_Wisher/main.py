##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import datetime as dt
import random
import pandas as pd
import smtplib

CAMINHO_ARQUIVO_ANIVERSARIANTE = "./Projetos/32_Birthday_Wisher/birthdays.csv"

data_de_hoje = dt.datetime.now()
mes_e_dia_de_hoje = (data_de_hoje.month,data_de_hoje.day)

dados_aniversariantes = pd.read_csv(CAMINHO_ARQUIVO_ANIVERSARIANTE)
aniversarios_por_data = {(linha["month"], linha["day"]): linha for _,linha in dados_aniversariantes.iterrows()}

print(aniversarios_por_data)
# if mes_e_dia_de_hoje in aniversarios_por_data:
#     caminho_carta_aleatoria = f"./Projetos/32_Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(caminho_carta_aleatoria) as carta:
#         mensagem = carta.read()
#         mensagem.replace("[NAME]",dados_aniversariantes[])
print(mes_e_dia_de_hoje[1])