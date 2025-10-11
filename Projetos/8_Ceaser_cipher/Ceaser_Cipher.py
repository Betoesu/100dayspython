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