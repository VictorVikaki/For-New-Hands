import tkinter as tk
root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x150")


label = tk.Label(root, text="This is the label widget", width=300, height=150,
                 bg="black", fg="yellow")
label.pack()

root.mainloop()