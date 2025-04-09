import random

word = ["alfa", "beta", "charlie"]

chosen_word = random.choice(word)
print(chosen_word)
blank = []
chosen_word_list = list(chosen_word)
for letter in range (0,len(chosen_word)):
    blank.append ("_")

blank = "".join(blank)
print(blank)
blank = list(blank)

guess = input("Guess a letter: ").lower()

backcup_chosen_word_list = deepcopy(chosen_word_list)

while guess in chosen_word_list:
    if "_"  in blank:
        posicao = chosen_word_list.index(guess)
        del blank[posicao]
        blank.insert(posicao, guess)
        if "_"  in blank:
    
            if chosen_word_list.count(guess) > 1:
                del chosen_word_list[posicao]
                posicao = chosen_word_list.index(guess)
                posicao_2 = len(chosen_word_list) - posicao
                posicao = posicao + posicao_2
                del blank [posicao]
                blank.insert(posicao, guess)
            chosen_word_list = backcup_chosen_word_list
            print(blank)
            guess = (input("Guess a letter: ")).lower()
        else:
            print("You win")
    else:
        print("You win")
    


















blank = "".join(blank)
print(blank)










