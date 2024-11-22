from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess

def billing():
    root.destroy()
    subprocess.run(['python','billing.py'])

def view_menu():
    root.destroy()
    subprocess.run(['python','view menu.py'])

def add():
    root.destroy()
    subprocess.run(['python','add.py'])

def emp_info():
    root.destroy()
    subprocess.run(['python', 'employee.py'])

def exitt():
    root.destroy()
    
root = Tk()
root.title("Employee dashboard")
root.geometry("1250x500")
root.configure(bg="white")
img = PhotoImage(file="assets/empdash.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)

img1 = PhotoImage(file="assets/billing.png")
b1 = Button(root,border=0,image=img1,command=billing)
b1.place(x=80, y=130)
img2 = PhotoImage(file="assets/menu.png")
b2 = Button(root, border=0,image=img2, command=view_menu)
b2.place(x=355, y=130)
img3 = PhotoImage(file="assets/add.png")
b3 = Button(root, border=0, image = img3, command=add)
b3.place(x=640, y=130)
img5 = PhotoImage(file="assets/empinfo.png")
b5 = Button(root, border=0, image=img5, command=emp_info)
b5.place(x=930, y=130)
b6 = Button(root, height=1, width=10, border=0, text="Exit", fg="black", bg="pink",command=exitt)
b6.place(x=580, y=420)
root.mainloop()
