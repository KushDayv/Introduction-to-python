import scapy.all as scapy
import socket

def scan(ip):
    # Create an ARP request packet to get MAC addresses for IP addresses
    arp_request = scapy.ARP(pdst=ip)
    
    # Create an Ethernet frame to send the ARP request
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

    # Combine the Ethernet frame and ARP request
    arp_request_packet = ether / arp_request

    # Send the packet and receive responses
    answered = scapy.srp(arp_request_packet, timeout=1, verbose=False)[0]

    # Create a list of dictionaries to store IP and MAC addresses
    devices_list = []
    
    # Iterate through the responses and extract IP and MAC addresses
    for element in answered:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)

    return devices_list

def check_online(ip, port=80):
    try:
        socket.setdefaulttimeout(5)  # Adjust the timeout as needed
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def main():
    target_ip_range = input("Enter the target IP range (e.g., 192.168.1.1/24): ")
    scanned_devices = scan(target_ip_range)

    print("Connected devices:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in scanned_devices:
        ip_address = device["ip"]
        mac_address = device["mac"]
        if check_online(ip_address):
            print(f"{ip_address}\t\t{mac_address}")

if __name__ == "__main__":
    main()
