import argparse
from src.operations import get_hosts, ping

# Create the parser
parser = argparse.ArgumentParser(description="Send ICMP packets")
parser.add_argument("-dest", type=str, required=True, help="Destination IP address")
parser.add_argument("-cidr", type=int, help="CIDR notation")
parser.add_argument("-n", type=int, help="Number of pings")
parser.add_argument("-t", type=float, help="speed of pings")
args = parser.parse_args()


if __name__ == "__main__":
    count = 4 if args.n is None else args.n
    cidr = 32 if args.cidr is None else args.cidr
    hosts = get_hosts(args.dest, cidr)
    try:
        ping(hosts, count, speed=args.t)
    except KeyboardInterrupt:
        print("Exiting...")