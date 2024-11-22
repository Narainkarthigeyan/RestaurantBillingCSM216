from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import mysql.connector as nk

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()

def emp_val():
    name = e1.get()
    age = e2.get()
    mobile = e3.get()
    place = e4.get()
    role = e5.get()
    q1 = "insert into employee values('{}',{},{},'{}','{}')".format(name,age,mobile,place,role)
    curdb.execute(q1)
    db.commit()
    messagebox.showinfo('Success','Employee added successfully')
    root1.destroy()
    
def add_emp():
    global e1,e2,e3,e4,e5, root1
    root1 = Toplevel(root)
    root.title("Add employee")
    root1.geometry("1000x600")
    root1.configure(bg="white")
    img1 = PhotoImage(file="assets/login1.png")
    pic1 = Label(root1, image=img1)
    pic1.place(x=0, y=0)
    frame1 = Frame(root1,bg="white",width=450, height=550)
    frame1.place(x=270, y=25)
    l = Label(frame1, bg="white", fg="#48b74b", text="ADD EMPLOYEE",font=("Microsoft New Tai Lue",20,"italic bold"))
    l.place(x=130, y=20)
    
    e1 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e1.place(x=360, y=130)
    e1.insert(0,"Employee Name")
    l1 = Frame(root1, bg="black", width=269, height=2)
    l1.place(x=360, y=160)

    e2 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e2.place(x=360, y=200)
    e2.insert(0,"Employee Age")
    l2 = Frame(root1, bg="black", width=269, height=2)
    l2.place(x=360, y=230)

    e3 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e3.place(x=360, y=260)
    e3.insert(0,"Mobile Number")
    l3 = Frame(root1, bg="black", width=269, height=2)
    l3.place(x=360, y=290)

    e4 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e4.place(x=360, y=330)
    e4.insert(0,"Place")
    l4 = Frame(root1, bg="black", width=269, height=2)
    l4.place(x=360, y=360)

    e5 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e5.place(x=360, y=400)
    e5.insert(0,"Role")
    l5 = Frame(root1, bg="black", width=269, height=2)
    l5.place(x=360, y=430)
    
    b1 = Button(frame1, text="Confirm",width = 10, border=0, bg="#c1e381",fg="white", font=("Microsoft YaHei UI light", 12), command=emp_val)
    b1.place(x=170, y=450)
    root1.mainloop()

def view_emp():
    root.destroy()
    subprocess.run(['python','view employee.py'])

def mainmenu():
    root.destroy()
    subprocess.run(['python','mainmenu.py'])

root = Tk()
root.title("Employee info")
root.geometry("1000x500")
root.configure(bg="white")
img = PhotoImage(file="assets/waitdp.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)
img1 = PhotoImage(file="assets/addemp.png")
b1 = Button(root, border=0, image=img1, command=add_emp)
b1.place(x=230, y=160)
img2 = PhotoImage(file="assets/empdetails.png")
b2 = Button(root, border=0, image=img2, command=view_emp)
b2.place(x=530, y=160)
b3 = Button(root, height=1, width=10,border=0, text="Back", bg="pink", fg="black", command=mainmenu)
b3.place(x=460, y=440)
root.mainloop()

