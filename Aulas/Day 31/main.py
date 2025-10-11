from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
cartaAtual = {}
listFrases = {}
#-----PALAVRA-EM-INGLES-----#

try:
    frases = pandas.read_csv("./Aulas/Day 31/data/words_to_learn.csv")
except:
   frasesArquivoOriginal = pandas.read_csv("./Aulas/Day 31/data/English_Phrases.csv")
   listFrases = frasesArquivoOriginal.to_dict(orient="records")
  
else:
    listFrases = frases.to_dict(orient="records") #orient="records" faz retornar uma lista



#-----MÉTODOS-----#

def ProximoFlashCard():
    global cartaAtual, tempoVirar
    tela.after_cancel(tempoVirar)
    cartaAtual = random.choice(listFrases)
    canvas.itemconfig(textoIdioma, text="English", fill="black")
    canvas.itemconfig(textoPalavra, text=cartaAtual["English"], fill="black")
    canvas.itemconfig(atualFlashCard, image=frenteFlashCard)
    tempoVirar = tela.after(3000,func=VirarFlashCard)
    

def RemoverPalavra():
    listFrases.remove(cartaAtual)
    frases = pandas.DataFrame(listFrases)
    frases.to_csv("./Aulas/Day 31/data/words_to_learn.csv")
    ProximoFlashCard()
    

def VirarFlashCard():
    canvas.itemconfig(atualFlashCard, image=versoFlashCard)
    canvas.itemconfig(textoIdioma,text="Portugues")
    canvas.itemconfig(textoPalavra,text=cartaAtual["Português"], fill="white")
    canvas.itemconfig(textoIdioma, fill="white")
    


#-----TELA-----#
tela = Tk()
tela.title("FlashCard")
tela.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

tempoVirar = tela.after(3000,func=VirarFlashCard)



#-----CONTEUDO FLASHCARD-----#
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)


#---Frente-FlashCard---#
frenteFlashCard = PhotoImage(file="./Aulas/Day 31/images/card_front.png")

#--Verso-FlashCard--#
versoFlashCard = PhotoImage(file="./Aulas/Day 31/images/card_back.png")

#--Atual-FlashCard--#
atualFlashCard = canvas.create_image(400, 263, image=frenteFlashCard)

#--Texto-FlashCard---#
textoIdioma = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
textoPalavra = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



#-----BOTÕES-----#
botaoCorretoImage = PhotoImage(file="./Aulas/Day 31/images/right.png")
botaoCorreto = Button(image=botaoCorretoImage,command=RemoverPalavra)
botaoCorreto.grid(row=1,column=1)

botaoErradoImage = PhotoImage(file="./Aulas/Day 31/images/wrong.png")
botaoErrado = Button(image=botaoErradoImage, command=ProximoFlashCard)
botaoErrado.grid(row=1,column=0)


ProximoFlashCard()

tela.after(3000,VirarFlashCard)















tela.mainloop()
