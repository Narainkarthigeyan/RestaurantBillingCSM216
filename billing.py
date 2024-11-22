from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image
import subprocess
import mysql.connector as nk
import time
import random

db = nk.connect(host="localhost", user="root", passwd="Narain@2580", database="login")
curdb = db.cursor()

def mainmenu():
    root.destroy()
    subprocess.run(['python','mainmenu.py'])

def cashm():
    messagebox.showinfo('Success', 'Cash payment done!')

def upim():
    messagebox.showinfo('Success', 'UPI payment successful!')

def cardm():
    messagebox.showinfo('Success','Card payment successful!')
    
def update_time():
    cur_time = time.strftime("%H:%M:%S")
    time1.config(text=cur_time)
    time1.after(1000,update_time)

def billno():
    while True:
        billnumber = random.randint(1000, 9999)
        curdb.execute("SELECT bill_number FROM bill WHERE bill_number = {}".format(billnumber))
        if not curdb.fetchone():
            return billnumber

bill_no = billno()

def loadwaiter():
    curdb.execute("select name from employee where role = 'waiter'")
    waiters = [row[0] for row in curdb.fetchall()]
    return waiters

def rec():
    q1="select itemno, itemname,category, price from menu"
    curdb.execute(q1)
    record = curdb.fetchall()
    return record

def add_tree(category_filter=None):
    tree.delete(*tree.get_children())
    if category_filter == "All" or not category_filter:
        val = rec()
    else:
        curdb.execute("SELECT itemno, itemname, category, price FROM menu WHERE category = %s", (category_filter,))
        val = curdb.fetchall()
    
    for row in val:
        tree.insert("", "end", values=row)


def load_categories():
    curdb.execute("SELECT DISTINCT category FROM menu")
    categories = [row[0] for row in curdb.fetchall()]
    return ["All"] + categories

def on_category_selected(event):
    selected_category = category_combobox.get()
    add_tree(selected_category)
        
total_amount = 0

def add_item():
    item_no = entry4.get().strip()
    quan = entry3.get().strip()

    if not item_no.isdigit() or not quan.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid item number and quantity.")
        return

    item_no = int(item_no)
    quan = int(quan)

    curdb.execute("SELECT itemname, price FROM menu WHERE itemno = %s", (item_no,))
    result = curdb.fetchone()

    if result:
        item_name, price = result
        item_total = price * quan
        items_listbox.insert(END, f"{item_name}     (x {quan})    -    Rs {item_total:.2f}")
        global total_amount
        total_amount += item_total
        total.config(text=f"Total: Rs {total_amount:.2f}")
        entry4.delete(0, END)
        entry3.delete(0, END)
    else:
        messagebox.showinfo("Item Not Found", f"The item number '{item_no}' is not in the menu.")

def generate_bill():
    if items_listbox.size() == 0:
        messagebox.showinfo("No Items", "Please add items to generate a bill.")
        return

    global total_amount
    bill_number = bill_no
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    waiter_name = wbox.get()

    try:
        curdb.execute(
            "INSERT INTO bill (time, bill_number, amount) VALUES (%s, %s, %s)",
            (current_time, bill_number, total_amount)
        )
        db.commit()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error saving the bill: {e}")
        return

    bill_window = Toplevel(root)
    bill_window.title("Generated Bill")
    bill_window.geometry("700x500")
    bill_window.configure(bg="white")

    header = Label(bill_window,text="Greenwaves Restaurant",font=("Helvetica", 14, "bold"),bg="white",)
    header.pack(pady=10)

    details = Label(bill_window,text=f"Bill Number: {bill_number}\nTime: {current_time}\nWaiter: {waiter_name}",font=("Helvetica", 10),bg="white",justify=LEFT,)
    details.pack(pady=5)

    bill_text = Text(bill_window, width=80, height=20, font=("Courier New", 10), bg="white", borderwidth=0)
    bill_text.pack(pady=10)

    bill_text.insert(END, f"{'Item':<30}{'Quantity':<10}{'Price':<10}{'Total':<10}\n")
    bill_text.insert(END, "-" * 60 + "\n")

    for item in items_listbox.get(0, END):
        try:
            #item format: "ItemName     (x Quantity)    -    Rs Total"
            item_parts = item.split("    -    ")  # Split by "    -    "
            name_and_quantity = item_parts[0].strip()
            total_price = item_parts[1].strip()  # Extract "Rs Total"

            item_name = name_and_quantity.split("(x")[0].strip()
            quantity = name_and_quantity.split("(x")[1].strip(")")

            item_total = float(total_price.replace("Rs", "").strip())
            price = item_total / int(quantity)  # Calculate each price of item

            bill_text.insert(END, f"{item_name:<30}{quantity:<10}Rs {price:<10.2f}Rs {item_total:<10.2f}\n",)
        except (IndexError, ValueError, TypeError) as e:
            bill_text.insert(END, f"Error processing item: {item}\n")

    bill_text.insert(END, "-" * 60 + "\n")
    bill_text.insert(END, f"{'Total:':<50}Rs {total_amount:.2f}\n")
    bill_text.insert(END, "\n\t\tThank you for visiting!  Hope you enjoyed the food!")
    bill_text.config(state=DISABLED)
    total_amount = 0.0
    total.config(text="Total: Rs 0.00")
    items_listbox.delete(0, END)

    #payment button
    paylab = Label(bill_window, text="PAYMENT METHODS",font=("Helvetica", 10),bg="white")
    paylab.place(x=285, y=400)
    cash = Button(bill_window, text="Cash", border=0, width=10,font=("Helvetica", 10),command=cashm)
    cash.place(x=180, y=450)
    upi = Button(bill_window, text="UPI", border=0, width=10,font=("Helvetica", 10),command=upim)
    upi.place(x=280, y=450)
    card = Button(bill_window, text="Credit / Debit cards", border=0, width=20,font=("Helvetica", 10),command=cardm)
    card.place(x=380, y=450)



root = Tk()
root.title("Billing")
root.attributes("-fullscreen", True)
root.configure(bg="white")
img = PhotoImage(file="assets/bill.png")
pic = Label(root, image=img)
pic.place(x=0, y=0)
b1 = Button(root, border=0, text="X", fg="black", bg="red", width=8, height=2, command=root.destroy)
b1.place(y=2, x=1469)

#time
time1 = Label(root, font=("Helvetica", 25), bg="white", fg="black")
time1.place(x=1380, y=80)
update_time()

#bill number and table number
Bl1 = Label(root, text=f"Bill No: {bill_no}", font=("Helvetica", 18),fg="black", bg="white")
Bl1.place(x=80, y=100)
t1 = Label(root, text="Table Number: ",  font=("Helvetica", 18), fg="black", bg="white")
t1.place(x=290, y=100)
tentry = Entry(root, width=8, fg="black", bg="white", border=0, font=("Microsoft YaHei UI light", 15))
tentry.place(x=480, y=100)
tline1 = Frame(root, height=2, width=90, bg="black")
tline1.place(x=480, y=130)

#waiter name
waiterl = Label(root, text="Waiter: ",  font=("Helvetica", 18), fg="black", bg="white")
waiterl.place(x=650, y=100)
waiters = loadwaiter()
wbox = ttk.Combobox(root, values=waiters, font=("Helvetica", 14), width=12)
wbox.place(x=750, y=100)
wbox.set("Select Waiter")

#add items frame and buttons
itemframe = Frame(root, width=400, height=200, bg="white")
itemframe.place(x=130, y=220)
l1 = Label(root, text="ADD ITEMS",font=("Helvetica", 18), fg="black", bg="white")
l1.place(x=130, y=180)
l3 = Label(itemframe, text="Quantity: ",font=("Helvetica", 18), fg="black", bg="white")
l3.place(x=40, y=80)
entry3 = Entry(itemframe, width=10, fg="black", bg="white", border=0, font=("Microsoft YaHei UI light", 15))
entry3.place(x=190, y=80)
line3 = Frame(itemframe, height=2, width=110, bg="black")
line3.place(x=190, y=110)
l4 = Label(itemframe, text="Item Number: ",font=("Helvetica", 18), fg="black", bg="white")
l4.place(x=40, y=20)
entry4 = Entry(itemframe, width=10, fg="black", bg="white", border=0, font=("Microsoft YaHei UI light", 15))
entry4.place(x=210, y=20)
line4 = Frame(itemframe, height=2, width=120, bg="black")
line4.place(x=210, y=50)
frb1 = Button(itemframe, border=0, width=10, text="Add", font=("Microsoft YaHei UI light", 15),command=add_item)
frb1.place(x=140, y=140)

#added items frame and button
added = Label(root, text="ITEMS ADDED",font=("Helvetica", 18), fg="black", bg="white")
added.place(x=130, y=440)
items_listbox = Listbox(root, font=("Helvetica", 12), width=45, height=10, bg="white")
items_listbox.pack()
items_listbox.place(x=130, y=490)

#total amount
total = Label(root, text="Total: Rs 0.00", font=("Helvetica", 15), fg="black", bg="white")
total.place(x=250, y=700)

#category box
category_label = Label(root, text="Filter by Category:", font=("Helvetica", 14), fg="black", bg="white")
category_label.place(x=750, y=200)
categories = load_categories()
category_combobox = ttk.Combobox(root, values=categories, font=("Helvetica", 14), width=15)
category_combobox.place(x=950, y=200)
category_combobox.set("All")
category_combobox.bind("<<ComboboxSelected>>", on_category_selected)

#tree
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="WHITE", rowheight=28)
style.configure("Treeview.heading", background="black", foreground="white")
tree = ttk.Treeview(root, columns=("col1","col2","col3","col4"), show="headings",height=10)
tree.column("col1",anchor=CENTER,stretch=NO,width=60)
tree.heading("col1",text="Item_No")
tree.heading("col2",text="Item_Name")
tree.column("col3",anchor=CENTER,stretch=NO)
tree.heading("col3",text="Category")
tree.heading("col4", text="Price")
tree.column("col4",anchor=CENTER,stretch=NO)
tree.place(x=750,y=250)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.place(x=1395, y=278, height=280)
tree.configure(yscrollcommand=scrollbar.set)
add_tree()

#generate bill and back
gen = Button(root, text="Generate bill", border=0,bg="#48b74b",width=15, font=("Microsoft YaHei UI light", 15), command=generate_bill)
gen.place(x=850, y=625)
ex = Button(root, text="Back", border=0,bg="red", width=15, font=("Microsoft YaHei UI light", 15),command=mainmenu)
ex.place(x=1090, y=625)
root.mainloop()
