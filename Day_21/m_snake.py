from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.seg_list = []
        self.create_snake()
        self.head = self.seg_list[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("blue")
        new_seg.penup()
        new_seg.goto(position)
        self.seg_list.append(new_seg)

    def expand(self):
        self.add_segment(self.seg_list[-1].position())

    def move(self):
        for i in range(len(self.seg_list) - 1, 0, -1):
            v_x = self.seg_list[i -1].xcor()
            v_y = self.seg_list[i -1].ycor()
            self.seg_list[i].goto(v_x, v_y)
        self.head.forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
