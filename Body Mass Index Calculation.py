from tkinter import*

root=Tk()
root.geometry("600x380+0+0")
root.title("Body Mass Index")

frame1 = Frame(root,pady=10,bd=16)
frame1.grid()

weight = StringVar()
height = StringVar()
result = StringVar()

frame2 = Frame(frame1,width=550,height=190,pady=10,bd=16,relief = "sunken")
frame2.grid(row = 0,column = 0)

frame3 = Frame(frame1,width=550,height=190,pady=10,bd=16,relief = "sunken")
frame3.grid(row = 1,column = 0)

lblweight = Label(frame2,text='Enter Your Weight',font=('arial',14,'bold'),bd=12)
lblweight.grid(row=0,column=0,sticky=W)
lblweight = Entry(frame2,textvariable=weight,font=('arial',14,'bold'),bd=12)
lblweight.grid(row=0,column=1,sticky=W)
lblkg = Label(frame2,text='kg',font=('arial',14,'bold'),bd=12)
lblkg.grid(row=0,column=2,sticky=W)

lblheight = Label(frame2,text='Enter Your Height',font=('arial',14,'bold'),bd=12)
lblheight.grid(row=1,column=0,sticky=W)
lblheight = Entry(frame2,textvariable=height,font=('arial',14,'bold'),bd=12)
lblheight.grid(row=1,column=1,sticky=W)
lblcm = Label(frame2,text='cm',font=('arial',14,'bold'),bd=12)
lblcm.grid(row=1,column=2,sticky=W)

lblresult = Label(frame2,text='Show Result(BMI)',font=('arial',14,'bold'),bd=12)
lblresult.grid(row=2,column=0,sticky=W)
lblresult = Entry(frame2,textvariable=result,font=('arial',14,'bold'),bd=12)
lblresult.grid(row=2,column=1,sticky=W)

def add():
    f = float(lblweight.get())
    s = float(lblheight.get())/100 #cm convert to meter
    a = f/(s*s)
    b = round(a, 2)
    result.set(b)

def Rest():
    weight.set("") 
    height.set("")
    result.set("") 

def Exit():
    root.destroy()     

btnTotal = Button(frame3,text='Total',font=('arial',14,'bold'),bd=12,pady=12,
                  width = 8, command= add)
btnTotal.grid(row=0,column=0)
btnReset = Button(frame3,text='Reset',font=('arial',14,'bold'),bd=12,pady=12,
                  width = 8,command=Rest)
btnReset.grid(row=0,column=1)
btnExit = Button(frame3,text='Exit',font=('arial',14,'bold'),bd=12,pady=12,
                  width = 8, command= Exit)
btnExit.grid(row=0,column=2)



root.mainloop()