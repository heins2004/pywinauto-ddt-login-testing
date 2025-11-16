import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Fake authentication logic (matches your DDT examples)
    if username == "admin" and password == "12345":
        result_label.config(text="Success")
    elif username == "user1" and password == "wrong":
        result_label.config(text="Fail")
    else:
        result_label.config(text="Invalid Credentials")

app = tk.Tk()
app.title("Login")
app.geometry("300x200")

tk.Label(app, text="Username").pack()
username_entry = tk.Entry(app)
username_entry.pack()

tk.Label(app, text="Password").pack()
password_entry = tk.Entry(app, show="*")
password_entry.pack()

login_btn = tk.Button(app, text="Login", command=login)
login_btn.pack(pady=10)

result_label = tk.Label(app, text="", fg="blue")
result_label.pack()

app.mainloop()
