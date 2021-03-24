from turtle import Turtle, Screen
import time

START_POS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            tn = Turtle("square")
            tn.color("blue")
            tn.penup()
            tn.goto(pos)
            self.segments.append(tn)

    def move_snake(self):
        scr = Screen()
        scr.update()
        time.sleep(0.1)
        for seg in range(len(START_POS) - 1, 0, -1):
            n_x = self.segments[seg - 1].xcor()
            n_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(n_x, n_y)
        self.head.forward(10)

    def k_up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)
        else:
            pass

    def k_down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)
        else:
            pass

    def k_right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)
        else:
            pass

    def k_left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)
        else:
            pass
