from typing import List

def decode_window_sizes_to_command(window_sizes: List[int]) -> str:
    return ''.join(chr(ws - 1000) for ws in window_sizes)

if __name__ == "__main__":
    try:
        raw_input = input("Enter window sizes (comma-separated): ")
        test = [int(x.strip()) for x in raw_input.split(",") if x.strip().isdigit()]

        if not test:
            print("[-] No valid window sizes provided.")
        else:
            decoded = decode_window_sizes_to_command(test)
            print("Decoded (raw):", decoded)
            decoded_ord = [ord(c) for c in decoded]
            print("Decoded (ord):", decoded_ord)

            with open("decoder.py.log", "w") as f:
                f.write(str(decoded_ord) + "\n")

    except Exception as e:
        print(f"[!] Error: {e}")
