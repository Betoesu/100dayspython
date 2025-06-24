import random
stages = ['''   
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
     |___ ''',''' 
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |___''', ''' 
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
     |___''', '''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
     |___ ''', '''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___ ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___ ''', ''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
     |___''']


word = ["phoenix", "jett", "reyna", "raze", "yoru", "neon", "iso", "brimstone", "viper", "omen", "astra", "harbor", "clove", "breach", "sova", "skye", "kayo", "fade", "gekko", "sage", "cypher", "killjoy", "chamber", "deadlock", "vyse","classic", "shorty", "frenzy", "ghost", "sheriff", "stinger", "spectre", "bucky", "judge", "bulldog", "guardian", "phantom", "vandal", "marshal", "operator", "ares", "odin","bind", "haven", "split", "ascent", "icebox", "breeze", "fracture", "pearl", "lotus", "sunset", "saqueadora", "sentinelas da luz", "glitchpop", "ion", "champions", "prime", "oni", "netuno", "vingança de gaia", "rgx"  ]

print("--------------------WELCOME TO THE VALORANT--------------------")
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
chosen_word = random.choice(word)

blank = ""

for spaces in chosen_word:
    blank += "_"
print("")
print(blank)

game_over = False

mistakes = 0

correct_letter = []
guesses_already_made = []

while game_over == False:
    
    guess = input("Guess a letter: ").lower()
    print("")
    if guess in guesses_already_made:
        print("You Already guess the letter", guess)
        continue


    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += guess  
            correct_letter.append(guess)
             
        elif letter in correct_letter:
            display += letter

        else: 
            display += "_" 

    guesses_already_made.append(guess)

    print(display)

    if guess not in chosen_word:
            mistakes += 1
            print(f"You guessed {guess}, that is not in the word. You lose a life")
            print("")
            print(f"**********************{6 - mistakes}/6 LIVES LEFT**********************")
            print(stages[mistakes])
            print("")

    if "_" not in display:
        game_over = True
        print("YOU WIN")
    
    if mistakes == 6:
        game_over = True
        print("You lose")