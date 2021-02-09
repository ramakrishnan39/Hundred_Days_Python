import random
import tkinter as tk
from tkinter import *
m= tk.Tk()
m.title("Kichu Kichu Thambalam")
m.geometry('640x480')

all_plots = []
str_plots = ""

l1=tk.Label(m,text="Tell me the number of Sand plots (should be 5 to 13) ")
t1=tk.Entry(m)
l2=tk.Label(m,text="Guess where the star will be ")

l3=tk.Label(m)
l4=tk.Label(m)
t2=tk.Entry(m)
msg=tk.Message()
p_flag=""

r1=tk.Radiobutton(m,text="Yes",variable = p_flag,value="yes")
r2=tk.Radiobutton(m,text="No",variable = p_flag,value="no")

def set_yes():
    global p_flag
    p_flag="yes"


def set_no():
    global p_flag
    p_flag="no"


def set_plots(pn_plots):
    global all_plots,str_plots
    str_plots=""
    for k in range(1, pn_plots + 1):
        all_plots.append('-')
    str_plots = ' '.join(map(str, all_plots))


def see():
    global all_plots,str_plots
    plots = t1.get() if t1.get() else l3.config(text="Please enter any value")
    n_plots=int(plots)
    if 5 <= n_plots <= 13:
        set_plots(n_plots)
        l3.config(text=str_plots)
        l2.pack()
        t2.pack()
        btn2.pack()
    else:
        l3.config(text="Sorry ! Please tell me your choice as between 5 to 13 !")


def choose_plot():
    global all_plots, str_plots
    plots = t1.get() if t1.get() else l3.config(text="Please enter any value")
    """This function is used to choose the plot in Kichu Kichu game"""
    set_plots(int(plots))
    print(len(str_plots))
    star_plot = random.choice(range(0, len(str_plots) - 1))
    print(star_plot)
    all_plots[star_plot] = '*'
    user_guess = int(t2.get()) if t2.get() else l3.config(text="Enter a valid choice!")
    str_plots = ' '.join(map(str, all_plots))
    l3.config(text=str_plots)
    if star_plot == user_guess - 1:
        l4.config(text="Yeah !!! You won  ")
        l4.pack()
    else:
        l4.config(text="Oh you lose my dear! don't worry try again! ")
        l4.pack()


def play():
    global msg, all_plots, str_plots

    while p_flag.lower() == 'y' or p_flag.lower() == 'yes':
        all_plots = []
        str_plots = ""
        choose_plot()
        l4.config(text="Do you wish to continue ? ")
        l4.pack()
    else:
        l3.config(text="You selected No")


btn1 = tk.Button(m,text="See sand clouds ",command=see)
btn2 = tk.Button(m,text="Guess", command=play)
l1.pack()
t1.pack()
btn1.pack()
l3.pack()


m.mainloop()



