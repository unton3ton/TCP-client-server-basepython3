import socket
import os

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server address
server_address = ('192.168.100.90', 8888)
sock.connect(server_address)

# open the image file and read the data
with open('image.jpg', 'rb') as f:
    # get the size of the image
    image_size = os.path.getsize('image.jpg')
    # send the size of the image first
    sock.sendall(image_size.to_bytes(8, byteorder='big'))
    
    # send the image data in chunks
    while True:
        chunk = f.read(1024)  # read in 1KB chunks
        if not chunk:
            break
        sock.sendall(chunk)

# close the socket
sock.close()
