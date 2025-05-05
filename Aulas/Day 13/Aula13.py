try:
    age = int(input("How old are you: "))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical number")
    age = int(input("How old are you: "))
print(age)