#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]" #Aqui eu coloquei como padrão o que será alterado em cada carta

with open("./Projetos/24_Mail_Merge/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file: #este comando abre o nome dos convidados 
    names = names_file.readlines() #este comando le tudo como uma lista

with open("./Projetos/24_Mail_Merge/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file: # Aqui eu abro a carta ainda nao mudada
    letter_content = letter_file.read() #Leio o conteudo da carta e guardo na variavel letter_content
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name) # Neste Loop eu tiro espaços desnecessários criando a variavel stripped_name que tem como comando strip. Depois crio a nova carta usando replace para trocar nosso placeholder com o nome da lista. E o for loop pega nome por nome da lista.
    with open(f"./Projetos/24_Mail_Merge/Mail Merge Project Start/output/ReadyToSend/letter_to_{stripped_name}.docx", mode="w") as letter: # Aqui eu levo o diretório para ReadyToSend e crio o arquivo letter_to_nome do convidadado
            letter.write(new_letter) 

