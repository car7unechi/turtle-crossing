from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align="Left", font=("times", 14, "normal") )

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="Left", font=("times", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=("times", 30, "normal"))
        
