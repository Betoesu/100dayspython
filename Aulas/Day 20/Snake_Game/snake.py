from turtle import Turtle

STARTIG_POSITIONS = [(0, 0), (-20, 0) , (-40, 0)]
MOVE_DISTANCE = 20  
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTIG_POSITIONS:
            self.adding_segments(position)
    
    def adding_segments(self):
        new_segments = Turtle("square")
        new_segments.color("green")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)
    
    def extend(self):
        self.adding_segments()


        
    

    def auto_move(self):
            for seg in range(len(self.segments) - 1, 0,-1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)