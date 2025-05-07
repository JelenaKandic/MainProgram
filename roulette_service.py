import tkinter as tk
from tkinter import messagebox
import csv
import random

def load_restaurants():
    with open('restaurant_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

restaurant_data = load_restaurants()

def show_roulette_options(root, username):
    from login_service import show_login
    from step2_service import show_step2

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Restaurant Roulette")
    root.configure(bg="lightyellow")

    tk.Label(root, text="🎲 Restaurant Roulette 🎲", font=("Helvetica", 16, "bold"), bg="lightyellow").pack(pady=20)

    def pick_restaurant(source):
        filtered = restaurant_data
        if source == "favorites":
            filtered = [r for r in restaurant_data if r.get("Favorite", "no").lower() == "yes"]
        elif source == "non-favorites":
            filtered = [r for r in restaurant_data if r.get("Favorite", "no").lower() != "yes"]

        if filtered:
            choice = random.choice(filtered)
            messagebox.showinfo("Suggestion", f"Try: {choice['Restaurant Name']}\n\nVisit: {choice.get('Link', 'No link provided')}")
        else:
            messagebox.showwarning("Error", "No matching data available.")

    tk.Button(root, text="Favorites", command=lambda: pick_restaurant("favorites"), width=20).pack(pady=5)
    tk.Button(root, text="Non-Favorites", command=lambda: pick_restaurant("non-favorites"), width=20).pack(pady=5)
    tk.Button(root, text="All Restaurants", command=lambda: pick_restaurant("all"), width=20).pack(pady=5)

    nav_frame = tk.Frame(root, bg="lightyellow")
    nav_frame.pack(pady=20)

    tk.Button(nav_frame, text="Logout", command=lambda: show_login(root), bg="red", fg="black").pack(side="left", padx=10)
    tk.Button(nav_frame, text="Home", command=lambda: show_step2(root, username), bg="green", fg="black").pack(side="left", padx=10)
