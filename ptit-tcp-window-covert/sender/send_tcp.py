from scapy.all import IP, TCP, send
from encoder import encode_command_to_window_sizes
import time
import os

RECEIVER_IP = "178.10.0.2"
RECEIVER_PORT = 12345
SRC_PORT = 54321
LOG_FILE = "send_tcp.py.log"

def send_command(command: str):
    """
    Gửi từng ký tự mã hóa qua gói TCP với Window Size đặc biệt.
    """
    # Xóa log cũ nếu có
    open(LOG_FILE, "w").close()

    window_sizes = encode_command_to_window_sizes(command)
    print(f"[+] Sending command: {command}")

    for index, ws in enumerate(window_sizes):
        pkt = IP(dst=RECEIVER_IP)/TCP(sport=SRC_PORT, dport=RECEIVER_PORT, flags="S", window=ws)
        send(pkt, verbose=False)

        log_line = f"  [-] Sent byte {index+1}/{len(window_sizes)}: window={ws}"
        print(log_line)

        with open(LOG_FILE, "a") as f:
            f.write(log_line + "\n")

        time.sleep(0.2)

    print("[+] Done sending command.")

if __name__ == "__main__":
    try:
        user_input = input("Enter command to send: ").strip()
        if user_input:
            send_command(user_input)
        else:
            print("[-] Empty command. Aborting.")
    except KeyboardInterrupt:
        print("\n[-] Interrupted by user.")
