from turtle import Turtle
import random


inicial_angle = (random.randint(-360,360))
while inicial_angle in range (75,100):
    inicial_angle = (random.randint(-360,360))
    
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(300)
    
    def move(self):
        self.forward(20)

    def y_collision(self):
        ball_heading = self.heading()
        self.setheading(-ball_heading)

    def x_collision(self):
        ball_heading = self.heading()

        self.setheading(-(ball_heading - 180))


