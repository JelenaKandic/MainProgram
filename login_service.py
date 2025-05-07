import tkinter as tk
from tkinter import messagebox
import json

def load_users():
    with open('login_users.json', 'r') as f:
        return json.load(f)

users = load_users()

def validate_login(entry_username, entry_password, root):
    from step2_service import show_step2  # moved here to avoid circular import

    username = entry_username.get()
    password = entry_password.get()

    for user in users:
        if user["Username"] == username and user["Password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            show_step2(root, username)
            return

    messagebox.showerror("Login Failed", "Incorrect input. Please try again.")

def start_login():
    root = tk.Tk()
    show_login(root)
    root.mainloop()

def show_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("500x500")
    root.title("Login Page")
    root.configure(bg="green")

    tk.Label(root, text="Username", fg="orange", bg="green").pack(pady=(10, 0))
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password", fg="orange", bg="green").pack(pady=(10, 0))
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Login", command=lambda: validate_login(entry_username, entry_password, root)).pack(pady=20)

    tk.Label(root, text="Don't know what to eat? Let us help!",
             font=("Helvetica", 9, "italic", "bold"), fg="white", bg="green").pack(pady=(5, 10))
