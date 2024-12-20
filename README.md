# Open Sesame Server

**Version 1.0.0 – Pre-Beta (Initial working version)**

The **Open Sesame Server** is a Python-based server that allows or denies access to a specific port based on the IP address of the client and the key they provide. The server starts with the port being blocked for all IPs. If a client sends the correct "open" code, their IP is unblocked for the port. If they send the "close" code, their IP is blocked again.

This server uses **iptables** (**Linux**) to dynamically block and unblock specific IPs. It modifies firewall rules to allow access to the server's port based on the provided keys.

## Features

- **Block All IPs**: Initially, the server blocks all incoming traffic to the specified port.
- **Unblock IPs**: When a client sends the correct **"open_sesame"** key, the server unblocks the port for that specific IP.
- **Reblock IPs**: When the client sends the **"close_sesame"** key, the server blocks that IP from accessing the port again.
- **Firewall Management**: **iptables** (Linux) to dynamically manage firewall rules and block/unblock specific IPs.

## Prerequisites

- **Linux** (with `iptables` installed on Linux).
- **Python 3.x** installed.
- **Admin privileges** are required to run the script because it modifies firewall settings using **pfctl** (macOS) or **iptables** (Linux).


## Versions

- **server_simple.py**: A basic version of the server used for testing. It doesn't modify firewall rules and is ideal for quick testing.
- **server_linux.py**: The version of the server for Linux, using **iptables** to manage firewall rules.
- **client.py**: A client script used for testing the server, sending the "open_sesame" and "close_sesame" keys to control access.

**server_simple.py** and **client.py** are primarily for testing. The other server versions (**server_macos.py** and **server_linux.py**) are self-explanatory and are used for the respective platforms' firewall management.

## Setup

The Open_Sesame server listens for incoming connections on a specified host and port. 

1. **Select the Host IP**:
   - To restrict the server to a specific network interface, set `HOST` to the IP of that interface:
   - Use `HOST = "0.0.0.0"` to listen on all interfaces (less secure but more flexible). OTHERWISE use the IP address of the interface you would like the code to listen on

2. **Firewall Configuration**:
   - The server dynamically manages access using `iptables` (Linux), blocking the specified port by default.
   - Ensure you have administrative privileges to allow the server to modify firewall rules.

3. **Verify Network Interfaces**:
   - Use `ip addr` (Linux) to check your interface IPs before setting `HOST`.

4. **Response to Attempts**
   - The code defaults to having all responses commented out, making the server effectively 'silent.' This means the server does not respond to any messages from the sender, even if they provide the correct code. Instead, it passively opens the port for authorized IPs without providing any feedback.
  
   
The server ensures secure, dynamic port access control, opening the port only for IPs that send the correct secret key.





