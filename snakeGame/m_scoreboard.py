from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__(self)
        self.num = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.num}", align="center", font=("Ariel", 15, "normal"))

    def increase_score(self):
        self.num += 1
        self.write(f"Score: {self.num}", align="center", font=("Ariel", 15, "normal"))
