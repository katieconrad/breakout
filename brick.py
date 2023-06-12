from turtle import Turtle


class Brick(Turtle):

    def __init__(self, colour, coords):
        super().__init__()
        self.penup()
        self.color(colour)
        self.colour_name = colour
        self.shape("square")
        self.shapesize(1, 5.4)
        self.speed("fastest")
        self.goto(coords)


class Row:

    def __init__(self, colour, x, y):
        self.bricks = []
        self.colour = colour
        self.starting_x = x
        self.starting_y = y
        self.create_bricks()

    def create_bricks(self):
        """Creates a row of bricks"""
        for i in range(14):
            brick_x = self.starting_x + (113 * i)
            brick_y = self.starting_y
            brick_coords = (brick_x, brick_y)
            brick = Brick(self.colour, brick_coords)
            self.bricks.append(brick)
