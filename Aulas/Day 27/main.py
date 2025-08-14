from tkinter import *

def button_clicked():
    new_title = input.get()
    my_label["text"] = new_title

#Tela
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Texto Rótulo
my_label = Label(text="I Am a Label", font=("Arial", 24))

#Teste de mudança de texto
my_label["text"] = "New text"
my_label.config(text="New test")
my_label.place(x=200 ,y=0)

#Botão
button = Button(text="Click me", command=button_clicked)


#Entry

input = Entry(width=25)











window.mainloop()