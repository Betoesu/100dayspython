from turtle import Turtle, Screen, colormode
import random
import colorgram

turtle = Turtle()
color = colormode(255)

turtle.shape("turtle")
turtle.color("red")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()