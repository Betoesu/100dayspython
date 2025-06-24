from turtle import Turtle,Screen
from main_turtle import MainTurtle
from cars import Cars
from scoreboard import Scoreboard
import time
WIN_ZONE = (0, 380)

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Crossy Road")
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.marcadores()
turtle = MainTurtle()
cars = Cars()
screen.update()

screen.listen()
screen.onkey(turtle.move, "Up")

level = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car(level)
    cars.move(level)
    if turtle.distance(WIN_ZONE) <= 10:
        level += 1
        scoreboard.next_level(level)
        scoreboard.marcadores()
        time.sleep(1)
        turtle.goto(0,-370)
    
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False



screen.exitonclick()