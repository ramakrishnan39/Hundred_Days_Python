from turtle import Turtle
from turtle import Screen

raju=Turtle()
raju.shape("turtle")
raju.color("Blue")
# raju.forward(100)
# raju.right(90)
# raju.forward(100)
# raju.right(90)
# raju.forward(100)
# raju.right(90)
# raju.forward(100)

for i in range(4):
    raju.forward(100)
    raju.right(90)

win= Screen()
win.exitonclick()
