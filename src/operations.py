import struct
import socket
import ipaddress
from src.ICMP import ICMP

def _extract_icmp_packet_bytes(data):
    ip_header = struct.unpack("!BBHHHBBH4s4s", data[:20])
    version_header_length = ip_header[0]
    header_length = (version_header_length & 15) * 4
    icmp_part = data[header_length:]
    return icmp_part

def get_hosts(ip, cidr):
    address = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    return [str(host) for host in address.hosts()]

def ping(hosts, count, speed=1.0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.bind(("0.0.0.0", 0))
    sock.settimeout(speed)
    for host in hosts:
        for i in range(count):
            icmp = ICMP(seq_num=i)
            sock.sendto(icmp.message, (host, 0))
            try:
                data, addr = sock.recvfrom(1024)
                reply_packet = ICMP.parse_bytes(_extract_icmp_packet_bytes(data))
                if reply_packet.type == 0:
                    print(f"{host} is up")
                    break
            except socket.timeout:
                break
