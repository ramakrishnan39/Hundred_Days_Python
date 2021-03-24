from turtle import Turtle, Screen
import random as rand

aamai = Turtle()
aamai.shape("turtle")
aamai.color("red")
is_nagarvu = True
count=0
colors=["red","yellow","blue","green","orange"]


def right():
    aamai.forward(100)
    aamai.right(90)


def left():
    aamai.left(90)
    aamai.forward(100)



while is_nagarvu is True:
    n=rand.randint(0,1)
    col=rand.choice(colors)
    if n == 0:
        left()
    else:
        right()

    aamai.color(col)
    if count > 10 :
        is_nagarvu = False
    count = count + 1


s = Screen()
s.exitonclick()
