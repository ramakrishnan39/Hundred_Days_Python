import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdead"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.2
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    win.after_cancel(timer)
    can_centre.itemconfigure(tom_can, text="00:00")
    lbl_timer.config(text="Timer")
    lbl_check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        lbl_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        lbl_timer.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        lbl_timer.config(text="Work Session", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    can_centre.itemconfigure(tom_can, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = win.after(1000, countdown, count - 1)
    else:
        global reps
        start_timer()
        mark = ""
        working_sess = math.floor(reps / 2)

        for _ in range(working_sess):
            mark += "✅"

        lbl_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

win = tk.Tk()
win.title("Pomodora App")
win.config(padx=100, pady=50, bg=YELLOW)

lbl_timer = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
lbl_timer.grid(row=0, column=2)

can_centre = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = tk.PhotoImage(file="tomato.png")
can_centre.create_image(100, 112, image=tom_img)
tom_can = can_centre.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
can_centre.grid(row=2, column=2)

btn_start = tk.Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
btn_start.grid(row=3, column=1)

btn_reset = tk.Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
btn_reset.grid(row=3, column=3)

lbl_check = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
lbl_check.grid(row=4, column=2)

win.mainloop()
