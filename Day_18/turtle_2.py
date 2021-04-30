from turtle import Turtle, Screen
import random

raju = Turtle()
raju.shape("turtle")
raju.color("green")
raju.setpos(100,100)

def draw_shape(num_side):
    for j in range(1, num_side + 1):
        raju.forward(100)
        raju.right(360 / num_side)


color_list = ["blue", "green", "Yellow", "red", "Orange", "Aliceblue", "lightblue", "lightgreen"]

for i in range(3, 8):
    draw_shape(i)
    raju.color(random.choice(color_list))

scr = Screen()
scr.exitonclick()
