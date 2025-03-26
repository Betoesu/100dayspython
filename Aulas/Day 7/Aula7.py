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
<<<<<<< HEAD
print(guess)
for letter in range (0,len(chosen_word)):
    if guess == chosen_word[letter]:
        print(guess + line)
        letter += 1
    else:
        print(line)
        letter += 1
=======
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









>>>>>>> 30511a43060d3ebfb3e7155b69555d11cb94942d


