import os

with open("commands.txt") as f:
    cmd = f.readline().strip()

with open("recv_cmd.sh", "w") as s:
    s.write(f"#!/bin/bash\n{cmd}\n")

os.chmod("recv_cmd.sh", 0o755)
print("Script created")
