from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image
import subprocess

def mainmenu():
    root.destroy()
    subprocess.run(['python','mainmenu.py'])

def billing():
    root.destroy()
    subprocess.run(['python','billing.py'])

def statement():
    root.destroy()
    subprocess.run(['python','billsummary.py'])

root = Tk()
root.title("Billing")
root.geometry("1000x500")
root.configure(bg="white")
img = PhotoImage(file="assets/login.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)
img1 = PhotoImage(file="assets/billing.png")
b1 = Button(root, border=0, image=img1, command=billing)
b1.place(x=230, y=110)
img2 = PhotoImage(file="assets/statement.png")
b2 = Button(root, border=0, image=img2, command=statement)
b2.place(x=530, y=110)
b3 = Button(root, height=1, width=10,border=0, text="Back", bg="pink", fg="black", command=mainmenu)
b3.place(x=460, y=390)
l1 = Label(root, text="BILLING", font=("Helvetica",18))
l1.place(x=430, y=20)
root.mainloop()
