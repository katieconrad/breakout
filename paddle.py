from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(position)
        self.color("white")
        self.shapesize(1.0, 10.0)
        self.limit = 720
        self.ball_distance = 105
        self.active = True

    def move_right(self):
        """Moves paddle to the right"""
        new_x = self.xcor() + 20
        if new_x < self.limit:
            self.goto(new_x, self.ycor())

    def move_left(self):
        """Moves paddle to the left"""
        new_x = self.xcor() - 20
        if new_x > -self.limit:
            self.goto(new_x, self.ycor())

    def shrink(self):
        """Shrinks paddle to half its size"""
        self.clear()
        self.shapesize(1.0, 5.0)
        self.ball_distance = 53
        self.limit = 765

    def reset(self):
        """Resets paddle to original size"""
        self.clear()
        self.shapesize(1.0, 10.0)
        self.ball_distance = 105
        self.limit = 720
