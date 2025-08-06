import os
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Projetos/24_modified_Snake_game/modified SnakeGame/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(F"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("./Projetos/24_modified_Snake_game/modified SnakeGame/data.txt", mode="w") as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
        
    def increse_score(self):
        self.score += 1
        self.update_scoreboard()

    