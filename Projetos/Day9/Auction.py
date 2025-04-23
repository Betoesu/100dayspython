lances = {}

print(r'''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')

print("Bem vindo ao Leilão Secreto")
mais_compradores = True
while True:
    nome = input("Digite seu Nome: ")
    valor = input("Quanto quer pagar: ")
    lances[nome] = int(valor)
    
    



   
    
    resposta = input("Vão ter mais compradores? [s][n] ").lower().strip()
    print("\n" * 100)
    while resposta not in ["s", "n"]:
        print("Você digitou a resposta errada")
        resposta = input("Vão ter mais compradores? [s][n] ").lower().strip()
        print("\n" * 100)
        
    if resposta == "n":
        break



lance_anterior = lances[nome]
for nome_lance in lances:
    if lances[nome_lance] > lance_anterior:
        maior_lance = lances[nome_lance]
        vencedor = nome_lance
        lance_anterior = lances[nome_lance]
    else:
        lance_anterior = lances[nome_lance]
        continue
        
print(f"O vencedor é {vencedor} com o lance de R$ {maior_lance} ")
    
    