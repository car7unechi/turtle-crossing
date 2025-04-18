import colorgram
from turtle import Turtle, Screen

rainbow_colors = colorgram.extract('rainbow.jpeg', 10)

rainbow_list = []

for color in rainbow_colors:
    first_color = color
    rgb = first_color.rgb
    r= rgb.r
    g= rgb.g
    b= rgb.b
    rainbow_list.append((r, g, b))

print(rainbow_list)
r_list = [(190, 171, 1), (143, 11, 107), (20, 112, 189), (39, 170, 118), (37, 145, 93), (216, 218, 2), (197, 45, 2), (228, 226, 64), (159, 35, 1), (36, 51, 124)]













