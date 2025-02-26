# print and imput, they are both functions
print("Hello World" + " " + "Bye World") # The + can bring together two different strings (a string its basically everything that will appear in quotes(""))
# Concatenation its the name
input("Whats your name? ") 
print("Hello " + input("What is your name? ") + "!") # The insider parentheses will always happen first

#variables
petname = input("what is your pet name? ")
print(petname, "has" ,len(petname), "letters") # You can't bring together a str with another thing that isn't a str, 
# in these cases you need to use a comma(,)

# Make your code readble, make it beautiful. Cause if you come back and dont organize your code, you will be confused

print("Hello, Welcome to The Band Name Generator")
city = input("Tell me the name of the city where you grow up?:\n")
petname = input("What is your pet name?\n")
print("Your Band Name is:\n" , city, petname)
