from src.ICMP import ICMP
import socket
import struct


socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
socket.bind(("0.0.0.0", 0))
while True:
    command = input("enter to send")
    packet = ICMP(8, 0)
    socket.sendto(packet.message, ("8.8.8.8", 0))
    data, addr = socket.recvfrom(1024)
    # Extract the ICMP packet
    ip_header = struct.unpack("!BBHHHBBH4s4s", data[:20])
    version_header_length = ip_header[0]
    header_length = (version_header_length & 15) * 4
    icmp_part = data[header_length:]
    # Create icmp packet object using raw bytes from the IP packet recieved
    reply_ICMP_packet = ICMP.parse(icmp_part)
    # Print the ICMP packet
    print(reply_ICMP_packet)
