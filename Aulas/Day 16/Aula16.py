
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Bulbbassour","Charmander","Squirtle"])
table.add_column("Type", ["Grass","Fire","Water"])

print(table)

table.align = "l"
print(table)

