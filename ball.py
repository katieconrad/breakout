from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_speed = 10
        self.start_options = [-1, 1]
        self.start_angle = self.get_angle()
        self.xmove = self.move_speed * self.start_angle
        self.ymove = self.move_speed
        self.sleep_time = 0.075
        self.goto(0, -400)
        self.total_hits = 0
        self.orange_hits = 0
        self.red_hits = 0
        self.top_hits = 0

    def move(self):
        """Moves the ball"""
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def top_bounce(self):
        """Bounces ball off top"""
        self.ymove *= -1
        self.move()

    def side_bounce(self):
        """Bounces ball off side"""
        self.xmove *= -1
        self.move()

    def paddle_bounce(self):
        """Bounces ball off paddle"""
        self.ymove *= -1
        self.move()

    def get_angle(self):
        """Gets the balls current angle"""
        angle = choice(self.start_options)
        return angle

    def reset(self, x, y):
        """Resets ball after it goes off bottom of screen"""
        self.color("black")
        self.color("white")
        self.sleep_time = 0.08
        self.start_angle = self.get_angle()
        self.xmove = self.move_speed * self.start_angle
        self.ymove = self.move_speed
        self.top_hits = 0
        self.total_hits = 0
        self.orange_hits = 0
        self.red_hits = 0
        self.goto(x, y)
        self.move()

    def increase_speed(self, colour):
        """Increases ball speed at given milestones"""
        self.total_hits += 1
        if colour == "orange":
            self.orange_hits += 1
        elif colour == "red":
            self.red_hits += 1
        if self.total_hits == 4:
            self.sleep_time *= 0.8
        if self.total_hits == 12:
            self.sleep_time *= 0.8
        if self.orange_hits == 1:
            self.sleep_time *= 0.8
        if self.red_hits == 1:
            self.sleep_time *= 0.8
