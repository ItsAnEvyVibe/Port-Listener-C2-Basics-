# -------------------------------------------------------------------------
# Project: Port-Listener-C2-Basics
# Author: Krystel E Albertson
# Date: February 2026
# Business: Lock it Down Solutions
# -------------------------------------------------------------------------

import socket

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4444))
    server.listen(1)
    print("[*] Listening on port 4444...")
    
    client_socket, address = server.accept()
    print(f"[*] Accepted connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")

start_listener()
