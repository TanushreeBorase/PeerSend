import socket

# Initialize Socket Instance
sock = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')

# Send a greeting message to the server
sock.send('A message from the client'.encode())

# Write received file data into a binary file
file = open('client-file.txt', 'wb')

# Receive data from the server in chunks
line = sock.recv(1024)

while line:
    file.write(line)
    line = sock.recv(1024)

print('File has been received successfully.')

file.close()

# Now, let's open and print the content of the received file
with open('client-file.txt', 'r') as file:
    print("File content:")
    print(file.read())  # This prints the file's content to the console

sock.close()
print('Connection Closed.')
