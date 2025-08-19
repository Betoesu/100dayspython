from tkinter import *
import math
import os # Para adicionar som 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00ff40"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5/60
SHORT_BREAK_MIN = 5/60
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)#Cancela efeito after
    canvas.itemconfig(timerText,text="00:00")#Volta o numero da contagem pra zero
    timerTitle.config(text="Timer")#Volta o titulo para timer
    checkMark.config(text="")#Renicia os check marks
    global reps # Para fazer mudança global
    reps = 0 #Renicia todo o processo
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1


    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    #Se as reps forem impar é hora do trabalho
    if reps % 2 != 0:
        countdown(workSec)
        timerTitle.config(text="WORK", fg=GREEN)

    #Se forem par é hora de descanso
    elif reps % 2 == 0 and reps != 8:
        countdown(shortBreakSec)
        timerTitle.config(text="Break", fg=PINK)

    else: # reps == 8
        countdown(longBreakSec)
        timerTitle.config(text="BREAK", fg=RED)

    
    # 🔥 GARANTIR QUE A JANELA APAREÇA COMO POP UP
    window.deiconify()  # Restaura a janela se estiver minimizada
    window.lift()       # Traz para o topo da pilha de janelas
    window.focus_force()  # Força o foco (cuidado: pode ser intrusivo)
    window.attributes('-topmost', True)  # Mantém no topo

    




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    countMinute = math.floor(count /60)
    countSeconds = count % 60
    if countSeconds < 10: #Maneira de evitar que os segundo fiquem 5 ao inves de 05
        countSeconds = f"0{countSeconds}"
    

    canvas.itemconfig(timerText, text=f"{countMinute}:{countSeconds}")

    #Aqui mantem nossa contagem somente até 0
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count - 1)#Mecanismo de tempo para algo acontecer, neste caso a classe countdown, e damos o argumento dessa clase, coloco -1 pq se nao nao iria ser uma contagem 
    else:
        start_timer()
        mark = ""
        workSessions = math.floor(reps/2)#A cada duas contagens é uma marca de pomodoro
        for _ in range(workSessions):
            mark += "✔"
        checkMark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

#Tela
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


window.after(1000,)


#Imagem tomate
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="./Aulas/Day 28/tomato.png")
canvas.create_image(100, 112,image=tomatoImage)
timerText = canvas.create_text(100,130,text=f"00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1, column=1)



#Timer
timerTitle = Label(text="Timer", foreground=GREEN, font=(FONT_NAME,50,"bold"), background=YELLOW)
timerTitle.grid(row=0,column=1)

#Botão Start
startButton = Button(text="Start",width=5,command=start_timer)
startButton.grid(row=2,column=0)

#Botão Reset
resetButton = Button(text="Reset",width=5, command=reset_timer)
resetButton.grid(row=2,column=2)

#Chech Mark
checkMark = Label(fg=GREEN,bg=YELLOW)
checkMark.grid(row=3,column=1)



window.mainloop()