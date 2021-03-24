from turtle import Turtle,Screen
import random

aamai = Turtle()
aamai.shape("turtle")
aamai.color("green")
aamai.speed(1)

colors=["yellow","red","black","green","violet"]

def draw_shape(num):
    for i in range(1,num+1):
        aamai.forward(100)
        aamai.left(360/num)

for i in range(2,10):
    draw_shape(i)
    aamai.color(random.choice(colors))

s=Screen()
s.exitonclick()