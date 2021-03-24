from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

scr = Screen()
scr.bgcolor("lightgreen")
scr.setup(height=600, width=600)
scr.title("Snake Game")
scr.tracer(0)

# Creates Snake object with default options
s = Snake()
# Creates Food object along with its randomized position.
f = Food()
# Creates score board
sc = Score()

scr.listen()
scr.onkey(s.k_up, "Up")
scr.onkey(s.k_down, "Down")
scr.onkey(s.k_left, "Left")
scr.onkey(s.k_right, "Right")

is_game_on = True
while is_game_on:
    # Used to move the snake by default
    s.move_snake()

    # Detecting collision
    if s.head.distance(f) < 10:
        f.new_pos()
        sc.increase_score()

scr.exitonclick()
