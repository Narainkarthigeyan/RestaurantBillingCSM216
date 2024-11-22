from tkinter import *
from tkinter import messagebox
import PIL
import mysql.connector as nk
import subprocess
from tkinter import ttk

db=nk.connect(host="localhost",user="root",passwd="Narain@2580",database="login")
curdb = db.cursor()

def rec():
    q1="select * from employee"
    curdb.execute(q1)
    record = curdb.fetchall()
    return record

def add_tree():
    global leng, val
    val = rec()
    for i,row in enumerate(val, start=1):
        tree.insert("","end",values=(i, *row))
    
def emp():
    root.destroy()
    subprocess.run(['python','employee.py'])
    
root = Tk()
root.title("View Employee")
root.geometry("925x500")
root.configure(bg="white")
root.resizable(False,False)
img = PhotoImage(file="assets/emp.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)

frame_container = Frame(root, padx=10, pady=10, bg='#badc58')
frame_fields = Frame(frame_container, bg='#badc58')

q2 = "select count(*) from employee"
curdb.execute(q2)
leng = curdb.fetchone()[0]
db.commit()

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="WHITE", rowheight=28)
style.configure("Treeview.heading", background="black", foreground="white")
tree = ttk.Treeview(root, columns=("col1","col2","col3","col4","col5","col6"), show="headings",height=10)
tree.column("col1",anchor=CENTER,stretch=NO,width=40)
tree.heading("col1",text="S_No")
tree.heading("col2",text="Employee Name")
tree.column("col3",anchor=CENTER,stretch=NO, width=60)
tree.heading("col3",text="Age")
tree.column("col4",anchor=CENTER,stretch=NO,width=150)
tree.heading("col4",text="Mobile Number")
tree.column("col5",anchor=CENTER,stretch=NO)
tree.heading("col5",text="Place")
tree.column("col6",anchor=CENTER,stretch=NO, width=150)
tree.heading("col6",text="Role")
tree.place(x=60,y=95)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.place(x=845, y=120, height=280)
tree.configure(yscrollcommand=scrollbar.set)
add_tree()

b1 = Button(root, border=0,bg="pink", fg="black",text="Back",height=1, width=10,command=emp)
b1.place(x=400, y=450)
root.mainloop()



