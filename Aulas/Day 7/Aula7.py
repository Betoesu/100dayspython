import random

def tem_item_repetido(lista):
    return len(lista) != len(set(lista))




word = ["alfa"]

chosen_word = random.choice(word)
print(chosen_word)
blank = []
chosen_word_list = list(chosen_word)
for letter in range (0,len(chosen_word)):
    blank.append ("_")

blank = "".join(blank)
print(blank)
blank = list(blank)

guess = str.lower(input("Guess a letter: "))

backcup_chosen_word_list = chosen_word_list.copy()
while guess in chosen_word_list:
    posicao = chosen_word_list.index(guess)
    del blank[posicao]
    blank.insert(posicao, guess)
    lista = chosen_word_list
    if tem_item_repetido(lista) == True:
        del chosen_word_list[posicao]
        posicao = chosen_word_list.index(guess)
        posicao_2 = len(chosen_word_list) - posicao
        posicao = posicao + posicao_2
        del blank [posicao]
        blank.insert(posicao, guess)
    chosen_word_list = backcup_chosen_word_list
    print(blank)
    guess = str.lower(input("Guess a letter: "))
    









