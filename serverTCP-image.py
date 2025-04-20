import socket
import threading

def handle_client(connection):
    try:
        # receive the size of the image first
        image_size_bytes = connection.recv(8)
        image_size = int.from_bytes(image_size_bytes, byteorder='big')

        # write the image data to a file
        with open('image_received.jpg', 'wb') as f:
            bytes_received = 0
            while bytes_received < image_size:
                chunk = connection.recv(1024)  # read in 1KB chunks
                if not chunk:
                    break
                f.write(chunk)
                bytes_received += len(chunk)

        print("Image received successfully.")

    finally:
        # close the connection
        connection.close()

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('0.0.0.0', 8888)
sock.bind(server_address)

# listen for incoming connections
sock.listen(5)  # максимальное количество ожидающих подключений

print('Server is running and waiting for connections...')

while True:
    # wait for a connection
    connection, client_address = sock.accept()
    print(f'Connection from {client_address} has been established.')

    # create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connection,))
    client_thread.start()
