from turtle import Turtle, Screen


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.top_score = 0
        with open("high_score.txt","r") as hs:
            self.top_score = int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.points += 1

    def update_score(self):
        self.clear()
        self.write(f"Score {self.points} High Score {self.top_score}", align="center", font=("Times new Roman", 12, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("Ohh Game over! Please start again.", align="center", font=("Times new Roman", 12, "normal"))
        if self.points > self.top_score:
            self.top_score = self.points
            with open("high_score.txt","w") as f:
                f.write(str(self.top_score))
