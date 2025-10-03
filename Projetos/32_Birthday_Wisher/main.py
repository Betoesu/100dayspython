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
MEU_EMAIL = "p07692063@gmail.com"
MINHA_SENHA = "gucnvqnohjkgogfa"

data_de_hoje = dt.datetime.now()
mes_e_dia_de_hoje = (data_de_hoje.month,data_de_hoje.day)

dados_aniversariantes = pd.read_csv(CAMINHO_ARQUIVO_ANIVERSARIANTE)
#aniversarios_por_data = {(linha["month"], linha["day"]): linha for _,linha in dados_aniversariantes.iterrows()} dessa maneira se houverem duas pessoas com mesmo aniversario o dicionario sobscreve
aniversarios_por_data = {}

for (_, linha) in dados_aniversariantes.iterrows():
    mes_e_dia_aniversário = (linha["month"], linha["day"])
    if mes_e_dia_aniversário not in aniversarios_por_data:
        aniversarios_por_data[mes_e_dia_aniversário] = []
    aniversarios_por_data[mes_e_dia_aniversário].append(linha)

if mes_e_dia_de_hoje in aniversarios_por_data:
    for pessoa in aniversarios_por_data[mes_e_dia_de_hoje]:
        nome_aniversariante = pessoa["name"]
        email_aniversariante = pessoa["email"]

        caminho_carta_aleatoria = f"./Projetos/32_Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(caminho_carta_aleatoria, encoding="utf-8" ) as carta: #<- o encoding utf 8 é para aceitar acento
            mensagem = carta.read()
            mensagem = mensagem.replace("[NAME]", nome_aniversariante)

            with smtplib.SMTP("smtp.gmail.com",port=587) as email:

                email.starttls()

                email.login(user=MEU_EMAIL, password=MINHA_SENHA)
                email.sendmail(from_addr=MEU_EMAIL,to_addrs=email_aniversariante,msg=f"Subject:Feliz Aniversario\n\n {mensagem}".encode("utf-8"))