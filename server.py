import socket
import threading
from encryption import decrypt, encrypt

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)

clients = []

def broadcast(msg, client_conn):
    """Send message to all clients except the sender"""
    for client in clients:
        if client != client_conn:
            try:
                client.send(msg)
            except:
                pass

def handle_client(conn, addr):
    print(f"[+] New connection from {addr}")
    while True:
        try:
            encrypted_msg = conn.recv(1024).decode()
            if not encrypted_msg:
                break
            decrypted_msg = decrypt(encrypted_msg)
            print(f"Message from {addr}: {decrypted_msg}")
            broadcast(encrypted_msg.encode(), conn)  # Broadcast to other clients
        except:
            break
    print(f"[-] {addr} disconnected")
    clients.remove(conn)
    conn.close()

print("Server is listening for clients...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
