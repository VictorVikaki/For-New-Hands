from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Simple Login Form")

title=Label(root, text="SIMPLE LOGIN FORM", font="bold")
title.place(x=100, y=50)

username=Label(root,text="Username:", font="bold")
username.place(x=50, y=100)
e1=Entry(root)
e1.place(x=200, y=100)

password=Label(root,text="Password:", font="bold")
password.place(x=50, y=150)
e2=Entry(root)
e2.place(x=200, y=150)

confirm=Label(root,text="Confirm:", font="bold")
confirm.place(x=50, y=200)
e3=Entry(root)
e3.place(x=200, y=200)

Button(text="Login", font="bold").place(x=200, y=250)

root.mainloop()