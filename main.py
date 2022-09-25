import time
import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)

i = Turtle()
i.hideturtle()
i.color("white")
i.pensize(5)
i.pu()
i.goto(0, -280)

while i.ycor() < 290:
    i.seth(90)
    i.pd()
    i.fd(50)
    i.pu()
    i.fd(50)

turtle.tracer(0)
right_paddle = Paddle(360, "red")
left_paddle = Paddle(-370, "orange")
ball = Ball()
r_score = Score(50)
l_score = Score(-50)

screen.listen()

game_is_on = True

while game_is_on:
    turtle.update()
    time.sleep(0.05)
    ball.move()
    screen.onkey(right_paddle.up, key="Up")
    screen.onkey(right_paddle.down, key="Down")

    screen.onkey(left_paddle.up, key="w")
    screen.onkey(left_paddle.down, key="s")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if right_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        r_score.increase()

    elif left_paddle.distance(ball) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        l_score.increase()

    if ball.xcor() > 360:
        ball.refresh()

    elif ball.xcor() < -360:
        ball.refresh()

screen.exitonclick()
