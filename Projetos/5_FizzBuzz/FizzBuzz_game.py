print("Welcome to Fizz Buzz game")
print('''Basically we have all the number between 1 and 100, and for every number divisble by the number you choose will appear fizz
and for every number divisible by other number from your chose will appear buzz, and by both: FizzBuzz''')
Fizz_number = int(input("Chose your Fizz Number: "))
Buzz_number = int(input("Chose your Buzz Number: "))
for number in range(1,101):
    if number % Fizz_number == 0 and number % Buzz_number == 0:
        print("FizzBuzz")
    elif number % Fizz_number == 0:
        print("Fizz")
    elif number % Buzz_number == 0:
        print("Buzz")
    else:
        print(number)
