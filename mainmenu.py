from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess

def exitt():
    messagebox.askquestion("Warning", "Do you want to exit the application?")
    if "yes":
        root.destroy()
    else:
        messagebox.showinfo(' ',"Did not exit from Mainmenu")

def modify():
    root.destroy()
    subprocess.run(['python', 'modify.py'])


def view_menu():
    root.destroy()
    subprocess.run(['python','view menu.py'])

def view_cust():
    root.destroy()
    subprocess.run(['python','view customer.py'])

def login():
    root.destroy()
    subprocess.run(['python', 'login.py'])

def emp_info():
    root.destroy()
    subprocess.run(['python', 'employee.py'])

def billing():
    root.destroy()
    subprocess.run(['python','bill.py'])
        
root = Tk()
root.title("MainMenu")
root.geometry("1250x500")
root.configure(bg="white")
img = PhotoImage(file="assets/main.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)
img1 = PhotoImage(file="assets/bill2.png")
b1 = Button(root,border=0,image=img1,command=billing)
b1.place(x=20, y=130)
img2 = PhotoImage(file="assets/menu.png")
b2 = Button(root, border=0,image=img2, command=view_menu)
b2.place(x=265, y=130)
img3 = PhotoImage(file="assets/modim.png")
b3 = Button(root, border=0, image = img3, command=modify)
b3.place(x=510, y=130)
img4 = PhotoImage(file="assets/custo.png")
b4 = Button(root, border=0,image = img4, command=view_cust)
b4.place(x=755, y=130)
img5 = PhotoImage(file="assets/empinfo.png")
b5 = Button(root, border=0, image=img5, command=emp_info)
b5.place(x=1000, y=130)
b6 = Button(root, height=1, width=10, border=0, text="Exit", fg="black", bg="pink",command=exitt)
b6.place(x=580, y=400)
b7 = Button(root, height=1, width=30, border=0, text="Login to another Account", fg="black", bg="#E0B7F4",command=login)
b7.place(x=515, y=435)
root.mainloop()
