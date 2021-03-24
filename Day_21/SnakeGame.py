from turtle import Screen
from m_snake import Snake
from m_food import Food
from m_scoreboard import Score
import time

scr = Screen()
scr.setup(height=600, width=600)
scr.bgcolor("peru")
scr.title("Snake")
scr.tracer(0)

snake = Snake()
food = Food()
score = Score()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")
is_game_on = True

while is_game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detects food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.update_score()
        snake.expand()

    # Detects wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.gameover()
        is_game_on = False

    # Detects its own tail
    for seg in snake.seg_list:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            is_game_on = False
            score.gameover()

scr.exitonclick()
