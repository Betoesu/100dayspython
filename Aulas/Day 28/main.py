from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    countdown(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    countMinute = math.floor(count /60)
    countSeconds = count % 60
    if countSeconds < 10:
        countSeconds = f"0{countSeconds}"
    

    canvas.itemconfig(timerText, text=f"{countMinute}:{countSeconds}")
    if count > 0:
        window.after(1000,countdown,count - 1)  


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
timer = Label(text="Timer", foreground=GREEN, font=(FONT_NAME,50,"bold"), background=YELLOW)
timer.grid(row=0,column=1)

#Botão Start
startButton = Button(text="Start",width=5,command=start_timer)
startButton.grid(row=2,column=0)


#Botão Reset
resetButton = Button(text="Reset",width=5)
resetButton.grid(row=2,column=2)

#Chech Mark
checkMark = Label(text="✔",fg=GREEN,bg=YELLOW)
checkMark.grid(row=3,column=1)

window.mainloop()