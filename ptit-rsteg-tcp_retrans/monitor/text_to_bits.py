def text_to_bits(text):
    bits = []
    for char in text:
        binval = format(ord(char), '08b')
        bits.extend(list(binval))  
    return bits
if __name__ == "__main__":
    message = "SECRET123"
    bits = text_to_bits(message)
    print(bits)

