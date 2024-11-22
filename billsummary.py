from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image
import subprocess
import mysql.connector as nk

db = nk.connect(host="localhost", user="root", passwd="Narain@2580", database="login")
curdb = db.cursor()

def load_dates():
    curdb.execute("SELECT DISTINCT DATE(time) FROM bill ORDER BY DATE(time)")
    return [row[0].strftime("%Y-%m-%d") for row in curdb.fetchall()]

def add_tree(selected_date):
    tree.delete(*tree.get_children())
    curdb.execute("SELECT bill_number, time, amount FROM bill WHERE DATE(time) = %s", (selected_date,))
    bills = curdb.fetchall()

    total_amount = 0
    for bill in bills:
        tree.insert("", "end", values=bill)
        total_amount += bill[2]
    total_label.config(text=f"Total Amount: Rs {total_amount:.2f}")

def on_date_selected(event):
    selected_date = date_combobox.get()
    if selected_date:
        add_tree(selected_date)

def mainmenu():
    root.destroy()
    subprocess.run(['python','mainmenu.py'])

root = Tk()
root.title("Bill Summary")
root.geometry("1005x600")
root.configure(bg="white")
root.resizable(False,False)
img = PhotoImage(file="assets/login.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)

l1 = Label(root, text="Bill Summary", font=("Helvetica", 18))
l1.place(x=430, y=20)

date_label = Label(root, text="Filter by Date:", font=("Helvetica", 14), fg="black", bg="white")
date_label.place(x=40, y=70)

dates = load_dates()
date_combobox = ttk.Combobox(root, values=dates, font=("Helvetica", 14), width=15)
date_combobox.place(x=180, y=70)
date_combobox.set("Select Date")
date_combobox.bind("<<ComboboxSelected>>", on_date_selected)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="WHITE", rowheight=28)
style.configure("Treeview.heading", background="black", foreground="white")
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=12)
tree.column("col1", anchor="center", stretch=NO, width=100)
tree.heading("col1", text="Bill Number")
tree.column("col2", anchor="center", stretch=NO, width=200)
tree.heading("col2", text="Time")
tree.column("col3", anchor="center", stretch=NO)
tree.heading("col3", text="Amount")
tree.place(x=240, y=120)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=730, y=150, height=300)

total_label = Label(root, text="Total Amount: Rs 0.00", font=("Helvetica", 14), fg="black", bg="white")
total_label.place(x=400, y=500)
ex = Button(root, text="Back", border=0,bg="pink", width=10,command=mainmenu)
ex.place(x=450, y=550)
root.mainloop()

