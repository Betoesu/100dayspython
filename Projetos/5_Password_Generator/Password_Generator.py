import random
print("Welcome to your password generator")

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","?","+","×","÷",">"]

n_l = int(input("How many letters? "))
n_n = int(input("How many numbers? "))
n_s = int(input("How many symbols? "))

password_list = []
for caracter in range (0, n_l):
	password_list += random.choice(letters)
for caracter in range (0, n_n):
	password_list += random.choice(numbers)
for caracter in range (0, n_s):
	password_list += random.choice(symbols)
random.shuffle(password_list)


password = ""
for caracter in password_list:
    password += caracter

print(f"Your password is {password}")