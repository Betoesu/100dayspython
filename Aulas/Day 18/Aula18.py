from turtle import Turtle, Screen, colormode
import random


turtle = Turtle()
color = colormode(255)

# turtle.shape("turtle")
# turtle.color("red")

# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()



sides = 2

for _ in range(8):
   sides += 1
   degree = 360/sides
   for _ in range(sides):
        turtle.forward(100)
        turtle.right(degree)



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


turtle.speed(0)
def spirograph(degrees):
    for _ in range(int(360/degrees)):
        turtle.circle(100)
        turtle.right(degrees)
        turtle.color(random_color())

spirograph(1)










screen = Screen()
screen.exitonclick()


