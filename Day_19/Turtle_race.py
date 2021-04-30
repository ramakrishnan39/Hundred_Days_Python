from turtle import Turtle,Screen

scr = Screen()

scr.setup(520,400)
u_in = scr.textinput(title="Your Input",prompt="Which color do you think will win the race? ")
colors = ["red","yellow","blue","green","orange","purple"]
y_pos = [-80,-50,-20,10,40,70]

for t_i in range(0,6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[t_i])
    tim.penup()
    tim.goto(x=-250,y = y_pos[t_i])

scr.exitonclick()