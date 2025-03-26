import random
word = ["alfa" , "beta", "charlie"]
chosen_word = random.choice(word)
print(chosen_word)
guess = str.lower(input("Guess a letter: "))
blank = []
chosen_word_list = list(chosen_word)
print(chosen_word_list)
for letter in range (0,len(chosen_word)):
    blank.append ("_")
    if guess == chosen_word[letter]:
        del chosen_word_list[letter]
        chosen_word_list.append(guess)

blank = "".join(blank)
print(blank)











