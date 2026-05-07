import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector



connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ikb12345"
)

cursor = connection.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS StudentDatabase")
cursor.execute("USE StudentDatabase")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Score INT
)
""")

connection.commit()



def add_student():
    name = name_entry.get()
    score = score_entry.get()

    if name == "" or score == "":
        messagebox.showwarning("Warning", "Please enter name and score")
        return

    if not score.isdigit():
        messagebox.showwarning("Warning", "Score must be a number")
        return

    score = int(score)

    if score < 1 or score > 100:
        messagebox.showwarning("Warning", "Score must be between 1 and 100")
        return

    cursor.execute("INSERT INTO Students (Name, Score) VALUES (%s, %s)", (name, score))
    connection.commit()

    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

    show_students()



def show_students():
    for row in table.get_children():
        table.delete(row)

    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()

    for record in records:
        table.insert("", tk.END, values=record)



def filter_students():
    score = filter_entry.get()

    if score == "":
        messagebox.showwarning("Warning", "Please enter a score")
        return

    if not score.isdigit():
        messagebox.showwarning("Warning", "Score must be a number")
        return

    score = int(score)

    for row in table.get_children():
        table.delete(row)

    cursor.execute("SELECT * FROM Students WHERE Score > %s", (score,))
    records = cursor.fetchall()

    for record in records:
        table.insert("", tk.END, values=record)



window = tk.Tk()
window.title("Student Database GUI")
window.geometry("600x450")

title_label = tk.Label(window, text="Student Database", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

tk.Label(window, text="Student Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)


tk.Label(window, text="Student Score:").pack()
score_entry = tk.Entry(window)
score_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Student", command=add_student)
add_button.pack(pady=10)


tk.Label(window, text="Show students with score higher than:").pack()
filter_entry = tk.Entry(window)
filter_entry.pack(pady=5)

filter_button = tk.Button(window, text="Filter Students", command=filter_students)
filter_button.pack(pady=10)

show_all_button = tk.Button(window, text="Show All Students", command=show_students)
show_all_button.pack(pady=5)


table = ttk.Treeview(window, columns=("ID", "Name", "Score"), show="headings")
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Score", text="Score")

table.pack(pady=15, fill="both", expand=True)

show_students()

window.mainloop()