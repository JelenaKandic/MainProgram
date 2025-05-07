import tkinter as tk
from mood_service import find_restaurants_and_show_result

def show_step2(root, username):
    from roulette_service import show_roulette_options  # move import here to avoid circular import

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="green")
    root.title("Step 2")

    tk.Label(root, text=f"Welcome {username}!", font=("Helvetica", 12, "bold"), bg="green").pack(pady=(10, 5))
    tk.Label(root, text="Please choose 1 or 2", font=("Helvetica", 10), bg="green").pack(pady=(0, 10))

    # Mood-based
    tk.Label(root, text="1.) What are you in the mood for?", font=("Helvetica", 10), bg="green").pack()
    mood_entry = tk.Entry(root, width=30)
    mood_entry.pack()

    tk.Label(root, text="Max Distance (miles):", bg="green").pack()
    distance_entry = tk.Entry(root, width=30)
    distance_entry.pack()

    tk.Label(root, text="Max Price ($ to $$$$):", bg="green").pack()
    price_entry = tk.Entry(root, width=30)
    price_entry.pack()

    tk.Label(root, text="Min Rating (e.g. 7):", bg="green").pack()
    rating_entry = tk.Entry(root, width=30)
    rating_entry.pack(pady=(0, 10))

    result_text = tk.StringVar()

    tk.Button(root, text="Find Restaurants", command=lambda: find_restaurants_and_show_result(
        mood_entry, distance_entry, price_entry, rating_entry)).pack(pady=5)

    tk.Label(root, textvariable=result_text, wraplength=350, bg="green").pack(pady=10)

    # Roulette option
    frame2 = tk.Frame(root, bg="green")
    frame2.pack(pady=5)

    tk.Button(frame2, text="Go", width=6, command=lambda: show_roulette_options(root, username)).pack(side="left", padx=(0, 10))
    tk.Label(frame2, text="2.) Restaurant Roulette", font=("Helvetica", 10), bg="green").pack(side="left")

    tk.Button(root, text="Logout", command=root.destroy, bg="red", fg="black").pack(pady=20)
