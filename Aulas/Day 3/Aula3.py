print("Welcome to rollercoaster")
height = int(input("What is your height in cm? ")
             )
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age <= 12:
        print("$5 Please")
    elif age > 12 and age <= 18:
        print("$7 Please")   
    else:
        print("$12 Please")
       
else:
    print("Sorry you have to grow taller before you can ride")
    


 
print("Welcome to the Odd or Even!!!")
number = int(input("Type a number: "))

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
    



    
 