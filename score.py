from turtle import Turtle


class Score(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x_cor, 270)
        self.write(f"{self.score}", align="center", font=("Aerial", 20, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Aerial", 20, "normal"))