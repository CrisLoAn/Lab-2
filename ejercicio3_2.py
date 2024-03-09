from Crypto.Cipher import DES
import base64
# Padding schemes
def pkcs7_pad(data, block_size):
    padding_size = block_size - len(data) % block_size
    padding = bytes([padding_size] * padding_size)
    return data + padding

def zero_pad(data, block_size):
    padding_size = block_size - len(data) % block_size
    padding = b'\x00' * padding_size
    return data + padding

# DES encryption function with padding
def des_encrypt(data, key, padding_func):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = padding_func(data, DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data)

# DES decryption function
def des_decrypt(encrypted_data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
    return decrypted_data.rstrip(b'\x00')

# Example usage
key = b'12345678' # 8-byte key for DES
data = b'This is a secret message.'
# Encrypt with PKCS#7 padding
encrypted_data_pkcs7 = des_encrypt(data, key, pkcs7_pad)
print("Encrypted with PKCS#7 padding:", encrypted_data_pkcs7)
# Decrypt with PKCS#7 padding
decrypted_data_pkcs7 = des_decrypt(encrypted_data_pkcs7, key)
print("Decrypted with PKCS#7 padding:", decrypted_data_pkcs7.decode())
# Encrypt with zero padding
encrypted_data_zero = des_encrypt(data, key, zero_pad)
print("Encrypted with zero padding:", encrypted_data_zero)
# Decrypt with zero padding
decrypted_data_zero = des_decrypt(encrypted_data_zero, key)
print("Decrypted with zero padding:", decrypted_data_zero.decode())