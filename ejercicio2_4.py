def ansix923_pad(data, block_size):
    last_byte = data[-1]
    pad_bytes = block_size - len(data) % block_size
    padded_data = data + bytes([pad_bytes - 1] * pad_bytes)
    return padded_data
# Example usage
data = b"Hello, world!"
block_size = 16 # AES block size is 128 bits (16 bytes)
padded_data = ansix923_pad(data, block_size)
print("ANSI X.923 padded data:", padded_data)