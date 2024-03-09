from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib
import binascii


def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, DES.block_size)


# Get the ciphertext and key from the user
ciphertext = input("Enter the ciphertext in hexadecimal format: ")
password = input("Enter the key: ")


# Hash the password to generate the key
key = hashlib.sha256(password.encode()).digest()[:8]


# Convert the ciphertext from hexadecimal to bytes
ciphertext = binascii.unhexlify(ciphertext)


# Decrypt the ciphertext
plaintext = decrypt(ciphertext, key)


# Print the decrypted plaintext
print("Decrypted plaintext:", plaintext.decode())