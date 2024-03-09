def initialize(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keystream(S, length):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])
    return bytes(keystream)

def rc4_encrypt(key, plaintext):
    S = initialize(key)
    keystream = generate_keystream(S, len(plaintext))
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream)])
    return ciphertext

def rc4_decrypt(key, ciphertext):
    return rc4_encrypt(key, ciphertext)  # RC4 decryption is the same as encryption

def main():
    key = input("Enter the key: ").encode()
    plaintext = input("Enter the plaintext: ").encode()

    ciphertext = rc4_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext.hex())

    decrypted_text = rc4_decrypt(key, ciphertext)
    print("Decrypted plaintext:", decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()
