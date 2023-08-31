import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(f"Server sent: {data}")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter a message to send to the server: ")
        client_socket.send(message.encode())
        
        if message.lower() == "exit":
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
