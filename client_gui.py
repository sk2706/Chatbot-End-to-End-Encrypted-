import socket
import threading
from tkinter import *
from encryption import encrypt, decrypt

client = socket.socket()
client.connect(('localhost', 9999))

# GUI Setup
window = Tk()
window.title("Secure Chat Client")

chat_log = Text(window, bg="black", fg="lightgreen", height=20, width=50)
chat_log.pack(padx=10, pady=5)

entry_box = Entry(window, width=40)
entry_box.pack(side=LEFT, padx=(10, 5), pady=(0, 10))

def send_message():
    msg = entry_box.get()
    if msg:
        encrypted_msg = encrypt(msg)
        client.send(encrypted_msg.encode())
        chat_log.insert(END, f"You: {msg}\n")
        entry_box.delete(0, END)

send_btn = Button(window, text="Send", command=send_message)
send_btn.pack(side=LEFT, padx=(0, 10), pady=(0, 10))

def receive_messages():
    while True:
        try:
            data = client.recv(1024).decode()
            if data:
                decrypted_msg = decrypt(data)
                chat_log.insert(END, f"Friend: {decrypted_msg}\n")
        except:
            break

# Run receiver in a background thread
threading.Thread(target=receive_messages, daemon=True).start()

window.mainloop()
