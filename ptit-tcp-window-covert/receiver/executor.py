import subprocess

def execute_command(command: str) -> str:
    """
    Thực thi lệnh shell và trả kết quả (stdout + stderr)
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout + result.stderr
        return output
    except subprocess.TimeoutExpired:
        return "[!] Command timed out."
    except Exception as e:
        return f"[!] Execution error: {e}"

if __name__ == "__main__":
    cmd = input("Enter command to execute: ")
    output = execute_command(cmd)
    print(output)
    with open("executor.py.log", "w") as f:
        f.write(output)
