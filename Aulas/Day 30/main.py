#FileNotFoundError

with open ("a_file.txt") as file:
    file.read()

#KeyError

dictionary = {"key": "value"}
value = dictionary["non_existent_key"]

#IndexError

fruitList = ["banana","Apple","Pineaple"]
fruit = fruitList[3]

#TypeError

text = "abc"
print(text + 5)


#FileNotFoundErro

try:
    file = open("file.txt")
    dictionary = {"key":"value"}
    print(dictionary["key"])
except FileNotFoundError:
    file = open("file.txt","w")
    file.write("Something")
except KeyError as errorMessage:
    print(f"That Key {errorMessage} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight/height ** 2
if height > 3:
    raise ValueError("Human Height Should not exceed 3 meters")
print(bmi)

