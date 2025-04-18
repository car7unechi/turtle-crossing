from turtle import Turtle
import random
from rainbow import r_list

class Car(Turtle):
    
    def __init__(self):
        super().__init__(shape="square")
        self.add_car()
        self.color(random.choice(r_list))
        
    def car_lo(self):
        x = 305
        y = random.randint(-260, 260)
        self.position = (x, y)
        return self.position
    
    def reset_lo(self):
        self.goto(self.car_lo())
        
    def add_car(self):
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(self.car_lo())
        self.setheading(180)
        
    def car_speed(self):
        delay = random.randint(1, 20)
        new_x = self.xcor() - delay
        new_y = self.ycor()
        self.goto(new_x, new_y)
        