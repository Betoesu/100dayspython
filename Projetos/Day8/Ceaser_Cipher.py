def encrypt(message): 
    crypt_message = ""
    for letter in message:

        if letter == " ":
            crypt_message += " "
        else:  
            position = alphabet.index(letter)
            position_number = position + number
            if position_number > 25:
                position_number -= 25

            letter = alphabet[position_number]
            crypt_message += letter
    print(crypt_message)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]




decode_or_encode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
if decode_or_encode == "encode":
    message = input("Type your message: ").lower()
    number = int(input("Type your shift number: "))
     #

elif decode_or_encode == "decode":
    message = input("Type your message: ").lower()
    number = int(input("Type your shift number: "))
    #

else:
    print("")
    input('''You type the worng command.      
Type Enter to go again: ''')
    print("")
    
encrypt(message)