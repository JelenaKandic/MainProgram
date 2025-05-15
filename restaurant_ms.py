# -*- coding: utf-8 -*-
"""
Created on Sun May 11 09:29:08 2025

@author: Jelena Kandic
"""

import socket
import csv
import json
import numpy as np

def load_restaurants():
    with open('restaurant_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

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

my_socket = socket.socket()
host = socket.gethostname()
my_port = 1247
my_socket.bind((host,my_port))
my_socket.listen()

restaurant_data = load_restaurants()

while True:
    print("start")
    my_connection, addr_main = my_socket.accept()
    print("Connection accepted from " + repr(addr_main[1]))
    
    command = my_connection.recv(10240).decode('utf-8')
    print (command)
    deserialized_array = np.array(json.loads(command))
    
    #print("First element:", deserialized_array[0])

    matches = find_by_mood(
        deserialized_array[0],
        deserialized_array[1],
        deserialized_array[2],
        deserialized_array[3]
    )
    
    #print("matches:", json.dumps(matches))
    
    data = json.dumps(matches).encode()

    my_connection.sendall(data)
    print ("the message has been sent")
   
          