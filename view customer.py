from tkinter import *
from tkinter import messagebox, simpledialog
import PIL
import mysql.connector as nk
import subprocess
from tkinter import ttk

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()


def records():
    q1="select name, username, mail, mobilenumber from regdetails"
    curdb.execute(q1)
    val = curdb.fetchall()
    return val

def add_tree():
    global leng
    data = records()
    for i, row in enumerate(data, start=1):
        tree.insert("","end",values=(i, *row))

def mainmenu(username):
    root.destroy()
    if username == "admin":
        subprocess.run(['python', 'mainmenu.py'])
    else:
        subprocess.run(['python', 'empdashboard.py'])

def get_username():
    username = simpledialog.askstring("Username Input", "Enter your username:", parent=root)
    if not username:
        messagebox.showerror("Error", "No username entered! Please try again.")
        root.destroy()
        return None

    query = f"SELECT username FROM regdetails WHERE username = '{username}'"
    curdb.execute(query)
    user = curdb.fetchone()
    if not user:
        messagebox.showerror("Error", "Username not found! Please try again.")
        root.destroy()
        return None

    return username


root = Tk()
root.title("View Customer list")
root.geometry("925x500")
root.configure(bg="white")
root.resizable(False,False)
img = PhotoImage(file="assets/viewcus.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)

username = get_username()
if not username:
    messagebox.showerror('','Try again!!!')

q2 = "select count(*) from regdetails"
curdb.execute(q2)
leng = curdb.fetchone()[0]
db.commit()
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="WHITE", rowheight=28)
style.configure("Treeview.heading", background="black", foreground="white")
tree = ttk.Treeview(root, columns=("col0","col1","col2","col3","col4"), show="headings", height=9)
tree.column("col0", anchor=CENTER, stretch=NO, width=40)
tree.heading("col0", text="S_No")
tree.column("col1", stretch=NO)
tree.heading("col1", text="Name")
tree.column("col2", anchor=CENTER, stretch=NO)
tree.heading("col2", text="UserName")
tree.column("col3",anchor=CENTER, stretch=NO)
tree.heading("col3", text="User Mail_ID")
tree.column("col4", anchor=CENTER, stretch=NO)
tree.heading("col4", text="Mobile Number")
tree.place(x=50, y=100)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.place(x=880, y=125, height=240)
tree.configure(yscrollcommand=scrollbar.set)
add_tree()

b1 = Button(root, border=0,height=1,bg="pink", fg="black",text="Back", width=10,command=lambda: mainmenu(username))
b1.place(x=420, y=440)
root.mainloop()
