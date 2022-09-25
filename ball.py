from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("white")
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1

    def refresh(self):
        self.goto(0, 0)
        self.paddle_bounce()
