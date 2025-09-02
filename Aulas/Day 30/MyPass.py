from tkinter import *
from tkinter import messagebox
import random
import pyperclip #Salvar algo no ctrl + c
import json

FONT = ("Arial",12)
caminho = "./Aulas/Day 30/senhas.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    

    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["!","@","#","$","%","&","*","?","+","-","_","="]

    quantLetras = random.randint(8,10)
    quantNumeros = random.randint(2,4)
    quantSimbolos = random.randint(2,4)

    letrasSenha = [random.choice(letters) for _ in range(quantLetras)]
    numerosSenha = [random.choice(numbers) for _ in range(quantNumeros)]
    simbolosSenha = [random.choice(symbols) for _ in range(quantSimbolos)]

    passwordList = letrasSenha + numerosSenha + simbolosSenha
    random.shuffle(passwordList)

    password = "".join(passwordList)
    
    passwordInput.delete(0,END)
    passwordInput.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():

    website = websiteInput.get().capitalize().strip()
    email = emailInput.get()
    senha = passwordInput.get()

    new_data = {
        website: {
        "email": email,
        "password":senha,
    }
    }

    #Pop Up para preencher todos os campos
    if  len(website) == 0 or len(email) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Ops", message="Tenha certeza que não deixou nenhum campo em branco")

    else:
        try:
            with open(caminho, "r") as file:
                #Lendo dados antigos
                data = json.load(file)

        except FileNotFoundError:
            with open(caminho,"w") as file:
                #Criando o Arquivo caso nao exista
                json.dump(new_data, file, indent=4)


        else:
            #Adicionando novos dados com os dados antigos
            data.update(new_data)

            with open(caminho,"w") as file:
                #Salvando os dados adicionais
                json.dump(data, file, indent=4)

        finally:         
            #O 0 representa o primeiro caractere e o END o ultimo
            emailInput.delete(0, END)
            passwordInput.delete(0,END)
            websiteInput.delete(0,END)

            #Volta o foco para o primeiro campo
            websiteInput.focus()


#--------------------------------PROCURAR CREDENCIAIS--------------------------------#
def Search():
    website = websiteInput.get().capitalize().strip()

    if len(website) == 0:
        messagebox.showinfo(title="Campo Vazio",message="Digite algo para procurar")
    else:
        try:
            with open(caminho,"r") as file:
                data = json.load(file)  
                
        except FileNotFoundError:
            messagebox.showinfo(title="Erro", message=f"Ainda não há senhas salvas")
        
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message= f"Email: {email}\nSenha: {password}")
                pyperclip.copy(password)
            
            else: 
                messagebox.showinfo(title="Erro", message=f"Não há informações registradas de {website}")













#--------------------------------FOCO DAS ENTRADAS--------------------------------#

#Arrumando comandos de seta para subir ou descer com as setas entre os inputs
def focus_email(event):
    emailInput.focus()

def focus_password(event):
    passwordInput.focus()

def focus_previous(event):
    wigdetAtual = window.focus_get()

    if wigdetAtual == passwordInput:
        emailInput.focus()
    elif wigdetAtual == emailInput:
        websiteInput.focus()

def focus_next(event):
    widgetAtual = window.focus_get()

    if widgetAtual == websiteInput:
        emailInput.focus()
    elif widgetAtual == emailInput:
        passwordInput.focus()

    

# ---------------------------- UI SETUP ------------------------------- #

#---Janela---
window = Tk()
window.title("Minhas Senhas")
window.config(padx=70,pady=70)




#---Imagem Cadeado---
canvas = Canvas(width=200, height=200)
lockImage = PhotoImage(file="./Aulas/Day 29/logo.png")
canvas.create_image(100,100,image=lockImage)
canvas.grid(row=0, column=1)




#---Textos---
websiteLabel = Label(text="Website/App:",pady=5,font=FONT)
websiteLabel.grid(row=1,column=0,sticky="e")

emaiLabel = Label(text="Email/Usuário:",pady=5, font=FONT)
emaiLabel.grid(row=2,column=0,sticky="e")

passwordLabel = Label(text="Senha:",pady=5, font=FONT)
passwordLabel.grid(row=3,column=0,sticky="e")



#---Espaços de Input---
#Website
websiteInput = Entry(width=35)
websiteInput.grid(row=1,column=1,columnspan=2,sticky="w")
websiteInput.focus()

#Faz com que ao apertar Enter va para o proximo campo
websiteInput.bind("<Return>", focus_email)

#Email
emailInput = Entry(width=55)
emailInput.grid(row=2,column=1,columnspan=2,sticky="w")


#Senha
passwordInput = Entry(width=35)
passwordInput.grid(row=3,column=1,sticky="w") 





#---Botões---

#Gerar Senha
generatePasswordButton = Button(text="Gerar Senha", width=15,command=generate_password)
generatePasswordButton.grid(row=3, column=2,sticky="w",padx=10)

#Add
addButton = Button(text="Adicionar",width=36,command=Save)
addButton.grid(row=4,column=1,columnspan=2,sticky="ew")

#Procurar
botaoProcurar = Button(text="Procurar", width=15,command=Search)
botaoProcurar.grid(row=1,column=2,sticky="w",padx=10)




#-------------------------------Botões de Movimento------------------------#

#Faz com que ao apertar Enter va para o proximo campo
emailInput.bind("<Return>",focus_password)


#Botões de Seta
for widget in [websiteInput, emailInput, passwordInput]:
    widget.bind("<Up>", focus_previous)
    widget.bind("<Down>", focus_next)

window.mainloop()