from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
color = colormode(255)

def random_walk():
    number = random.randint(1,2)
    

    if number == 1:
        turtle.right(random.choice(directions))
        

    else:
        turtle.left(random.choice(directions))
    
    turtle.forward(30)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

directions = [0,90,180,270]

turtle.pensize(15)
turtle.speed("fastest")

for _ in range (200):
    color = random_color()
    turtle.color(color)
    random_walk()

screen = Screen()
screen.exitonclick()