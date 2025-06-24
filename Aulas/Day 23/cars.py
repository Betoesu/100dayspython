from turtle import Turtle
import random

COLORS = ["red", "green", "blue","white","orange","purple","pink","gray","yellow"]
MOVE_INCREMENT = 5
STARTING_MOVE_DISTANCE = 5


class Cars:
    def __init__(self):
        self.all_cars = []
        

    

    def create_car(self,level):
        random_chance = random.randint(1,6)
        if level >= 10:
             random_chance = random.randint(1,3)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-330,330)
            new_car.goto(410, random_y)
            self.all_cars.append(new_car)

        

    def move(self,level):
            for car in self.all_cars:
                car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level))
        



    
    