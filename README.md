# PeerSend

## Usage Instructions:
# Starting the Server:

Run the Python script.
Choose the server mode by entering s.
Enter the port number for the server to listen on.
The server will start listening for incoming connections and will handle file reception automatically.

# Sending a File:

Run the Python script on another computer.
Choose the file-sending mode by entering f.
Enter the server’s IP address and the port number it is listening on.
Specify the path or name of the file you wish to send.
The file transfer will begin, and a confirmation will display upon completion.


+------------------------+                  +-----------------------+
|      Client Side       |                  |      Server Side      |
+------------------------+                  +-----------------------+
| 1. Run script          |                  | 1. Run script         |
| 2. Choose 'f' (send)   |                  | 2. Choose 's' (server)|
| 3. Enter server IP     |                  | 3. Enter port number  |
|    and port number     |                  | 4. Start listening    |
| 4. Enter filename      |                  |    for connections    |
|                        |   Connection     |                       |
|                        |  established     | 5. Accept connection  |
| 5. Send filename       | ---------------> | 6. Receive filename   |
| 6. Send file size      | ---------------> | 7. Receive file size  |
| 7. Send file data      | ---------------> | 8. Write data to file |
|                        |                  | 9. Confirm receipt    |
| 8. Display success     | <--------------- |                       |
+------------------------+                  +-----------------------+

Client Machine: Initiates the file transfer by choosing to send a file, specifying the server's IP and port, and sending the file.
Server Machine: Listens for incoming connections, accepts them, receives file details and data, and saves the file to disk.
Arrows: Show the direction of data flow between the client and server.


