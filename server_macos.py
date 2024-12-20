
import socket
import subprocess

CORRECT_KEY_OPEN = "open_sesame"
CORRECT_KEY_CLOSE = "close_sesame"
PORT = 12345
HOST = "0.0.0.0"

def block_ip(ip):
    """Block an IP from accessing this port using pfctl."""
    try:
        # Create a pf rule to block the IP
        rule = f"block in proto udp from {ip} to any port {PORT}"
        subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "add", ip], check=True)
        subprocess.run(["sudo", "pfctl", "-f", "/etc/pf.conf"], check=True)
        print(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking IP {ip}: {e}")

def unblock_ip(ip):
    """Unblock an IP from accessing this port using pfctl."""
    try:
        # Remove the pf rule blocking the IP
        subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "delete", ip], check=True)
        subprocess.run(["sudo", "pfctl", "-f", "/etc/pf.conf"], check=True)
        print(f"Unblocked IP: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error unblocking IP {ip}: {e}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"Server is listening on {HOST}:{PORT}")

    authorized_ips = set()  # Track IPs authorized for the port

    while True:
        data, addr = server_socket.recvfrom(1024)
        ip, port = addr
        message = data.decode('utf-8')
        print(f"Received message from {addr}: {message}")

        if message == CORRECT_KEY_OPEN:
            if ip in authorized_ips:
                response = "Your IP is already authorized."
            else:
                authorized_ips.add(ip)
                unblock_ip(ip)  # Remove IP from block list
                response = "Your IP has been authorized. You can now access this port."
            print(f"Authorized IPs for this port: {authorized_ips}")
            server_socket.sendto(response.encode('utf-8'), addr)

        elif message == CORRECT_KEY_CLOSE:
            if ip in authorized_ips:
                authorized_ips.remove(ip)
                block_ip(ip)  # Add IP to block list
                response = "Your IP has been de-authorized. You can no longer access this port."
            else:
                response = "Your IP was not authorized."
            print(f"Authorized IPs for this port: {authorized_ips}")
            server_socket.sendto(response.encode('utf-8'), addr)

        elif ip in authorized_ips:
            # Handle normal traffic from authorized IPs
            response = f"Server received your message: {message}"
            server_socket.sendto(response.encode('utf-8'), addr)
        else:
            # Ignore traffic from unauthorized IPs
            print(f"Ignored traffic from unauthorized IP: {ip}")
            response = "Access denied. Your IP is not authorized for this port."
            server_socket.sendto(response.encode('utf-8'), addr)

# Block all traffic to the port initially
def initialize_block_all():
    """Block all incoming traffic to the port by default using pfctl."""
    try:
        # Add a rule to block all incoming UDP traffic to the specific port
        subprocess.run(
            ["sudo", "pfctl", "-t", "blocklist", "-T", "flush"], check=True  # Flush existing rules first
        )
        subprocess.run(
            ["sudo", "pfctl", "-t", "blocklist", "-T", "add", "0.0.0.0"], check=True  # Block all IPs
        )
        subprocess.run(["sudo", "pfctl", "-f", "/etc/pf.conf"], check=True)
        print(f"Port {PORT} is blocked for all IPs by default.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing block on port {PORT}: {e}")

# Start by blocking the port for all traffic
initialize_block_all()
start_server()