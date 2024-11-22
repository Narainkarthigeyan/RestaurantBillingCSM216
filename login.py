from tkinter import *
from tkinter import messagebox
import PIL
import mysql.connector as nk
import subprocess

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()

def check(username, pw):
    quser = "select * from regdetails where username like '{}'".format(username)
    curdb.execute(quser)
    userr = curdb.fetchone()
    db.commit()
    count=0
    attempts=3
    
    if userr:
        if userr[3] == pw:
            messagebox.showinfo(' ', 'LOGIN SUCCESSFUL')
            root.destroy()
            if username == "admin":
                subprocess.run(['python', 'mainmenu.py'])
            else:
                subprocess.run(['python', 'users.py'])
            
        else:
            messagebox.showerror(' ', 'Wrong Password!')
            count+=1
            val = attempts-count
            messagebox.showinfo(' ', 'You have', val, 'attempts left!!!')
    else:
        messagebox.showerror(' ', 'No username found, Try registering first!')
        
def signin():
    uname1 = user.get()
    pwdc = user2.get()
    check(uname1, pwdc)
    

def reg():
    name=e1.get()
    uname=e2.get()
    mail=e3.get()
    pwd=e4.get()
    pwd1=e5.get()
    mob=e6.get()
    temp = 1
    
    try:
        q1="select username from regdetails where username = %s"
        curdb.execute(q1,(uname,))
        user=curdb.fetchone()
        if user:
            messagebox.showerror(' ','Username already exists! Try again')
    except mysql.connector.IntegrityError as err:
        if err.errno == 1062:
            print("Error: Duplicate entry. The username already exists.")

    if (len(mob) != 10):
        messagebox.showerror(' ', 'Enter a valid mobile number')
        temp = 0

    if(pwd != pwd1):
        messagebox.showerror(' ','Incorrect password input')
        temp = 0
    
    if temp == 1:
        q2="insert into regdetails values('{}', '{}', '{}', '{}','{}',{})".format(name, uname, mail, pwd, pwd1, mob)
        curdb.execute(q2)
        db.commit()
        messagebox.showinfo(' ','SUCCESSFULLY REGISTERED')



def register():
    global e1, e2, e3, e4, e5, e6    
    root1 = Toplevel(root)
    root1.title("Register")
    root1.geometry("924x500")
    root1.configure(bg="white")
    img1 = PhotoImage(file="assets/login1.png")
    pic1 = Label(root1, image=img1)
    pic1.place(x=0, y=0)
    fr1 = Frame(root1, bg="white", width=450, height=450)
    fr1.place(x=250, y=25)
    txt1 = Label(fr1,text="New User Registration", bg="white", fg="#48b74b", font=("Microsoft New Tai Lue",20,"italic bold"))
    txt1.place(x=75, y=10)

    e1 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e1.place(x=340, y=100)
    e1.insert(0,"Name")
    l1 = Frame(root1, bg="black", width=269, height=2)
    l1.place(x=340, y=130)

    e2 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e2.place(x=340, y=150)
    e2.insert(0,"Create Username")
    l2 = Frame(root1, bg="black", width=269, height=2)
    l2.place(x=340, y=180)

    e3 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e3.place(x=340, y=200)
    e3.insert(0,"Enter mail ID")
    l3 = Frame(root1, bg="black", width=269, height=2)
    l3.place(x=340, y=230)

    e4 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15), show="*")
    e4.place(x=340, y=250)
    e4.insert(0,"Create Password")
    l4 = Frame(root1, bg="black", width=269, height=2)
    l4.place(x=340, y=280)

    e5 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15),show="*")
    e5.place(x=340, y=300)
    e5.insert(0,"Confirm Password")
    l5 = Frame(root1, bg="black", width=269, height=2)
    l5.place(x=340, y=330)

    e6 = Entry(root1, bg="white", fg="black",border=0, width=20,font=("Microsoft YaHei UI light", 15))
    e6.place(x=340, y=350)
    e6.insert(0,"Mobile number")
    l6 = Frame(root1, bg="black", width=269, height=2)
    l6.place(x=340, y=380)

    btn = Button(root1, text="Register", border=0, bg="#c1e381",fg="white", font=("Microsoft YaHei UI light", 12), command=reg)
    btn.place(x=450, y=420)
    root1.mainloop()


root = Tk()
root.title("Login")
root.geometry("925x500")
root.configure(bg="white")
root.resizable(False,False)

img = PhotoImage(file="assets/login.png")
pic = Label(root, image=img)
pic.place(x=00, y=0)
frame1 = Frame(root, bg="white", width=350, height=350)
frame1.place(x=60, y=50)
img1 = PhotoImage(file="assets/img.png")
pic1 = Label(root, image=img1)
pic1.place(x=70, y=50)
frame = Frame(root, bg="white", width=350, height=350)
frame.place(x=525, y=50)
h1 = Label(frame,text="Sign in", bg="white", fg="#48b74b", font=("Microsoft New Tai Lue",20,"italic bold"))
h1.place(x=125, y=10)

user = Entry(frame, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI light", 15))
user.place(x=30, y=85)
user.insert(0,"Username")
line = Frame(frame, height=2, width=269, bg="black")
line.place(x=30, y=115)

user2 = Entry(frame, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI light", 15), show="*")
user2.place(x=30, y=150)
user2.insert(0,"Password")
line1 = Frame(frame, height=2, width=269, bg="black")
line1.place(x=30, y=180)

b1 = Button(frame,text="LOGIN",bg="#c1e381", border=0, fg="white", font=("Comic light", 15, "italic"), width=10, height=1, command=signin)
b1.place(x=100, y=240)

l1 = Label(frame, text="New User?", bg="white", fg="black",font=("Microsoft YaHei UI light",10))
l1.place(x=90, y=300)

b2 = Button(frame, text="Register", border=0, fg="#6495ED",bg="white", font=("Microsoft YaHei UI light",10), command=register)
b2.place(x=170, y=298)

root.mainloop()
 
