# -*- coding: utf-8 -*-

import socket

image_socket = socket.socket()
host = socket.gethostname() 
port = 1249
image_socket.connect((host, port))

image_socket.send("mostar".encode('utf-8'))

with open('received_image.jpg', 'wb') as f:
    while True:
        data = image_socket.recv(1024,)
        if not data:
            break
        f.write(data)

print("Image received. Filename: received_image.jpg")
image_socket.close()

