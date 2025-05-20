# from turtle import Turtle, Screen

# turtle = Turtle(shape="turtle")
# screen = Screen()


# def forwards():
#     turtle.forward(15)

# def backwards():
#     turtle.backward(15)

# def clockwise():
#     turtle.right(15)

# def counter_clockwise():
#     turtle.left(15)

# def clear():
#     turtle.reset()

# screen.listen()


# screen.onkey(key="w", fun=forwards)
# screen.onkey(key="s", fun=backwards)
# screen.onkey(key= "d", fun=clockwise)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="c", fun=clear)






import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=700, width=700)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? [red/blue/green/yellow/orange/purple] Enter a color: ").lower() .strip()
colors = ["red","yellow","orange","blue","purple","green"]
paces = [0,1,2,3,4,5,6,7,8,9,10]
all_turtles = []


if user_bet in colors:
    is_race_on = True

else:
    exit()

y = 280
x = -330
for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x , y)
    y -= 100
    all_turtles.append(turtle)





while is_race_on:
    turtle_chosen = random.choice(all_turtles)
    random_distance = random.randint(0,10)
    turtle_chosen.forward(random_distance)

    if turtle_chosen.xcor() > 315:
        winning_turtle = turtle_chosen.pencolor()
        is_race_on = False
    
        if turtle_chosen.pencolor() == user_bet:
            print("You Win")
        
        else:
            print(f"You lose the winner was {winning_turtle}")
        
    
        
    









screen.exitonclick()




















screen.exitonclick()