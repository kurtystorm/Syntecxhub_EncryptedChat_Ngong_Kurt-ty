import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5555

clients = []

def log_message(msg):
    with open("chat_log.txt", "a") as f:
        f.write(f"{datetime.now()} {msg}\n")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(4096)
            if not message:
                break

            log_message(message.decode(errors="ignore"))
            broadcast(message, client)

        except:
            breakasa
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()
