from turtle import Turtle


class MainTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(0,-370)
        

    def move(self):
        self.forward(20)