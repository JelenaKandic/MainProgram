This document outlines how to programmatically request and receive image data from the image microservice implemented in unsplash_image_search_ms.py. 
This service communicates over a TCP socket connection and returns the binary image data for a single image result based on a search term.

OVERVIEW:
Protocol: TCP socket

Host: gethostname() on the server machine (usually localhost if testing locally)

Port: 1249

Input: UTF-8 encoded search term (e.g., "mostar")

Output: Raw JPEG image bytes (a single .jpg image file)

HOW TO REQUEST DATA:
To request an image, open a TCP socket to the server and send a UTF-8 encoded string representing your image search keyword.
EX CODE-
import socket

# Set up the socket
s = socket.socket()
host = 'localhost'  # Replace with actual server IP if remote
port = 1249
s.connect((host, port))

# Send search term
search_term = "mountains"
s.send(search_term.encode('utf-8'))


HOW TO RECIEVE DATA:
After sending the search term, the server will respond with binary image data (JPEG format). 
Read from the socket in chunks until no data is left, and write the data to a .jpg file.
OUTPUT-
A new file received_image.jpg containing the downloaded image.
EX CODE:
with open('received_image.jpg', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

s.close()
