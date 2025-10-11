from turtle import Turtle, Screen, colormode
import random


turtle = Turtle()
color = colormode(255)

sides = 2

for _ in range(8):
   sides += 1
   degree = 360/sides
   for _ in range(sides):
        turtle.forward(100)
        turtle.right(degree)



