from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-380,340)
        self.pendown()
        self.pencolor("white")
        self.write("Tutorial", align="left", font=("Arial",20,"normal"))


    def marcadores(self):
        self.hideturtle()
        self.goto(-380,340)
        self.pencolor("white")
        self.penup()
        self.goto(-400,340)
        for _ in range(0,80):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        
        self.penup()
        self.goto(-400,-340)
        for _ in range(0,80):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    
    def next_level(self,level):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-380,340)
        self.pendown()
        self.pencolor("white")
        self.write(f"Level: {level}", align="left", font=("Arial",20,"normal"))

        