from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
import sys


def scan_network(ip_range):
    # Create ARP request
    arp_request = ARP(pdst=ip_range)
    # Create broadcast frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine frame and request
    packet = ether / arp_request

    # Send packet and receive response
    result = srp(packet, timeout=1, verbose=0)[0]

    # Parse response
    clients = []
    for sent, received in result:
        clients.append({"ip": received.psrc, "mac": received.hwsrc})

    return clients

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <ip_range>")
        sys.exit(1)

    ip_range = sys.argv[1]
    clients = scan_network(ip_range)

    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(client["ip"] + "\t\t" + client["mac"])

if __name__ == "__main__":
    main()
