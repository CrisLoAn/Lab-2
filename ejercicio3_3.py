# Sample data
sample_data = b'Este en un mensaje de prueba'
# Encryption and decryption tests
def encryption_decryption_test(data, key):
    print("Original data:", data.decode())
    # Encrypt with PKCS#7 padding
    encrypted_data_pkcs7 = des_encrypt(data, key, pkcs7_pad)
    print("Encrypted with PKCS#7 padding:", encrypted_data_pkcs7)
    decrypted_data_pkcs7 = des_decrypt(encrypted_data_pkcs7, key)
    print("Decrypted with PKCS#7 padding:",
    decrypted_data_pkcs7.decode())
    # Encrypt with zero padding
    encrypted_data_zero = des_encrypt(data, key, zero_pad)
    print("Encrypted with zero padding:", encrypted_data_zero)
    decrypted_data_zero = des_decrypt(encrypted_data_zero, key)
    print("Decrypted with zero padding:", decrypted_data_zero.decode())
    print()
# Perform tests
key = b'12345678' # 8-byte key for DES
print("Encryption and Decryption Tests with Sample Data:")
encryption_decryption_test(sample_data, key)