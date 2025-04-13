print("Welcome to the Freedy Fazbear Pizzaria")
bill = 0
size = input("Which size of pizza do you want? Small, Medium or Large (S, M or L): ")
if size == "S":
    bill += 15
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 2 
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1   
elif size == "M":
    bill += 20
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 3
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1     
elif size == "L":
    bill += 25
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 3
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1   
else:
    print("You typed the wrongs inputs")    
print(f"Your final bill is R${bill}")