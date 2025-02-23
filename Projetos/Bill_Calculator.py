print("Welcome to your bill calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would yu like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (bill + (tip/100 * bill))/people
print(f"Each person should pay: {round(bill_per_person,2)}")