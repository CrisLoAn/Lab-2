from Crypto.Cipher import ChaCha20
from binascii import unhexlify


# Clave y nonce en hexadecimal
nonce_hex = "0000000000000000"
key_hex = "717765727479"
key = bytes.fromhex(key_hex)
key += b'\x00' * (32 - len(key))


# Verificar si la clave es de longitud correcta (32 bytes)
if len(key) != 32:
    raise ValueError("La clave debe tener 32 bytes de longitud")


# Convertir el nonce de hexadecimal a bytes
nonce = unhexlify(nonce_hex)


# Texto cifrado en hexadecimal (ejemplo)
cipher_text_hex = input("Ingrese el texto a descifrar: ")


# Crear el objeto ChaCha20
cipher = ChaCha20.new(key=key, nonce=nonce)


# Convertir el texto cifrado de hexadecimal a bytes
cipher_text = unhexlify(cipher_text_hex)


# Descifrar el texto
decipher_text = cipher.decrypt(cipher_text)


try:
    # Mostrar el texto descifrado en hexadecimal
    print("Texto descifrado en hexadecimal:", decipher_text.decode())


except Exception as e:
    print("Ocurrió un error:", e)