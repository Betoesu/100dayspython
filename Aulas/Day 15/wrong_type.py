def wrong_type(escolha,right_type,pergunta,idioma):
    while escolha not in right_type:
        if idioma == "portugues":
            print("Você digitou o comando errado. Tente novamente")
        elif idioma == "english":
            print("You typed the wrong comand. Try Again")
        escolha = input(pergunta).lower()
    return escolha
