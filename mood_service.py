import tkinter as tk
#import csv
import webbrowser
import socket
import json
import numpy as np

def show_results_window(matches, username):
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
        tk.Button(result_win, text="Add to favorite", command=lambda: add_favorite(name, username)).pack(pady=5)
        #print("rest name on button:", name)

def show_favorite_window(matches, username):
    result_win = tk.Toplevel()
    result_win.title("Favorite Restaurants")

    tk.Label(result_win, text="Favorite Restaurants", font=("Helvetica", 14, "bold")).pack(pady=10)

    if not matches:
        tk.Label(result_win, text="No matches found.", fg="red").pack(pady=10)
        return

    for r in matches:
        name = r["name"]
        link_label = tk.Label(result_win, text=name, fg="blue", cursor="hand2", font=("Helvetica", 11, "underline"))
        link_label.pack(anchor="w", padx=20, pady=2)
"""
        url = r.get(" Link") or r.get("Link")
        if url:
            link_label.bind("<Button-1>", lambda e, link=url: webbrowser.open(link))
"""

def add_favorite(name, username):
    favorite_socket = socket.socket()
    host = socket.gethostname() 
    port = 1248
    favorite_socket.connect((host, port))

    params = np.array(["A", name, username])
    params_data = json.dumps(params.tolist()).encode()
    favorite_socket.sendall(params_data)
    data = favorite_socket.recv(10240).decode('utf-8')
    print ("Favorite answer: " + data)
    favorite_socket.close()

def show_favorite(username):
    favorite_socket = socket.socket()
    host = socket.gethostname() 
    port = 1248
    favorite_socket.connect((host, port))

    params = np.array(["G", username])
    params_data = json.dumps(params.tolist()).encode()
    favorite_socket.sendall(params_data)
    data = favorite_socket.recv(10240).decode('utf-8')
    print ("Favorite answer: " + data)
    matches = json.loads(data)
    show_favorite_window(matches, username)
    favorite_socket.close()
    
def find_restaurants_and_show_result(mood_entry, distance_entry, price_entry, rating_entry, username):
    restaurant_socket = socket.socket()
    host = socket.gethostname() 
    port = 1247
    restaurant_socket.connect((host, port))

    params = np.array([mood_entry.get(), distance_entry.get(), price_entry.get(), rating_entry.get()])
    params_data = json.dumps(params.tolist()).encode()
    restaurant_socket.sendall(params_data)
    data = restaurant_socket.recv(10240).decode('utf-8')
    print ("Restaurant answer: " + data)
    matches = json.loads(data)
    show_results_window(matches, username)
    restaurant_socket.close()
