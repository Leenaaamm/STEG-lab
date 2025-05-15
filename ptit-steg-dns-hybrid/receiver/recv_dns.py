import re

cmd_txt = "commands.txt"
log_txt = "log_dns.txt"

bits = []

try:
    with open(log_txt, 'r') as logf:
        for line in logf:
            line = line.strip()
            match = re.search(r'A\?\s+([01])\.ptitlab\.local\.', line)
            if match:
                bits.append(match.group(1))
except FileNotFoundError:
    print(f"[ERROR] Không tìm thấy file log: {log_txt}")
    exit(1)

binary_str = ''.join(bits)

chars = []
for i in range(0, len(binary_str), 8):
    byte = binary_str[i:i+8]
    if len(byte) < 8:
        break
    try:
        chars.append(chr(int(byte, 2)))
    except ValueError:
        continue

command = ''.join(chars)

try:
    with open(cmd_txt, 'w') as f:
        f.write(command + '\n')
        f.write(binary_str + '\n')
except IOError as e:
    print(f"[ERROR] Không ghi được vào '{cmd_txt}': {e}")
    exit(1)

print("Command reconstructed:")
print(command)

