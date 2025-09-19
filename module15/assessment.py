import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# ---------------- Database Setup ----------------
conn = sqlite3.connect("repairmate.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    device TEXT,
    issue TEXT,
    status TEXT,
    cost REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")
conn.commit()

# ---------------- Classes ----------------
class Customer:
    def _init_(self, name, phone):
        self.name = name
        self.phone = phone
    
    def save(self):
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?,?)",
                       (self.name, self.phone))
        conn.commit()

class Repair:
    def _init_(self, customer_id, device, issue, cost=0, status="Pending"):
        self.customer_id = customer_id
        self.device = device
        self.issue = issue
        self.cost = cost
        self.status = status
    
    def save(self):
        cursor.execute("INSERT INTO repairs (customer_id, device, issue, status, cost) VALUES (?,?,?,?,?)",
                       (self.customer_id, self.device, self.issue, self.status, self.cost))
        conn.commit()

# ---------------- GUI Functions ----------------
def add_customer():
    try:
        name = entry_name.get()
        phone = entry_phone.get()
        if not name or not phone:
            raise ValueError("All fields required")
        c = Customer(name, phone)
        c.save()
        messagebox.showinfo("Success", "Customer added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_repair():
    try:
        cust_id = int(entry_cust_id.get())
        device = entry_device.get()
        issue = entry_issue.get()
        cost = float(entry_cost.get())
        r = Repair(cust_id, device, issue, cost)
        r.save()
        messagebox.showinfo("Success", "Repair added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_repairs():
    pattern = entry_search.get()
    cursor.execute("SELECT * FROM repairs")
    results = cursor.fetchall()
    output.delete(1.0, tk.END)
    for r in results:
        if re.search(pattern, str(r), re.IGNORECASE):
            output.insert(tk.END, f"{r}\n")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("RepairMate - Simple Version")

# Customer Frame
frame1 = tk.LabelFrame(root, text="Add Customer")
frame1.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame1, text="Name").grid(row=0, column=0)
tk.Label(frame1, text="Phone").grid(row=1, column=0)

entry_name = tk.Entry(frame1)
entry_phone = tk.Entry(frame1)
entry_name.grid(row=0, column=1)
entry_phone.grid(row=1, column=1)

tk.Button(frame1, text="Add Customer", command=add_customer).grid(row=2, column=0, columnspan=2)

# Repair Frame
frame2 = tk.LabelFrame(root, text="Add Repair")
frame2.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame2, text="Customer ID").grid(row=0, column=0)
tk.Label(frame2, text="Device").grid(row=1, column=0)
tk.Label(frame2, text="Issue").grid(row=2, column=0)
tk.Label(frame2, text="Cost").grid(row=3, column=0)

entry_cust_id = tk.Entry(frame2)
entry_device = tk.Entry(frame2)
entry_issue = tk.Entry(frame2)
entry_cost = tk.Entry(frame2)

entry_cust_id.grid(row=0, column=1)
entry_device.grid(row=1, column=1)
entry_issue.grid(row=2, column=1)
entry_cost.grid(row=3, column=1)

tk.Button(frame2, text="Add Repair", command=add_repair).grid(row=4, column=0, columnspan=2)

# Search Frame
frame3 = tk.LabelFrame(root, text="Search Repairs (Regex)")
frame3.pack(fill="both", expand="yes", padx=10, pady=5)

entry_search = tk.Entry(frame3, width=30)
entry_search.pack(side="left")
tk.Button(frame3, text="Search", command=search_repairs).pack(side="left")

output = tk.Text(frame3, height=10)
output.pack(fill="both", expand="yes")

root.mainloop()