# Open Sesame Server

**Version 1.0.0 – Pre-Beta (Initial working version)**

The **Open Sesame Server** is a Python-based server that allows or denies access to a specific port based on the IP address of the client and the key they provide. The server starts with the port being blocked for all IPs. If a client sends the correct "open" code, their IP is unblocked for the port. If they send the "close" code, their IP is blocked again.

This server uses **pfctl** on **macOS** and **iptables** on **Linux** to dynamically block and unblock specific IPs. It modifies firewall rules to allow access to the server's port based on the provided keys.

## Features

- **Block All IPs**: Initially, the server blocks all incoming traffic to the specified port.
- **Unblock IPs**: When a client sends the correct **"open_sesame"** key, the server unblocks the port for that specific IP.
- **Reblock IPs**: When the client sends the **"close_sesame"** key, the server blocks that IP from accessing the port again.
- **Firewall Management**: Uses **pfctl** (macOS) or **iptables** (Linux) to dynamically manage firewall rules and block/unblock specific IPs.

## Prerequisites

- **macOS** or **Linux** (with `iptables` installed on Linux).
- **Python 3.x** installed.
- **Admin privileges** are required to run the script because it modifies firewall settings using **pfctl** (macOS) or **iptables** (Linux).


## Versions

- **server_simple.py**: A basic version of the server used for testing. It doesn't modify firewall rules and is ideal for quick testing.
- **server_macos.py**: The version of the server for macOS, using **pfctl** to manage firewall rules.
- **server_linux.py**: The version of the server for Linux, using **iptables** to manage firewall rules.
- **client.py**: A client script used for testing the server, sending the "open_sesame" and "close_sesame" keys to control access.

**server_simple.py** and **client.py** are primarily for testing. The other server versions (**server_macos.py** and **server_linux.py**) are self-explanatory and are used for the respective platforms' firewall management.
