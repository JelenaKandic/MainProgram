import tkinter as tk
import csv
import webbrowser

def load_restaurants():
    with open('restaurant_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

restaurant_data = load_restaurants()

def find_by_mood(mood, max_dist, max_price, min_rating):
    mood = mood.strip().lower()
    matches = []
    price_levels = {'$': 1, '$$': 2, '$$$': 3, '$$$$': 4}

    for r in restaurant_data:
        if mood and mood not in r["Type of Food"].lower():
            continue
        try:
            if max_dist and float(r["Distance from Me (miles)"]) > float(max_dist):
                continue
            if max_price and price_levels.get(r["Price"], 0) > price_levels.get(max_price, 4):
                continue
            if min_rating and float(r["Rating"]) < float(min_rating):
                continue
        except ValueError:
            continue
        matches.append(r)
    return matches

def show_results_window(matches):
    result_win = tk.Toplevel()
    result_win.title("Matching Restaurants")

    tk.Label(result_win, text="Matching Restaurants", font=("Helvetica", 14, "bold")).pack(pady=10)

    if not matches:
        tk.Label(result_win, text="No matches found.", fg="red").pack(pady=10)
        return

    for r in matches:
        name = r["Restaurant Name"]
        url = r.get(" Link") or r.get("Link")
        link_label = tk.Label(result_win, text=name, fg="blue", cursor="hand2", font=("Helvetica", 11, "underline"))
        link_label.pack(anchor="w", padx=20, pady=2)
        if url:
            link_label.bind("<Button-1>", lambda e, link=url: webbrowser.open(link))

def find_restaurants_and_show_result(mood_entry, distance_entry, price_entry, rating_entry):
    matches = find_by_mood(
        mood_entry.get(),
        distance_entry.get(),
        price_entry.get(),
        rating_entry.get()
    )
    show_results_window(matches)
