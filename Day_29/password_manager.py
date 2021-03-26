from tkinter import *

BG_COLOR = "#F39189"
FONT_NAME = "Helvetica"

win = Tk()
win.title("Password Manager")
win.config(bg=BG_COLOR, padx=50, pady=50)

l_can = Canvas(height=220, width=200, bg=BG_COLOR, highlightthickness=0)
img_lock = PhotoImage(file="password_icon.png")
l_can.create_image(110, 70, image=img_lock)
l_can.grid(row=0, column=0)

# Labels
lbl_web = Label(text="Website                          :", bg=BG_COLOR, anchor="e", justify="left")
lbl_email = Label(text="Email ID/Username      :", bg=BG_COLOR, anchor="e", justify="left")
lbl_pass = Label(text="Password                      :", bg=BG_COLOR, anchor="e", justify="left")

lbl_web.grid(row=1, column=0)
lbl_email.grid(row=2, column=0)
lbl_pass.grid(row=3, column=0)

# Entries

txt_web = Entry(width=35)
txt_web.focus()
txt_email = Entry(width=25)
txt_email.insert(0,"ramkrishp3@gmail.com")
txt_pass = Entry(width=35)

txt_web.grid(row=1, column=1,columnspan=2)
txt_email.grid(row=2, column=1,columnspan=1)
txt_pass.grid(row=3, column=1,columnspan=2)

#Buttons
btn_genpass= Button(text="Generate")
btn_genpass.grid(row=2,column=2)
win.mainloop()
