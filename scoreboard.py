from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.turn = 3
        self.color("white")
        self.game_on = True
        self.rows = []
        self.screens_cleared = 0
        self.update()
        self.game_paused = True

    def update(self):
        """Updates scoreboard"""
        self.goto(-750, -450)
        self.write(f"Lives: {self.turn}", align="left", font=("Courier", 15, "normal"))
        self.goto(750, -450)
        self.write(f"Score: {self.score}", align="right", font=("Courier", 15, "normal"))

    def lost_turn(self):
        """Logs a lost turn and updates scoreboard"""
        self.turn -= 1
        self.clear()
        self.update()

    def add_score(self, colour):
        """Calculates score when brick is hit and updates scoreboard"""
        if colour == "yellow":
            self.score += 1
        elif colour == "green":
            self.score += 3
        elif colour == "orange":
            self.score += 5
        elif colour == "red":
            self.score += 7
        self.clear()
        self.update()

    def pause_game(self):
        """Toggles pause status on or off"""
        if self.game_paused:
            self.game_paused = False
        else:
            self.game_paused = True

    def reset(self):
        """Resets scoreboard on Game Over or Win"""
        if self.screens_cleared == 1:
            pass
        else:
            self.score = 0
            self.turn = 3
            self.screens_cleared = 0
            self.clear()
            self.update()
