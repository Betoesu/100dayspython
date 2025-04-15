







decode_or_encode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
if decode_or_encode == "encode":
    message = input("Type your message: ")
    number = input("Type your shift number: ")
     #

elif decode_or_encode == "decode":
    message = input("Type your message: ")
    number = input("Type your shift number: ")
            #

else:
    print("")
    input('''You type the worng command.      
Type Enter to go again: ''')
    print("")
        