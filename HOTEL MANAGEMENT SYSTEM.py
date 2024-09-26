from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
import tempfile

root = Tk()
root.geometry("1300x620")
root.title("VICTOR")
root.resizable(TRUE, TRUE)
root.withdraw()

# Loading screen
def start():
    import time

    my_pb["value"] = 10
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 30
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 60
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 80
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 100
    root.update_idletasks()
    time.sleep(1)

    load.destroy()
    login_screen.deiconify()

load = Toplevel()
load.geometry("400x200")
load.title("Loading Page")
load.resizable(FALSE, FALSE)
load.configure(bg="white")
load.overrideredirect(1)

mn = Label(load, font=("arial", 18, "bold"), fg="black", bg="white")
mn.place(x=170, y=60)

my_pb = Progressbar(load, orient='horizontal', mode='determinate', length=350)
my_pb.place(x=20, y=120)

label_1 = Label(load, text="Loading", fg='black', font=("Microsoft YaHei UI Light", 11), bg="white")
label_1.pack(side=TOP)

label_2 = Label(load, text="Please Wait....", bg="white")
label_2.place(x=150, y=90)

start_btn = Button(load, text='Start', command=start)
start_btn.place(x=170, y=160)

# Login screen
login_screen = Toplevel()
login_screen.geometry('400x300')
login_screen.resizable(FALSE, FALSE)
login_screen.title("VICTOR")
login_screen.configure(bg="white")
login_screen.overrideredirect(1)
login_screen.withdraw()

def on_enter_user(e):
    if user.get() == 'Username':
        user.delete(0, "end")

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, "Username")

user = Entry(login_screen, width=25, bd=5, relief=FLAT, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

def on_enter_code(e):
    if code.get() == 'Password':
        code.delete(0, "end")
        code.config(show="*")

def on_leave_code(e):
    if code.get() == '':
        code.config(show="")
        code.insert(0, "Password")

code = Entry(login_screen, bd=5, width=25, relief=FLAT, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)

def login():
    username = user.get()
    password = code.get()

    if username == "Victor" and password == "1234":
        login_screen.destroy()
        root.deiconify()
    else:
        messagebox.showerror("Invalid", "Invalid username or password")

login_btn = Button(login_screen, text="Login", command=login)
login_btn.place(x=150, y=200)

# Main form
l1 = Label(root, text="HOTEL MANAGEMENT SYSTEM", font=('arial', 36, 'bold'))
l1.place(x=200, y=0)

can_cvas = Canvas(root, width=1300, height=5)
line = can_cvas.create_line(0, 0, 1300, 0, width=10, fill="deep sky blue")
can_cvas.place(x=0, y=50)

#Customer Name
name = Label(root, text="Customer Name", font=('arial', 14, 'bold'), fg="navy")
name.place(x=0, y=65)
e1 = Entry(root, font=('arial', 15))
e1.place(x=180, y=65, width=430, height=30)

can_vas = Canvas(root, width=620, height=15)
line2 = can_vas.create_line(0, 0, 620, 0, width=15, fill="midnight blue")
can_vas.place(x=0, y=100)

# cold drinks
f1 = Frame(root, width=300, height=485)
f1.place(x=0, y=105)
canvas1 = Canvas(f1, width=295, height=480)
rectangle = canvas1.create_rectangle(3, 15, 290, 475, outline="dim grey")
canvas1.place(x=3, y=5)
colddrinks = Label(f1, text="Cold Drinks", font=('arial', 18, 'bold'), fg="navy")
colddrinks.place(x=15, y=5)
soda = Label(f1, text="Soda", font=('arial', 16, 'bold'), fg="green")
soda.place(x=15, y=55)
sodaentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
sodaentry.place(x=110, y=55, width=180, height=30)
water = Label(f1, text="Water", font=('arial', 16, 'bold'), fg="green")
water.place(x=15, y=105)
waterentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
waterentry.place(x=110, y=105, width=180, height=30)
juice = Label(f1, text="Juice", font=('arial', 16, 'bold'), fg="green")
juice.place(x=15, y=155)
juiceentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
juiceentry.place(x=110, y=155, width=180, height=30)
wine = Label(f1, text="Wine", font=('arial', 16, 'bold'), fg="green")
wine.place(x=15, y=205)
wineentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
wineentry.place(x=110, y=205, width=180, height=30)

# foods
f2 = Frame(root, width=310, height=490)
f2.place(x=301, y=105)
canvas2 = Canvas(f2, width=305, height=485)
rectangle2 = canvas2.create_rectangle(3, 15, 300, 480, outline="dim grey")
canvas2.place(x=3, y=5)
foods = Label(f2, text="Foods", font=('arial', 18, 'bold'), fg="navy")
foods.place(x=15, y=5)
matoke = Label(f2, text="Matoke", font=('arial', 16, 'bold'), fg="green")
matoke.place(x=15, y=65)
matokeentry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
matokeentry.place(x=110, y=65, width=190, height=30)
rice = Label(f2, text="Rice", font=('arial', 16, 'bold'), fg="green")
rice.place(x=15, y=125)
riceentry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
riceentry.place(x=110, y=125, width=190, height=30)
ugali = Label(f2, text="Ugali", font=('arial', 16, 'bold'), fg="green")
ugali.place(x=15, y=185)
ugalientry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
ugalientry.place(x=110, y=185, width=190, height=30)

# hot drinks
f3 = Frame(f1, width=280, height=235)
f3.place(x=10, y=241)
canvas3 = Canvas(f3, width=275, height=230)
rectangle3 = canvas3.create_rectangle(5, 15, 270, 225, outline="dim grey")
canvas3.place(x=5, y=5)
hotdrinks = Label(f3, text="Hot Drinks", font=('arial', 18, 'bold'), fg="navy")
hotdrinks.place(x=15, y=5)
coffee = Label(f3, text="Coffee", font=('arial', 16, 'bold'), fg="black")
coffee.place(x=15, y=45)
coffeeentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
coffeeentry.place(x=120, y=45, width=150, height=30)
tea = Label(f3, text="Tea", font=('arial', 16, 'bold'), fg="black")
tea.place(x=15, y=85)
teaentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
teaentry.place(x=120, y=85, width=150, height=30)
milk = Label(f3, text="Milk", font=('arial', 16, 'bold'), fg="black")
milk.place(x=15, y=125)
milkentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
milkentry.place(x=120, y=125, width=150, height=30)

# fruits
f4 = Frame(f2, width=280, height=235)
f4.place(x=15, y=250)
canvas4 = Canvas(f4, width=275, height=230)
rectangle4 = canvas4.create_rectangle(5, 15, 270, 225, outline="dim grey")
canvas4.place(x=5, y=5)
fruits = Label(f4, text="Fruits", font=('arial', 18, 'bold'), fg="navy")
fruits.place(x=15, y=5)
mangoes = Label(f4, text="Mangoes", font=('arial', 16, 'bold'), fg="black")
mangoes.place(x=15, y=45)
mangoesentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
mangoesentry.place(x=150, y=45, width=120, height=30)
apples = Label(f4, text="Apples", font=('arial', 16, 'bold'), fg="black")
apples.place(x=15, y=85)
applesentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
applesentry.place(x=150, y=85, width=120, height=30)
oranges = Label(f4, text="Oranges", font=('arial', 16, 'bold'), fg="black")
oranges.place(x=15, y=125)
orangesentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
orangesentry.place(x=150, y=125, width=120, height=30)

# receipt
f5 = Frame(root, width=375, height=430)
f5.place(x=606, y=55)
canvas5 = Canvas(f5, width=370, height=425)
rectangle5 = canvas5.create_rectangle(5, 15, 365, 420, outline="dim grey")
canvas5.place(x=5, y=5)
receipt = Label(f5, text="Receipt", font=('arial', 18, 'bold'), fg="navy")
receipt.place(x=15, y=5)
text = Text(f5, width=42, height=22, wrap=WORD)
text.place(x=20, y=50)

# calculator
f6 = Frame(root, width=315, height=430)
f6.place(x=981, y=55)
canvas6 = Canvas(f6, width=310, height=425)
rectangle6 = canvas6.create_rectangle(5, 5, 300, 420, outline="dim grey")
canvas6.place(x=5, y=5)
calculator = Label(f6, text="Calculator", font=('arial', 12), fg="black")
calculator.place(x=15, y=0)

text_input = StringVar()
operator = ""

def buttonclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def buttoncleardisplay():
    global operator
    operator = ""
    text_input.set("")


def buttonequals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


textDisplay = Entry(f6, font=('arial', 20, 'bold'), textvariable=text_input, bd=8, insertwidth=4,
                   bg='White', justify='right')
textDisplay.place(x=15, y=20, width=280)

button7 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='7',
            command=lambda: buttonclick(7)).place(x=15, y=70)
button8 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='8',
            command=lambda: buttonclick(8)).place(x=85, y=70)
button9 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='9',
            command=lambda: buttonclick(9)).place(x=155, y=70)
buttonaddition = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='+', width=2,
                   command=lambda: buttonclick("+")).place(x=225, y=70)

button4 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='4',
            command=lambda: buttonclick(4)).place(x=15, y=140)
button5 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='5',
            command=lambda: buttonclick(5)).place(x=85, y=140)
button6 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='6',
            command=lambda: buttonclick(6)).place(x=155, y=140)
buttonsubtraction = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='-', width=2,
                      command=lambda: buttonclick("-")).place(x=225, y=140)

button1 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='1',
            command=lambda: buttonclick(1)).place(x=15, y=210)
button2 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='2',
            command=lambda: buttonclick(2)).place(x=85, y=210)
button3 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='3',
            command=lambda: buttonclick(3)).place(x=155, y=210)
buttonmultiplication = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='*', width=2,
                         command=lambda: buttonclick("*")).place(x=225, y=210)

button0 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='0',
            command=lambda: buttonclick(0)).place(x=15, y=280)
buttondecimal = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 25, 'bold'), text='.',
                  command=lambda: buttonclick(".")).place(x=85, y=280)
buttonclear = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='C',
                command=lambda: buttoncleardisplay()).place(x=155, y=280)
buttondivision = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='/', width=2,
                   command=lambda: buttonclick("/")).place(x=225, y=280)

buttonequals = Button(f6, padx=16, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='=', width=14,
                 command=buttonequals).place(x=15, y=350)

def Reset():
    e1.delete(0, END)
    sodaentry.delete(0, END)
    waterentry.delete(0, END)
    juiceentry.delete(0, END)
    wineentry.delete(0, END)
    coffeeentry.delete(0, END)
    teaentry.delete(0, END)
    milkentry.delete(0, END)
    matokeentry.delete(0, END)
    riceentry.delete(0, END)
    ugalientry.delete(0, END)
    mangoesentry.delete(0, END)
    applesentry.delete(0, END)
    orangesentry.delete(0, END)
    taxentry.delete(0, END)
    totalentry.delete(0, END)
    text.delete('0.0', END)


def Exit():
    Exit = messagebox.askyesno("Quit System", "Do you want to Quit?")
    if Exit > 0:
        root.destroy()
        return


def printreceipt():
    r = text.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(r)
    os.startfile(filename, "print")


# total
def Total():
    try:
        a1 = int(sodaentry.get())
    except:
        a1 = 0
    try:
        a2 = int(waterentry.get())
    except:
        a2 = 0
    try:
        a3 = int(juiceentry.get())
    except:
        a3 = 0
    try:
        a4 = int(wineentry.get())
    except:
        a4 = 0
    try:
        a5 = int(coffeeentry.get())
    except:
        a5 = 0
    try:
        a6 = int(teaentry.get())
    except:
        a6 = 0
    try:
        a7 = int(milkentry.get())
    except:
        a7 = 0
    try:
        a8 = int(matokeentry.get())
    except:
        a8 = 0
    try:
        a9 = int(riceentry.get())
    except:
        a9 = 0
    try:
        a10 = int(ugalientry.get())
    except:
        a10 = 0
    try:
        a11 = int(mangoesentry.get())
    except:
        a11 = 0
    try:
        a12 = int(applesentry.get())
    except:
        a12 = 0
    try:
        a13 = int(orangesentry.get())
    except:   
        a13 = 0

    sodaprice = 100.0
    waterprice = 50.0
    juiceprice = 70.0
    wineprice = 2500.0
    matokeprice = 130.0
    riceprice = 120.0
    ugaliprice = 90.0
    coffeeprice = 60.0
    teaprice = 25.0
    milkprice = 40.0
    mangoesprice = 200.0
    applesprice = 15.0
    orangesprice = 20.0

    totsoda = float(a1) * sodaprice
    totwater = float(a2) * waterprice
    totjuice = float(a3) * juiceprice
    totwine = float(a4) * wineprice
    totcoffee = float(a5) * coffeeprice
    tottea = float(a6) * teaprice
    totmilk = float(a7) * milkprice
    totmatoke = float(a8) * matokeprice
    totrice = float(a9) * riceprice
    totugali = float(a10) * ugaliprice
    totmangoes = float(a11) * mangoesprice
    totapples = float(a12) * applesprice
    totoranges = float(a13) * orangesprice

    totalcost = (totsoda + totwater + totjuice + totwine + totcoffee + tottea + totmilk + totmatoke
                 + totrice + totugali + totmangoes + totapples + totoranges)
    paytax = (totalcost * 0.016)
    tax.set(paytax)
    overall = "Kshs", (paytax + totalcost)
    mytotal.set(overall)

    sentense = ("Hello, " + e1.get() + "\n Items   Amount   price"
                                       "\n  Soda       " + str(
        sodaentry.get()) + "      " +
                str(sodaprice) + "\n  Water      " + str(waterentry.get()) + "      " +
                str(waterprice) + "\n  Juice      " + str(juiceentry.get()) + "      " +
                str(juiceprice) + "\n  Wine       " +
                str(wineentry.get()) + "      " + str(wineprice) + "\n  Matoke     " +
                str(matokeentry.get()) + "      " + str(matokeprice)
                + "\n  Rice       " + str(riceentry.get()) + "      " + str(riceprice) + "\n  Ugali      " +
                str(ugalientry.get()) + "      " + str(ugaliprice) + "\n  Coffee     "
                + str(coffeeentry.get()) + "      " + str(coffeeprice) + "\n  Tea       " +
                str(teaentry.get()) + "      " + str(teaprice) + "\n  Milk  " +
                str(milkentry.get()) + "      " + str(milkprice) + "\n  Mangoes       " +
                str(mangoesentry.get()) + "      " + str(mangoesprice) + "\n  Apples      " +
                str(applesentry.get()) + "      " +
                str(applesprice) + "\n  Oranges " + str(orangesentry.get()) + "      " +
                str(orangesprice) + "\n\n  Tax   " + str(taxentry.get()) + "\n\n  Total   " +
                str(totalentry.get()) +
                "\n\nThank you for your visit ")
    text.insert(0.0, sentense)


tax = StringVar()
mytotal = StringVar()

lbltax = Label(root, text="Tax", font=('arial', 16, 'bold'), fg="firebrick")
lbltax.place(x=700, y=490)
taxentry = Entry(root, bg="powder blue", font=('arial', 17, 'bold'), justify=RIGHT, textvariable=tax)
taxentry.place(x=850, y=490, width=350, height=30)

btotal = Button(root, text="Total", fg="firebrick", bg="powder blue", font=('arial', 18, 'bold'), command=Total)
btotal.place(x=650, y=530, width=180, height=30)
totalentry = Entry(root, bg="powder blue", font=('arial', 17, 'bold'), justify=RIGHT, textvariable=mytotal)
totalentry.place(x=850, y=530, width=350, height=30)

print = Button(root, text="Print Receipt", fg="firebrick", bg="powder blue", font=('arial', 18, 'bold'),command=printreceipt)
print.place(x=650, y=580, width=180, height=30)

reset = Button(root, text="Reset", fg="firebrick", bg="powder blue", font=('arial', 18, 'bold'), command=Reset)
reset.place(x=850, y=580, width=180, height=30)

exit = Button(root, text="Exit", fg="firebrick", bg="powder blue", font=('arial', 18, 'bold'), command=Exit)
exit.place(x=1020, y=580, width=180, height=30)


def exit():
    root.destroy()


# login system placeholder functions
def logout():
    root.withdraw()
    login_screen.deiconify()

root.protocol("WM_DELETE_WINDOW", logout)

login_screen.withdraw()
root.withdraw()
root.mainloop()