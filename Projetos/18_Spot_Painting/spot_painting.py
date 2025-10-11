import turtle as turtle_module
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('Aulas/Day 18/spot_painting.jpg', 6)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)


color_list = [ (198, 13, 32), (248, 236, 25), (40, 76, 188)]
turtle = turtle_module.Turtle()
turtle_module.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.speed(0)
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_dots = 100


for dot_count in range(1, number_dots + 1):
    turtle.dot(20,random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()