from tkinter import *

FONT = ("Arial",12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

#Janela
window = Tk()
window.title("Minhas Senhas")
window.config(padx=20,pady=20)

#Imagem Cadeado
canvas = Canvas(width=200, height=200)
lockImage = PhotoImage(file="./Aulas/Day 29/logo.png")
canvas.create_image(100,100,image=lockImage)
canvas.grid(row=0, column=1)

#Textos
websiteLabel = Label(text="Website:", padx=5,pady=5,font=FONT)
websiteLabel.grid(row=1,column=0)

emaiLabel = Label(text="Email/Username:", padx=5,pady=5,font=FONT)
emaiLabel.grid(row=2,column=0)

passwordLabel = Label(text="Password:", padx=0,pady=5, font=FONT)
passwordLabel.grid(row=3,column=0)

#Espaços de Input
websiteInput = Entry(width=35)
websiteInput.grid(row=1,column=1,columnspan=2)

emailInput = Entry(width=35)
emailInput.grid(row=2,column=1,columnspan=2)

passwordInput = Entry(width=21,)
passwordInput.grid(row=3,column=1,sticky="w") #stick="w" gruda o passwordInput para west(esquerda)



window.mainloop()