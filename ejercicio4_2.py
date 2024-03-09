from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import hashlib

def encrypt(plaintext, key, mode):
    method = algorithms.TripleDES(key)
    cipher = Cipher(method, mode, backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def pad(data, size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

plaintext = input("Introduce el texto plano: ")
password = input("Introduce la clave (debe ser de 8 bytes para DES64): ")
key = hashlib.sha256(password.encode()).digest()[:8]

print("Texto plano:", plaintext)

plaintext = pad(plaintext.encode())

ciphertext = encrypt(plaintext, key, modes.ECB())
print("Cifrado (ECB):", ciphertext.hex())