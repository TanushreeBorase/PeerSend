import socket
import threading
import os

# Function to handle incoming connections and receive files
def handle_client(client_socket):
    filename = client_socket.recv(1024).decode()
    filesize = int(client_socket.recv(1024).decode())
    print(f"Receiving {filename} of size {filesize} bytes")

    with open(filename, 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)

    print(f"{filename} received successfully")
    client_socket.close()

# Function to start the server
def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[*] Listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Function to send a file to a peer
def send_file(ip, port, filename):
    filesize = os.path.getsize(filename)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    sock.send(os.path.basename(filename).encode())
    sock.send(str(filesize).encode())

    with open(filename, 'rb') as f:
        bytes_sent = 0
        while bytes_sent < filesize:
            data = f.read(1024)
            sock.send(data)
            bytes_sent += len(data)

    print(f"{filename} sent successfully")
    sock.close()

# Main function
if _name_ == "_main_":
    choice = input("Start server (s) or send file (f)? ")
    if choice == 's':
        port = int(input("Enter port number: "))
        start_server(port)
    elif choice == 'f':
        ip = input("Enter peer IP address: ")
        port = int(input("Enter peer port number: "))
        filename = input("Enter filename to send: ")
        send_file(ip, port, filename)
