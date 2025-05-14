import sys

KEY = 0x42
def encode_message_to_ttl(message):
    message_bytes = message.encode('ascii')
    encrypted_bytes = bytes([b ^ KEY for b in message_bytes])

    ttl_values = []

    for i in range(len(encrypted_bytes)):
        ttl = (encrypted_bytes[i] & 0xFF) + 64
        ttl_values.append(ttl)

    return ttl_values

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 encode.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    ttl_values = encode_message_to_ttl(message)

    with open("ttl_values.txt", "w") as f:
        for ttl in ttl_values:
            f.write(str(ttl) + "\n")
    
    print(f"[+] Encoded message to TTL values: {len(ttl_values)} TTLs.")

