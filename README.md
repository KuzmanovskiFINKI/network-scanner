# Python Network Scanner

## Overview
This project is a simple network scanner written in Python using the `scapy` library. It scans the local network to detect devices and displays their IP addresses and MAC addresses. The tool sends ARP (Address Resolution Protocol) requests to a specified range of IP addresses and listens for responses to identify active devices.

## Features
- Scans a local network range for active devices.
- Displays IP and MAC addresses of discovered devices.
- Uses the `scapy` library for network packet creation and inspection.
- Simple and easy-to-use command-line interface.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- `scapy` library (install using `pip`)

### Installing `scapy`
To install `scapy`, run the following command:
```bash
pip install scapy
```

## How to Use
1. Clone the repository:
```bash
git clone https://github.com/KuzmanovskiFINKI/network-scanner.git
cd network-scanner
```
2. Run the script with the desired network range:
```bash
python network_scanner.py <IP_range>
```
Replace `<IP_range>` with the desired network range to scan (e.g., `192.168.1.1/24`).

## Example Output
Here is an example output of the network scanner:
```
IP Address         MAC Address
------------------------------------
192.168.1.2        00:1a:2b:3c:4d:5e
192.168.1.10       0a:1b:2c:3d:4e:5f
192.168.1.25       1a:2b:3c:4d:5e:6f
```

