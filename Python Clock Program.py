from tkinter import*
from time import*

def update():
    time_string = strftime("%I:%M:%S %p")
    time_Label.config(text=time_string)

    day_string = strftime("%A")
    day_Label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_Label.config(text=date_string)

    window.after(1000,update)
 


window = Tk()

time_Label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_Label.pack()

day_Label = Label(window,font=("Ink Free",25))
day_Label.pack()

date_Label = Label(window, font=("Ink Free",30))
date_Label.pack()

update()

window.mainloop()