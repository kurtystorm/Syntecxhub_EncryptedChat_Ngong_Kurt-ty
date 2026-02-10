import socket
import threading
import base64
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
PORT = 5555

# Pre-shared key (same for all clients)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def receive(sock):
    while True:
        try:
            encrypted = sock.recv(4096)
            if not encrypted:
                break
            decrypted = cipher.decrypt(encrypted)
            print("\nReceived:", decrypted.decode())
        except:
            break

def send(sock):
    while True:
        msg = input()
        encrypted = cipher.encrypt(msg.encode())
        sock.send(encrypted)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    print("Connected to server")

    threading.Thread(target=receive, args=(sock,), daemon=True).start()
    send(sock)

if __name__ == "__main__":
    main()
