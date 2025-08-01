from turtle import Turtle,Screen

screen = Screen()
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
   

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)



