# Network Mapper Tool

The Network Mapper Tool is a command-line utility for mapping a network by sending ICMP (Internet Control Message Protocol) packets (pings) to a range of IP addresses. This tool is useful for network troubleshooting, discovering active hosts, and identifying network topology.

## Usage

To use the Network Mapper Tool, follow these steps:

1. Clone the repository:
git clone <repository-url>



2. Install dependencies:
pip install -r requirements.txt

3. Navigate to the directory containing the tool:
cd <repository-directory>

4. Run the tool with the desired options:
python main.py -dest <destination-ip> [-cidr <cidr-notation>] [-n <number-of-pings>] [-t <ping-speed>]


- `-dest <destination-ip>`: Specify the destination IP address.
- `-cidr <cidr-notation>` (optional): Specify the CIDR notation for the subnet. Default is 32.
- `-n <number-of-pings>` (optional): Specify the number of pings to send to each host. Default is 4.
- `-t <ping-speed>` (optional): Specify the speed of pings. 

5. View the results:

The tool will display the results of the network mapping, including the status of each host (reachable or unreachable).

## Example

Here's an example command to map a network:

python main.py -dest 192.168.1.0 -cidr 24 -n 5 -t 0.5


This command maps the network with the destination IP address `192.168.1.0`, using CIDR notation `/24`, sending 5 pings to each host at a speed of 0.5 seconds between pings.
## Notes

- The tool utilizes ICMP packets (pings) to map the network. Therefore, it requires appropriate permissions to send ICMP packets, typically requiring administrative privileges or superuser access.
- It's important to use the tool responsibly and ensure compliance with network policies and regulations.
- For more information on usage and options, refer to the tool's command-line help:

python main.py -h


