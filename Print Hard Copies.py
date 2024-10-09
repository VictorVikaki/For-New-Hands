from tkinter import *
import os
import tempfile
from tkinter import scrolledtext as st

root = Tk()
root.geometry('800x550')

def print_command(txt):
    print_item = tempfile.mktemp('.txt')
    open(print_item,'w').write(txt)
    os.startfile(print_item, 'print')

textArea = st.ScrolledText(root,width=50, height=20)
textArea.place(x=50,y=50)

print_btn = Button(root,text='Print',command=lambda: print_command(textArea.get('1.0',END)))
print_btn.place(x=200,y=450)

name = "\n\n\n\tPLEASE SUBSCRIBE TO MY CHANNEL\n\t\t\t\n" +("-"*50) + "\n\n\t THANK YOU"
textArea.insert('insert',name)


root.mainloop()