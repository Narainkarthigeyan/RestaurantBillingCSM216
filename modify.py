from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import mysql.connector as nk

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()

def show():
    global text
    text = click.get()
    
def mainmenu():
    messagebox.askquestion("Warning", "Do you want to return to Mainmenu?")
    if "yes":
        root.destroy()
        subprocess.Popen(['python', 'Mainmenu.py'])

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

def update_values():
    item = en1.get()
    cat = en2.get()
    newprice = en3.get()
    q1 = "update menu set Price = {} where ItemName = '{}'".format(newprice, item)
    curdb.execute(q1)
    db.commit()
    messagebox.showinfo(' ',"Price Updated Successfully")

def remove_values():
    itemn = ent1.get()
    cat = ent2.get()
    q2 = "delete from menu where ItemName = '{}'".format(itemn)
    curdb.execute(q2)
    db.commit()
    messagebox.showinfo(' ', "Item deleted successfully")

def add_items():
    global e1,e2_var,e3_var,e4
    root1 = Toplevel(root)
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

def update():
    global en1, en2, en3
    root2 = Toplevel(root)
    root2.title("Update item price")
    root2.geometry("1000x500")
    root2.configure(bg="white")
    img2 = PhotoImage(file="assets/login1.png")
    pic2 = Label(root2, image=img2)
    pic2.place(x=0, y=0)
    frame2 = Frame(root2,bg="white",width=450, height=450)
    frame2.place(x=270, y=25)
    l = Label(frame2, bg="white", fg="#48b74b", text="UPDATE ITEM PRICE",font=("Microsoft New Tai Lue",20,"italic bold"))
    l.place(x=90, y=20)

    en1 = Entry(root2, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    en1.place(x=360, y=130)
    en1.insert(0,"Item Name")
    ln1 = Frame(root2, bg="black", width=269, height=2)
    ln1.place(x=360, y=160)

    en2 = Entry(root2, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    en2.place(x=360, y=200)
    en2.insert(0,"Category")
    ln2 = Frame(root2, bg="black", width=269, height=2)
    ln2.place(x=360, y=230)

    en3 = Entry(root2, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    en3.place(x=360, y=275)
    en3.insert(0,"New Price (in numbers)")
    ln3 = Frame(root2, bg="black", width=269, height=2)
    ln3.place(x=360, y=305)
    b1 = Button(frame2, height=1, width=15, border=0, text="Confirm",bg="#c1e381",fg="white",font=("Microsoft New Tai Lue",15,"italic"),command=update_values)
    b1.place(x=135, y=340)
    root2.mainloop()

def remove():
    global ent1, ent2
    root3 = Toplevel(root)
    root3.title("Remove item")
    root3.geometry("1000x500")
    root3.configure(bg="white")
    img3 = PhotoImage(file="assets/login1.png")
    pic3 = Label(root3, image=img3)
    pic3.place(x=0, y=0)
    frame3 = Frame(root3,bg="white",width=450, height=450)
    frame3.place(x=270, y=25)
    l = Label(frame3, bg="white", fg="#48b74b", text="REMOVE  AN  ITEM",font=("Microsoft New Tai Lue",20,"italic bold"))
    l.place(x=100, y=20)

    ent1 = Entry(root3, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    ent1.place(x=360, y=130)
    ent1.insert(0,"Item Name")
    lnt1 = Frame(root3, bg="black", width=269, height=2)
    lnt1.place(x=360, y=160)

    ent2 = Entry(root3, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    ent2.place(x=360, y=230)
    ent2.insert(0,"Category")
    lnt2 = Frame(root3, bg="black", width=269, height=2)
    lnt2.place(x=360, y=260)
    b1 = Button(frame3, height=1, width=15, border=0, text="Confirm",bg="#c1e381",fg="white",font=("Microsoft New Tai Lue",15,"italic"),command=remove_values)
    b1.place(x=135, y=340)
    root3.mainloop()
    
             
root = Tk()
root.title("MainMenu")
root.geometry("1100x600")
root.configure(bg="white")
img = PhotoImage(file="assets/modi.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)
img1 = PhotoImage(file="assets/remove.png")
img2 = PhotoImage(file="assets/add.png")
img3 = PhotoImage(file="assets/update.png")
img4 = PhotoImage(file="assets/back.png")
b1 = Button(root,border=0, image = img2,command=add_items)
b1.place(x=135, y=180)
b2 = Button(root,border=0,image = img3, command=update)
b2.place(x=460, y=180)
b3 = Button(root,border=0,image = img1,command=remove)
b3.place(x=800, y=180)
b4 = Button(root, border=0,height=1, width=10, text="Back", bg="pink", fg="black", command=mainmenu)
b4.place(x=525, y=500)
root.mainloop()
