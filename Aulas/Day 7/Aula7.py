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


word = ["Phoenix","Jett","Reyna","Raze","Yoru",'Neon',"Iso", "Brimstone", "Viper", "Omen", "Astra", "Harbor", "Clove", "Breach", "Sova", "Skye", "KAYO", "Fade", "Gekko", "Sage", "Cypher", "Killjoy", "Chamber", "Deadlock", "Vyse","Classic", "Shorty", "Frenzy", "Ghost", "Sheriff", "Stinger", "Spectre", "Bucky", "Judge", "Bulldog", "Guardian", "Phantom", "Vandal", "Marshal", "Operator", "Ares", "Odin","Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Pearl", "Lotus", "Sunset","Saqueadora","Sentinelas da Luz","Glitchpop", "Ion", "Champions", "Sentinelas da Luz", "Prime","Oni", "Netuno", "Vingança de Gaia","RGX"   ]

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
            input("Press Enter to Continue")
            

    

    if "_" not in display:
        print("*****You win*****")
        game_over = True
    
    elif mistakes == 6:
         print("*****You lose*****")
         game_over = True

    

