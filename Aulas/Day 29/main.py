from tkinter import *

FONT = ("Arial",12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    websiteApp = websiteInput.get()
    emailUsuario = emailInput.get()
    senha = passwordInput.get()

    caminho = "./Aulas/Day 29/senhas.txt"

    try:
        with open(caminho,"r") as f:
            conteudo = f.read().strip()
    except FileNotFoundError:
        conteudo = ""

    if not conteudo: # o not funciona pra ver se a variavel ta vazia
        with open(caminho, "a") as f:
            f.write("WEBSITE/APP | EMAIL/USUARIO | SENHA\n")

    with open(caminho, "a") as file:
        file.write(f"{websiteApp} | {emailUsuario} | {senha}\n")
    
    #O 0 representa o primeiro caractere e o END o ultimo
    emailInput.delete(0, END)
    passwordInput.delete(0,END)
    websiteInput.delete(0,END)

    #Volta o foco para o primeiro campo
    websiteInput.focus()

def focus_email(event):
    emailInput.focus()

def focus_password(event):
    passwordInput.focus()

def save_on_enter(event):
    save()




    

# ---------------------------- UI SETUP ------------------------------- #

#Janela
window = Tk()
window.title("Minhas Senhas")
window.config(padx=70,pady=70)

#Imagem Cadeado
canvas = Canvas(width=200, height=200)
lockImage = PhotoImage(file="./Aulas/Day 29/logo.png")
canvas.create_image(100,100,image=lockImage)
canvas.grid(row=0, column=1)

#Textos
websiteLabel = Label(text="Website/App:",pady=5,font=FONT)
websiteLabel.grid(row=1,column=0,sticky="e")

emaiLabel = Label(text="Email/Usuário:",pady=5, font=FONT)
emaiLabel.grid(row=2,column=0,sticky="e")

passwordLabel = Label(text="Senha:",pady=5, font=FONT)
passwordLabel.grid(row=3,column=0,sticky="e")

#Espaços de Input

#Website
websiteInput = Entry(width=35)
websiteInput.grid(row=1,column=1,columnspan=2,sticky="w")
websiteInput.focus()

#Faz com que ao apertar Enter va para o proximo campo
websiteInput.bind("<Return>", focus_email)



#Email
emailInput = Entry(width=35)
emailInput.grid(row=2,column=1,columnspan=2,sticky="w")

#Faz com que ao apertar Enter va para o proximo campo
emailInput.bind("<Return>",focus_password)


#Senha
passwordInput = Entry(width=35)
passwordInput.grid(row=3,column=1,sticky="w") 

#Salva e funciona como o botao de adicionar
passwordInput.bind("<Return>", save_on_enter)


#Botões

#Senha
generatePasswordButton = Button(text="Gerar Senha", width=15)
generatePasswordButton.grid(row=3, column=2,sticky="w",padx=10)

#Add
addButton = Button(text="Adicionar",width=36,command=save)
addButton.grid(row=4,column=1,columnspan=2,sticky="ew")

window.mainloop()