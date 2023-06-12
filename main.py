from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Row
from text import Text
import time

# Create and configure screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=1000, width=1600)
screen.title("Breakout")
screen.tracer(0)

# Create ball, paddle, and scoreboard
paddle = Paddle((0, -400))
ball = Ball()
scoreboard = Scoreboard()
text = Text()

# Set event listener and pause function
screen.listen()
screen.onkey(scoreboard.pause_game, "space")


# Create bricks
def starting_positions():
    text.clear()
    """Sets bricks, paddle, and ball in starting positions"""
    yellow_row_1 = Row("yellow", -740, 0)
    yellow_row_2 = Row("yellow", -740, 30)
    green_row_1 = Row("green", -740, 60)
    green_row_2 = Row("green", -740, 90)
    orange_row_1 = Row("orange", -740, 120)
    orange_row_2 = Row("orange", -740, 150)
    red_row_1 = Row("red", -740, 180)
    red_row_2 = Row("red", -740, 210)
    scoreboard.rows = [yellow_row_1.bricks, yellow_row_2.bricks, green_row_1.bricks, green_row_2.bricks,
                       orange_row_1.bricks, orange_row_2.bricks, red_row_1.bricks, red_row_2.bricks]
    paddle.reset()
    ball.reset(paddle.xcor(), paddle.ycor())
    scoreboard.reset()
    scoreboard.game_on = True
    screen.onkey(None, "Return")
    text.welcome()

starting_positions()

while scoreboard.game_on:
    paddle.active = not scoreboard.game_paused

    # Listen for paddle movement while not paused, but not when game is paused
    if paddle.active:
        text.clear()
        screen.onkey(paddle.move_left, "Left")
        screen.onkey(paddle.move_right, "Right")
        screen.onkey(paddle.move_left, "a")
        screen.onkey(paddle.move_right, "d")
    else:
        screen.onkey(None, "Left")
        screen.onkey(None, "Right")
        screen.onkey(None, "a")
        screen.onkey(None, "d")

    if not scoreboard.game_paused:
        # When not paused, ball moves
        screen.update()
        time.sleep(ball.sleep_time)
        ball.move()

        # If all rows are cleared and 2 screens are cleared, player wins
        if len(scoreboard.rows) == 0 and scoreboard.screens_cleared == 2:
            scoreboard.game_paused = True
            text.win()
            screen.onkey(starting_positions, "Return")

        # If all rows cleared and only 1 screen cleared, create a second screen of bricks
        if len(scoreboard.rows) == 0 and scoreboard.screens_cleared < 2:
            scoreboard.screens_cleared += 1
            starting_positions()

        # Check for collision with top wall
        if ball.ycor() > 490:
            ball.top_hits += 1
            # On first hit, paddle shrinks to half its size
            if ball.top_hits == 1:
                paddle.shrink()
            ball.top_bounce()

        # Check for collision with paddle
        if ball.distance(paddle) < paddle.ball_distance and -400 <= ball.ycor() <= -381:
            ball.paddle_bounce()

        # Check for collisions with side walls
        if ball.xcor() < -790 or ball.xcor() > 790:
            ball.side_bounce()

        # Check for collisions with bricks
        for row in scoreboard.rows:
            if len(row) == 0:
                scoreboard.rows.pop(scoreboard.rows.index(row))
            else:
                for brick in row:
                    if -19 <= ball.ycor() - brick.ycor() <= 19 and -55 <= ball.xcor() - brick.xcor() <= 55:
                        ball.top_bounce()
                        scoreboard.add_score(brick.colour_name)
                        ball.increase_speed(brick.colour_name)
                        brick.goto(0, 600)
                        row.pop(row.index(brick))

        # If ball goes off bottom, lose a life and reset
        if ball.ycor() < -490:
            if scoreboard.turn > 1:
                ball.goto(paddle.xcor(), paddle.ycor())
                scoreboard.lost_turn()
                ball.reset(paddle.xcor(), paddle.ycor())
                paddle.reset()
            elif scoreboard.turn == 1:
                scoreboard.lost_turn()
                scoreboard.game_paused = True
                ball.x_move = 0
                ball.y_move = 0
                for row in scoreboard.rows:
                    for brick in row:
                        brick.clear()
                        brick.goto(0, 600)
                text.game_over()
                screen.onkey(starting_positions, "Return")

    # If game is paused, wait and update screen
    else:
        time.sleep(ball.sleep_time)
        screen.update()

screen.mainloop()
