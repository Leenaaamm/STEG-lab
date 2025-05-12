import socket

HOST = "0.0.0.0"
PORT = 12345

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print("[*] Receiver ready, waiting for sender...")
        conn, addr = sock.accept()
        print(f"[*] Connected by {addr}")
    except Exception as e:
        print(f"[!] Server error: {e}")
        return

    seen_payloads = set()
    hidden_bits = []

    while True:
        data = conn.recv(1024)
        if not data:
            break
        decoded = data.decode('utf-8', errors='ignore')
        payload = decoded.strip()

        if payload in seen_payloads:
            bit = payload.split('_')[0]
            hidden_bits.append(bit)
            print(f"[*] Retransmitted packet detected, bit={bit}")
        else:
            seen_payloads.add(payload)
            print(f"[!] First-time packet (ignored for hidden bit): {payload}")

    message = ""
    for i in range(0, len(hidden_bits), 8):
        byte = hidden_bits[i:i+8]
        if len(byte) < 8:
            break
        message += chr(int("".join(byte), 2))

    with open("hidden_message.txt", "w", encoding="utf-8") as f:
        f.write(message)

    print(f"[+] Hidden message extracted: {message}")
    conn.close()

if __name__ == "__main__":
    start_server()

