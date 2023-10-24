# server.py
import socket
import threading

def handle_client(client_socket):
    # Функція обробки клієнтських запитів
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print("Отримано від клієнта:", data)
        # Логіка обробки отриманого повідомлення

        # Відправляємо відповідь клієнту
        response = "Відповідь від сервера"
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Сервер готовий приймати з'єднання.")

    while True:
        client_socket, addr = server_socket.accept()
        print("З'єднання встановлено з", addr)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
