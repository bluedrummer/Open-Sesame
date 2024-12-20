# Open Sesame Server

The **Open Sesame Server** is a Python-based server that allows or denies access to a specific UDP port based on the IP address of the client and the key they provide. The server starts with the port being blocked for all IPs. If a client sends the correct "open" code, their IP is unblocked for the port. If they send the "close" code, their IP is blocked again.

This server uses **pfctl** on **macOS** and **iptables** on **Linux** to dynamically block and unblock specific IPs. It modifies firewall rules to allow access to the server's port based on the provided keys.

## Features

- **Block All IPs**: Initially, the server blocks all incoming UDP traffic to the specified port.
- **Unblock IPs**: When a client sends the correct **"open_sesame"** key, the server unblocks the port for that specific IP.
- **Reblock IPs**: When the client sends the **"close_sesame"** key, the server blocks that IP from accessing the port again.
- **Firewall Management**: Uses **pfctl** (macOS) or **iptables** (Linux) to dynamically manage firewall rules and block/unblock specific IPs.

## Prerequisites

- **macOS** or **Linux** (with `iptables` installed on Linux).
- **Python 3.x** installed.
- **Admin privileges** are required to run the script because it modifies firewall settings using **pfctl** (macOS) or **iptables** (Linux).
