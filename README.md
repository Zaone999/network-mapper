# Network Mapper Tool

The Network Mapper Tool is a command-line utility for mapping a network by sending ICMP (Internet Control Message Protocol) packets (pings) to a range of IP addresses. This tool is useful for network troubleshooting, discovering active hosts, and identifying network topology.

---

## Usage

To use the Network Mapper Tool, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the directory containing the tool:**
   ```sh
   cd <repository-directory>
   ```

3. **Run the tool with the desired options:**
   ```sh
   python main.py -dest <destination-ip> [-cidr <cidr-notation>] [-n <number-of-pings>] [-t <ping-speed>]
   ```

   - `-dest <destination-ip>`: Specify the destination IP address.
   - `-cidr <cidr-notation>` (optional): Specify the CIDR notation for the subnet. Default is 32.
   - `-n <number-of-pings>` (optional): Specify the number of pings to send to each host. Default is 4.
   - `-t <ping-speed>` (optional): Specify the speed of pings. 

5. **View the results:**

   The tool will display the results of the network mapping, including the status of each host (reachable or unreachable).

---

## Example

Here's an example command to map a network:

```sh
python main.py -dest 192.168.1.0 -cidr 24 -n 5 -t 0.5
```

This command maps the network with the destination IP address `192.168.1.0`, using CIDR notation `/24`, sending 5 pings to each host at a speed of 0.5 seconds between pings.

---

## Learning Outcomes

By working on this project, I've gained knowledge and experience in the following areas:

- Understanding how things operate at the IP layer.
- Learning about the components of ICMP packets and their purposes.
- Exploring the `struct` module in Python for handling binary data.
- Understanding the socket layer at the kernel level and its interaction with Python.

---

## Limitations

While this tool provides a basic ICMP implementation for network mapping, it's important to note that it may not be as powerful or complete as libraries like Scapy. The objective of this project was to understand how protocols operate at the byte level, including interpreting headers and their sizes.

---

## Notes

- The tool utilizes ICMP packets (pings) to map the network. Therefore, it requires appropriate permissions to send ICMP packets, typically requiring administrative privileges or superuser access.
- It's important to use the tool responsibly and ensure compliance with network policies and regulations.
- For more information on usage and options, refer to the tool's command-line help:
  ```sh
  python main.py -h
  ```

---
