import tkinter as tk
root=tk.Tk()
root.title("Welcome to Python GUI world")
root.geometry('300x200')
txt1=tk.Entry(root)
txt1.pack()
txt2=tk.Entry(root)
txt2.pack()

def add():
    n1=int(txt1.get())
    n2=int(txt2.get())
    msg=tk.Message(root,text=n1+n2)
    msg.pack()
def min():
    n1=int(txt1.get())
    n2=int(txt2.get())
    msg=tk.Message(root,text=n1-n2)
    msg.pack()
def mul():
    n1=int(txt1.get())
    n2=int(txt2.get())
    msg=tk.Message(root,text=n1*n2)
    msg.pack()
def div():
    n1=int(txt1.get())
    n2=int(txt2.get())
    msg=tk.Message(root,text=n1/n2)
    msg.pack()
btnadd=tk.Button(root,text="Add",command=add)
btnadd.pack()
btnmin=tk.Button(root,text="Minus",command=min)
btnmin.pack()
btnmul=tk.Button(root,text="Multiple",command=mul)
btnmul.pack()
btndiv=tk.Button(root,text="Division",command=div)
btndiv.pack()
btnext=tk.Button(root,text="Exit",command=root.destroy)
btnext.pack()
root.mainloop()