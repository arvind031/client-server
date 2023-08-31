import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Client sent: {data}")
        
        response = input("Enter a response to send to the client: ")
        client_socket.send(response.encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Server listening on 127.0.0.1:12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from: {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
