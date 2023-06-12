from turtle import Turtle


class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def game_over(self):
        """Posts message when game is over"""
        self.goto(0, 0)
        self.write("Game over.", align="center", font=("Courier", 50, "normal"))
        self.goto(0, -100)
        self.write("Press enter to play again.", align="center", font=("Courier", 16, "normal"))
        self.forward(0)

    def win(self):
        """Posts message when game is won"""
        self.goto(0, 0)
        self.write("You win!", align="center", font=("Courier", 50, "normal"))
        self.goto(0, -100)
        self.write("Press enter to play again.", align="center", font=("Courier", 16, "normal"))
        self.forward(0)

    def welcome(self):
        """Posts welcome message at start of game"""
        self.goto(0, 420)
        self.write("Welcome to Breakout!", align="center", font=("Courier", 20, "normal"))
        self.goto(0, 380)
        self.write("Press space to play and pause", align="center", font=("Courier", 14, "normal"))

    def reset(self):
        """Clears previous messages"""
        self.goto(0, 600)
        self.clear()
