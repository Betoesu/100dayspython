from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ): #quiz_brain: QuizBrain, faz com que o tipo de dado quiz_brain seja de tipo QuizBrain(A classe)
        self.quiz = quiz_brain

        #Tela
        self.tela = Tk()
        self.tela.title("Quizzler")
        self.tela.config(padx=20,pady=20, background=THEME_COLOR)

        #Score
        self.texto_score = Label(text=f"Score: {self.quiz.score}", fg="white", background=THEME_COLOR)
        self.texto_score.grid(row=0, column=1)
        
        #Canva
        self.canvas = Canvas(background="white", width=300, height=250)
        self.texto_pergunta = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="teste",
            font=FONT,
            fill=THEME_COLOR
            )
               
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        #Botões

        imagem_verdadeiro = PhotoImage(file="./Projetos/34_Quizzler/images/true.png")
        self.botao_verdadeiro = Button(image=imagem_verdadeiro, highlightthickness=0, command=self.resposta_verdadeiro)
        self.botao_verdadeiro.grid(column=0, row=2)
        

        imagem_falso = PhotoImage(file="./Projetos/34_Quizzler/images/false.png")
        self.botao_falso = Button(image=imagem_falso, highlightthickness=0, command=self.resposta_falso)
        self.botao_falso.grid(column=1,row=2)
        
        self.get_next_question()
        

        self.tela.mainloop()
    


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            pergunta = self.quiz.next_question()
            self.canvas.itemconfig(self.texto_pergunta, text=pergunta)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.texto_pergunta, text=f"You've completed the quiz\n Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.botao_verdadeiro.config(state="disabled")
            self.botao_falso.config(state="disabled")

    def resposta_verdadeiro(self):
        esta_certo = self.quiz.check_answer("True")
        self.give_feedback(esta_certo)
        

    def resposta_falso(self):
        esta_certo = self.quiz.check_answer("False")
        self.give_feedback(esta_certo)

    def give_feedback(self,esta_certo):
        if esta_certo == True:
            self.canvas.config(bg="green")
            self.texto_score.config(text=f"Score: {self.quiz.score}")
        elif esta_certo == False:
            self.canvas.config(bg="red")
        self.canvas.after(1000,self.get_next_question)



