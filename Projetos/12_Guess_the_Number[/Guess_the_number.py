import random
def wrong_type(escolha):
    while escolha not in ["easy", "hard"]:
        print("You typed the wrong command")
        escolha = input("Choose a difficulty: Type 'easy' or 'hard': " ).lower()
    return escolha


print('''
   _____                       _   _                                  _                
  / ____|                     | | | |                                | |               
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    
                                                                                       
                                                                                       
 ''')

number = random.randint(1,100)
print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100.") 
dificulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
dificulty = wrong_type(dificulty)
if dificulty == "easy":
    print("You have 10 attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    for attempts in range(10, 1, -1):

        if guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            exit()
        print(f"You Have {attempts - 1} attempts remaining")
        guess = int(input("Guess again: "))
    print("You've run out attempts")
    
elif dificulty == "hard":
    print("You have 5 attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    for attempts in range(5, 1, -1):

        if guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            exit()
        print(f"You Have {attempts - 1} attempts remaining") 
        guess = int(input("Guess again: "))
    print("You've run out attempts")
        