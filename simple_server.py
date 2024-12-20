import socket

CORRECT_KEY = "open_sesame"
PORT = 12345
HOST = "0.0.0.0"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"Server is listening on {HOST}:{PORT}")

    open_mode = False

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode('utf-8')}")

        if not open_mode:
            if data.decode('utf-8') == CORRECT_KEY:
                print("Correct key received, server is now 'open'!")
                open_mode = True
                response = "Access granted! Server is now open." #Line could be removed later on
                server_socket.sendto(response.encode('utf-8'), addr)
            else:
                print("Incorrect key received, ignoring.")
#        else:
 #           response = f"Server received your message: {data.decode('utf-8')}"
 #           server_socket.sendto(response.encode('utf-8'), addr)

start_server()



