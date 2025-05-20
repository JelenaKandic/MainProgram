# -*- coding: utf-8 -*-

import requests
#import os
from dotenv import load_dotenv
import socket

load_dotenv()

API_KEY = "Hgz2jg17T4TJ3oq5iODoH_ENwVhQj9p3lM6tvzO9LXg" #os.getenv('UNSPLASH_API_KEY')
BASE_URL = "https://api.unsplash.com"
HEADERS = {'Authorization': f'Client-ID {API_KEY}'}
print("key:", API_KEY)

my_socket = socket.socket()
host = socket.gethostname()
my_port = 1249
my_socket.bind((host,my_port))
my_socket.listen()

def search_images(query, num_images=10):
    endpoint = f"{BASE_URL}/search/photos"
    params = {'query': query, 'per_page': num_images}
    response = requests.get(endpoint, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()['results']

def download_image(image_url, filename):
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(8192):
            file.write(chunk)
    print(f"Downloaded: {filename}")

#if __name__ == "__main__":
while True:
    print("start")
    my_connection, addr_main = my_socket.accept()
    print("Connection accepted from " + repr(addr_main[1]))
    
    search_term = my_connection.recv(10240).decode('utf-8')
    print (search_term)
    
    results = search_images(search_term)

    if results:
        for i, image in enumerate(results):
            image_url = image['urls']['regular']
            print("URL:",image_url)
            filename = f"{search_term.replace(' ', '_')}_{i+1}.jpg"
            download_image(image_url, filename)
            with open(filename, 'rb') as f:
                image_data = f.read()
                my_connection.sendall(image_data)
                print("image sent")
                my_connection.close()
            break
    else:
        print("ERROR: No images found for the given query.")
    
