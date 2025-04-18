from turtle import Turtle, Screen
import time
from animal import Animal
import random
from car import Car
from rainbow import r_list
from level import Level

car_list = []
game_speed = .2
max_obj = 1

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing!")
my_screen.listen()
my_screen.tracer(0)
my_screen.colormode(255)

tom = Animal()
level = Level()

my_screen.onkeypress(fun=tom.moving, key="Up")

game_on = True

while game_on:

    time.sleep(game_speed)
    my_screen.update()

    ran_num_obj = random.randint(0, max_obj)
    for i in range(ran_num_obj):
        car = Car()
        car_list.append(car)

    for i in range(len(car_list)):
        car_list[i].car_speed()
        if tom.distance(car_list[i]) < 20:
            game_on = False
            level.game_over()

    if tom.ycor() > 290:
        level.increase_level()
        game_speed = game_speed / 2
        tom.animal_reset()
        




my_screen.exitonclick()