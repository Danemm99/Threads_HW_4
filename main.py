# main.py
import threading
from server import start_server
from client import start_client

# Запускаємо сервер у окремому потоці
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Запускаємо клієнта
start_client()
