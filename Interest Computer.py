from tkinter import*

root=Tk()
root.geometry("500x300")
root.title("Simple Interest Calculator")

def Calculate():
    prin=int(principalentry.get())
    rat=int(rateentry.get())
    tim=int(timeentry.get())
    amount=(prin*rat*tim)/100
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)

principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="Interest Rate:",font="arial 15")
time=Label(root,text="Time:",font="arial 15")

interest=Label(root,text="Interest:",font="arial 15")
interest.place(x=50,y=230)

principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)

principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()

principalentry=Entry(root,textvariable=principalvalue,font="arial 20",width=8)
rateentry=Entry(root,textvariable=ratevalue,font="arial 20",width=8)
timeentry=Entry(root,textvariable=timevalue,font="arial 20",width=8)

Button(text="Calculate",font="arial 15",command=Calculate).place(x=370,y=20)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=370,y=90)

principalentry.place(x=200,y=20)
rateentry.place(x=200,y=90)
timeentry.place(x=200,y=160)

root.mainloop()