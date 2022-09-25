import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.pu()
        self.goto(x_cor, 0)
        self.speed("fastest")

    def up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
