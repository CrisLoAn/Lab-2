from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii


def aes_ecb_decrypt(ciphertext, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()


    # Desencriptar el texto cifrado
    decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()


    # Remover el relleno CMS (PKCS7)
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()


    return plaintext


# Función para generar una clave de 256 bits a partir de la clave en texto plano
def generate_key(password):
    hashed_password = hashlib.sha256(password).digest()
    return hashed_password


# Ejemplo de uso:
ciphertext = binascii.unhexlify(b"d8f11e13d25771e83898efdbad0e522c")
encryption_key_plain = b"123456"
encryption_key = generate_key(encryption_key_plain)  # Convertir la clave de texto plano a una clave de bytes
plaintext = aes_ecb_decrypt(ciphertext, encryption_key)
print("Plaintext:", plaintext.decode())