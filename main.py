# main.py
import threading
from server import start_server
from client import start_client

server_thread = threading.Thread(target=start_server)
server_thread.start()

start_client()
