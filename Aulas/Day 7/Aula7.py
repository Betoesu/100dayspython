import random
word = ["alfa" , "beta", "charlie"]
chosen_word = random.choice(word)
print(chosen_word)
guess = str.lower(input("Guess a letter: "))
chosen_word_list = list(chosen_word)
position_letter = 0
for letter in range (0,len(chosen_word)):
    if guess == chosen_word[position_letter]:
        print("Right\n")
        position_letter += 1
    else:
        print("Wrong\n")
        position_letter += 1



