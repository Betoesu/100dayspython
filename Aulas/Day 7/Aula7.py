import random

word = ["alfa" , "beta", "charlie"]

chosen_word = random.choice(word)
print(chosen_word)
blank = []
chosen_word_list = list(chosen_word)
x = 1

guess = str.lower(input("Guess a letter: "))
for letter in range (0,len(chosen_word)):
    blank.append ("_")
    if guess == chosen_word[letter]:
        del blank[letter]
        blank.append(guess)
contador = 0

        







blank = "".join(blank)
print(blank)











