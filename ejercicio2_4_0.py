from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def encrypt_with_padding(message, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    # Pad the message
    pad_length = 16 - (len(message) % 16)
    padded_message = message + bytes([pad_length]) * pad_length
    # Encrypt the padded message
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(ciphertext)

def decrypt_with_padding(ciphertext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    # Decrypt the ciphertext
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    # Unpad the decrypted message
    pad_length = decrypted_message[-1]
    unpadded_message = decrypted_message[:-pad_length]
    return unpadded_message

# Sample data
message = b"This is a secret message to be encrypted!"
key = b"supersecretkey12" # 256-bit key
iv = b"random_iv_123456" # Change the length of the IV to 16 bytes
# Encryption and decryption tests
print("Original message:", message)

# Encrypt the message using AES with CBC mode and various padding schemes
for padding_scheme in ['PKCS7', 'ANSIX923', 'ISO7816-4', 'ZeroPadding']:
    print("\nPadding Scheme:", padding_scheme)
    ciphertext = encrypt_with_padding(message, key, iv)
    print("Encrypted message:", ciphertext)
    decrypted_message = decrypt_with_padding(base64.b64decode(ciphertext),
    key, iv)
    print("Decrypted message:", decrypted_message.decode())