import random as r
random_intenger = r.randint(1,10)
print(random_intenger)


import test
print(test.nome)
#import is a way of bring data or done codes for your code, in ther case above, I import the name of the code and next
#print the name of the code and de variable that are in the other code

import random
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1,10)

print('''Welcome to Head and Tails
Press anything to start''')
import random   
heads_tails = random.randint(1,2)
if heads_tails == 1:
    print("Heads")
else:
    print("Tails") 
    
    
Nba_Teams = ["Lakers", "Warriors","Heat","Celtics"]

print(Nba_Teams[0]) 
Nba_Teams[0] = "Los Angeles Lakers"
print(Nba_Teams[0])

Nba_Teams.append("Wolves")
print(Nba_Teams[4])


friends = ["Pedro","Samuel","Felipe","Afranio","Diogo","Rodrigo","João Caio"]
import random
number_person = random.randint(0,6)
print("The person who will pay is",friends[number_person]) #or print(random.choice(friends))

homens_aula = ["Pedro","Jose" , "Igor" , "Emilly"]
mulheres_aula = ["Giovana","Emilly"]

sala_aula_separada_por_genero = [homens_aula,mulheres_aula]
print(sala_aula_separada_por_genero)

Nba_Teams = ["Lakers", "Warriors","Heat","Celtics"]
fut_teams = ["Santos", "Flamengo","Botafogo"]
Teams = [Nba_Teams,fut_teams]
print(Teams[0][2])


Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
options = [Rock,Paper,Scissors]

person_random = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
print(options[int(person_random)])

print("Computer chose:")
computer_random = random.randint(0,2)
print(options[computer_random])

if int(person_random) == computer_random:
    print("Draw")
elif person_random == "0" and computer_random == 1:
    print("You lose")
elif person_random == "0" and computer_random == 2:
    print("You win")
elif person_random == "1" and computer_random == 0:
    print("You win")
elif person_random == "1" and computer_random == 2:
    print("You lose")
elif person_random == "2" and computer_random == 0:
    print("You lose")
elif person_random == "2" and computer_random == 1:
    print("You win")