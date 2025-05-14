from scapy.all import *
import sys

KEY = 0x42

def decode_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    message = b""
    for pkt in packets:
        if IP in pkt and ICMP in pkt and pkt[IP].ttl > 64:
            ttl_value = pkt[IP].ttl
            message += bytes([ttl_value - 64])
    decrypted_message = bytes([b ^ KEY for b in message])
    try:
        return decrypted_message.decode('ascii')
    except UnicodeDecodeError:
        return "Error: Failed to decode message."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./receiver.py <pcap_file>")
        sys.exit(1)
    pcap_file = sys.argv[1]
    decoded_message = decode_pcap(pcap_file)
    with open("decode_msg.txt", "w") as f:
        f.write(decoded_message)
    print(f"[+] Decoded message: {decoded_message}")

