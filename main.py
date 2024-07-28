from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=ScoreBoard()
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect colisions with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #right side paddle miss
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    #left side paddle miss
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

    if scoreboard.l_score >= 2:
        scoreboard.winner_Text="Left side won\n     GAME OVER"
        scoreboard.game_result()
        game_is_on=False
    if scoreboard.r_score>=2:
        scoreboard.winner_Text="Right side won\n    GAME OVER"
        scoreboard.game_result()
        game_is_on=False


screen.exitonclick()
