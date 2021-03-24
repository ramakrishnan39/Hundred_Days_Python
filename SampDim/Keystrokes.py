from turtle import Turtle, Screen


t1=Turtle()


def do_print():
    t1.color("blue")
    t1.penup()
    t1.forward(20)


scr=Screen();

scr.onkey(do_print,"Up")
scr.exitonclick();