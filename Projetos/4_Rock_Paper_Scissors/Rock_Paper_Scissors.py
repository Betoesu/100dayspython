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
input("Press any button to finish")