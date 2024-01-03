from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
#key bindings
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    #Left paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


















screen.exitonclick()