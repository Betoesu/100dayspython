#Subscripting
print("Hello"[4]) 

#Intenger == Inteiro
print(32_332_312+12_202_021) #When we have large numbers like up there we can use underline ex: 100_000_000 == 100000000

#Float == Racionais
print(3.1334 + 3.1334)

#Boolean
print(True)
print(False)

print(type(123.2))
print(type(123))
print(type("Oii"))
print(type(True))

print(int("123") + int("123"))
int()
float()
str()
bool()


#print ("Number of letters in your name: "+ len(input("Enter your name: "))) fix the error


print ("Number of letters in your name: " + str(len(input("Enter your name: "))))
print(10 + 10) 
print(10 - 10)
print(10 * 10)
print(10/2) #Division Float
print(10//2) #Division Intenger
print(2**3) #Exponent

print(round(12/7))

# +=
# -=
# *=
# /=
# This is when you need to chance a value of a variable like this: score = 0. MAKES A SCORE, instead doing this == score = score + 1, you can do this, score += 1

#f-strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score} and your height is {height}") 



print("Welcome to your bill calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would yu like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (bill + (tip/100 * bill))/people
print(f"Each person should pay: {round(bill_per_person,2)}")