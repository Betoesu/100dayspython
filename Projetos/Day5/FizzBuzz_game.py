print("Welcome to Fizz Buzz game")
print('''Basically we have all the number between 1 and 100, and for every number divisble by the number you choose will appear fizz
and for every number divisible by other number from your chose will appear buzz, and by both: FizzBuzz''')
input("Press Enter to Start")
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)