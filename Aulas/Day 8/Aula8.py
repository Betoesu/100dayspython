def greet_me (name):
    print("Hello ", name)
    print("I see you, ", name)
    print("Whaha ", name)

def life_in_weeks(age):
    age = 90 - int(age)
    weeks = int(age) * 52
    print(f"You have {weeks} weeks left.")

def calculate_love_score(name_1, name_2):
    true = 0
    love = 0
    for letters in name_1.lower():
        if letters in ["t","r","u","e"]:
            true += 1
        if letters in ["l","o","v","e"]:
            love += 1

    for letters in name_2.lower():
        if letters in ["t","r","u","e"]:
            true += 1
        if letters in ["l","o","v","e"]:
            love += 1

    print(str(true) + str(love))


greet_me("Pedro")

life_in_weeks(input("How old are you? "))



calculate_love_score("Kanye West", "Kim Kardashian")
    
    
def encrypt(message,number): 
    crypt_message = ""
    if decode_or_encode == "decode":
        number *= -1
    for letter in message:

        if letter not in alphabet:
            crypt_message += letter
        else:  
            position = alphabet.index(letter)
            position_number = position + number
            if position_number > 25:
                position_number -= 26

            letter = alphabet[position_number]
            crypt_message += letter
    print(crypt_message)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


keep_going = True

while keep_going == True:
    decode_or_encode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if (decode_or_encode == "encode") or (decode_or_encode == "decode"):
        message = input("Type your message: ").lower()
        number = int(input("Type your shift number: "))
        encrypt(message,number)

    
    else:
        print("")
        print('''You type the wrong command.''')
        print("")
        

    errou_miseravel = False
    while errou_miseravel == False:
        chose = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if chose == "no":
            keep_going = False
            errou_miseravel = True
        elif chose == "yes":
            errou_miseravel = True
        else:
            print("You type the wrong command.")