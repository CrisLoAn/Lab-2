from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes, hmac
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import os

# Generate a private key for use in the exchange.
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())

# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key and
# get a public key from that. Note that in a DH handshake both peers
# must agree on a common set of parameters.
peer_public_key = ec.generate_private_key(ec.SECP256R1(), default_backend()).public_key()

shared_key = private_key.exchange(ec.ECDH(), peer_public_key)

# Perform key derivation.
derived_key = hashlib.sha256(shared_key).digest()

# Encrypt the message.
nonce = os.urandom(16)
algorithm = algorithms.ChaCha20(derived_key, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message")

print("Ciphertext:", ct)

# Decrypt the message.
algorithm = algorithms.ChaCha20(derived_key, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
decryptor = cipher.decryptor()
pt = decryptor.update(ct)

print("Decrypted plaintext:", pt)
