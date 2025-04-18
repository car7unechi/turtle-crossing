from turtle import Turtle

class Animal(Turtle):
    
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        
    def moving(self):
        self.forward(15)
        
    def animal_reset(self):
        self.goto(0, -280)