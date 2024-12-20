import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("Hello, server!".encode('utf-8'), ('0.0.0.0', 12345))

client_socket.close()