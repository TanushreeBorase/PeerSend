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

Architecture:

![image](https://github.com/user-attachments/assets/6d546dde-fe73-48db-bc1c-612c71508122)


Client Machine: Initiates the file transfer by choosing to send a file, specifying the server's IP and port, and sending the file.

Server Machine: Listens for incoming connections, accepts them, receives file details and data, and saves the file to disk.

Arrows: Show the direction of data flow between the client and server.


To access and run your file transfer project, follow these step-by-step instructions:

### 1. **Setting Up the Server**:
   - **Open a Terminal/Command Prompt** on the machine you want to act as the server.
   - **Navigate to the Project Directory** using `cd path/to/your/project`.
   - **Run the Python Script**:
     ```bash
     python server.py
      python client.py
     ```
   - **Choose to Start as Server**:
     - When prompted, type `s` and press **Enter**.
     - Enter a port number (e.g., `12345`) and press **Enter**.
   - The server will start listening for incoming connections.

### 2. **Sending a File from the Client**:
   - **Open a Terminal/Command Prompt** on the machine you want to act as the client.
   - **Navigate to the Project Directory** using `cd path/to/your/project`.
   - **Run the Python Script**:
     ```bash
     python server.py
     ```
   - **Choose to Send a File**:
     - When prompted, type `f` and press **Enter**.
   - **Enter Server Details**:
     - Input the server's **IP address** and the **port number** (e.g., `192.168.1.5`, `12345`).
   - **Enter the Filename**:
     - Provide the full path or name of the file you wish to send and press **Enter**.
   - The client will start the transfer, and both machines will display success messages upon completion.

### **Visual Access Guide**:
- **Server**:
  - Terminal display will show `[*] Listening on port 12345`.
  - When a connection is accepted, it will display `[*] Accepted connection from (IP Address, Port)` and the progress of the file transfer.
- **Client**:
  - Terminal prompts the user to enter the server's IP, port, and file path.
  - Displays `filename sent successfully` when the transfer completes.


