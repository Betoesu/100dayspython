from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(120)
    
    def move(self):
        self.forward(10)

    def collision(self):
        if self.xcor() > 0:
            self.setheading(-45)
        if self.xcor() < 0:
            self.setheading(-135)

