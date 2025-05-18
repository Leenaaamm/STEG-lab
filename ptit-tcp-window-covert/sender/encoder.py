from typing import List

def encode_command_to_window_sizes(command: str) -> List[int]:
    return [ord(c) + 1000 for c in command]

def decode_window_sizes_to_command(window_sizes: List[int]) -> str:
    return ''.join(chr(ws - 1000) for ws in window_sizes)

if __name__ == "__main__":
    command = input("Nhập thông điệp cần mã hóa: ")
    print(command)
    window_sizes = encode_command_to_window_sizes(command)
    print(f"\nThông điệp gốc: {command}")
    print(f"Mã hóa (window sizes): {window_sizes}")
    print(f"Giải mã lại: {decode_window_sizes_to_command(window_sizes)}")

    # Thêm dòng ghi ra file
    with open("encode_output.txt", "w") as f:
        f.write(str(window_sizes))
