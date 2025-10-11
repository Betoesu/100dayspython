from tkinter import *

def button_clicked():
    new_title = input.get()
    my_label["text"] = new_title

#Tela
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
#Padding == Preenchimento
window.config(padx=100, pady=200)

#Texto Rótulo
my_label = Label(text="I Am a Label", font=("Arial", 24))

#Teste de mudança de texto
my_label["text"] = "New text"
my_label.config(text="New test")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Botão
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
newButton = Button(text="New Button", command=button_clicked)
newButton.grid(column=2, row=0)

#Entry

input = Entry(width=25)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()