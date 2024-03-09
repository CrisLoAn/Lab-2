from cryptography.hazmat.primitives import padding
def pkcs7_pad(data, block_size):
    padder = padding.PKCS7(block_size * 8).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data
# Example usage
data = b"Hello, world!"
block_size = 16 # AES block size is 128 bits (16 bytes)
padded_data = pkcs7_pad(data, block_size)
print("PKCS#7 padded data:", padded_data)