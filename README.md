# Secure Chat App

A multi-client secure chat application built using Python. This project includes:
- **Server Code (`server.py`):** Accepts connections from multiple clients and broadcasts encrypted messages.
- **Client GUI (`client_gui.py`):** A Tkinter-based chat client that encrypts messages with AES before sending.
- **Client Terminal (`client.py` or `client_terminal.py`):** A command-line version of the chat client.
- **Encryption Module (`encryption.py`):** Implements AES encryption and decryption using pycryptodome.

## Features

- AES-based end-to-end encryption.
- Multi-client support via threading.
- Simple and effective Tkinter GUI.
- Broadcast messages between clients.

## How to Run

1. **Start the Server:**  
   Run `server.py` in a terminal/command prompt with administrator privileges.

2. **Run the Clients:**  
   For a GUI client, run:
   ```bash
   python client_gui.py
