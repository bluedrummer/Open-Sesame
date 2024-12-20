import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("Hello, server!".encode('utf-8'), ('10.10.20.42', 12345))

client_socket.close()