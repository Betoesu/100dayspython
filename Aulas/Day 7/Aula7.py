import random
word = ["alfa" , "beta", "charlie"]
chosen_word = random.choice(word)
print(chosen_word)
number_spaces = len(chosen_word)
blank = []
for b in range (0,number_spaces):
    blank.append ("_")
line = "".join(blank)
print(line)
guess = str.lower(input("Guess a letter: "))
print(guess)
for letter in range (0,len(chosen_word)):
    if guess == chosen_word[letter]:
        print(guess + line)
        letter += 1
    else:
        print(line)
        letter += 1


