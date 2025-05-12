def wrong_type(escolha,right_type,pergunta):
    while escolha not in right_type:
        print("Você digitou o comando errado. Tente novamente")
        escolha = input(pergunta).lower()
    return escolha
