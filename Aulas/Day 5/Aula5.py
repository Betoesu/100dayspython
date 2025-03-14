all_fruits = ["Apple", "Pineapple","Pear"]
for fruit in all_fruits:
    print(fruit)
    print(fruit + " pie")
    
student_scores = [150, 123, 142, 182, 189, 165, 161, 190]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score
print(sum)

#print(max(student_scores)) = 190

previous_score = 0
for score in student_scores:
    if score > previous_score:
        previous_score = score
print(f"The highest note is {score}")

total = 0
for number in range(1,101):
    total += number
print(total)

for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)
        
        
        
        
import random
print("Welcome to your password generator")

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","?","+","×","÷",">"]

n_l = int(input("How many letters? "))
n_n = int(input("How many numbers? "))
n_s = int(input("How many symbols? "))

password = ""
for caracterl in range (0, n_l):
	password += random.choice(letters)
for caractern in range (0, n_n):
	password += random.choice(numbers)
for caracters in range (0, n_s):
	password += random.choice(symbols)
print(password)