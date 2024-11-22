from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import mysql.connector as nk

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()

def add_values():
    itemn = e1.get()
    cat = e2_var.get()
    vnv = e3_var.get()
    price = e4.get()
    if(vnv=="Vegetarian"):
        vnv = 'V'
    else:
        vnv = 'NV'
    q = "insert into menu(itemname, category, v_nv, price) values('{}','{}','{}',{})".format(itemn,cat,vnv,price)
    curdb.execute(q)
    db.commit()
    messagebox.showinfo(' ','Item added successfully')
    root1.destroy()

root1 = Tk()
root1.title("Add items")
root1.geometry("1000x500")
root1.configure(bg="white")
img1 = PhotoImage(file="assets/login1.png")
pic1 = Label(root1, image=img1)
pic1.place(x=0, y=0)
frame1 = Frame(root1,bg="white",width=450, height=450)
frame1.place(x=270, y=25)
l = Label(frame1, bg="white", fg="#48b74b", text="ADD ITEM",font=("Microsoft New Tai Lue",20,"italic bold"))
l.place(x=150, y=20)
e1 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
e1.place(x=360, y=130)
e1.insert(0,"Item Name")
l1 = Frame(root1, bg="black", width=269, height=2)
l1.place(x=360, y=160)
l2 = Label(root1, text="Category", bg="white", font=("Microsoft YaHei UI light", 12))
l2.place(x=360, y=180)
cat_options = ["Starters", "Tiffin", "Chicken", "Rotti", "Gravy", "Dessert"]
e2_var = StringVar(root1)
e2_var.set(cat_options[0])
e2 = OptionMenu(root1, e2_var, *cat_options)
e2.place(x=360, y=210)
e2.config(bg="#c1e381", fg="black", width=15)
l3 = Label(root1, text="Veg / Non-Veg", bg="white", font=("Microsoft YaHei UI light", 12))
l3.place(x=360, y=260)
options = ["Vegetarian","Non-Vegetarian"]
e3_var = StringVar(root1)
e3_var.set(options[0])
e3 = OptionMenu(root1, e3_var, *options)
e3.place(x=360, y=290)
e3.config(bg="#c1e381", fg="black", width=15)
e4 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
e4.place(x=360, y=350)
e4.insert(0,"Price (in numbers)")
l4 = Frame(root1, bg="black", width=269, height=2)
l4.place(x=360, y=380)
b1 = Button(frame1, text="Confirm",width = 10, border=0, bg="#c1e381",fg="white", font=("Microsoft YaHei UI light", 12),command=add_values)
b1.place(x=170, y=390)
root1.mainloop()
