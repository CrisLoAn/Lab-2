def iso7816_pad(data, block_size):
    pad_bytes = block_size - len(data) % block_size
    padded_data = data + b'\x80' + bytes([0] * (pad_bytes - 1))
    return padded_data
# Example usage
data = b"Hello, world!"
block_size = 16 # AES block size is 128 bits (16 bytes)
padded_data = iso7816_pad(data, block_size)
print("ISO/IEC 7816-4 padded data:", padded_data)