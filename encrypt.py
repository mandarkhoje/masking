from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
# Key generation
key = os.urandom(32) # AES-256 requires a 256-bit key
# Initialization vector
iv = os.urandom(16)
# Encrypt
def encrypt_data(key, iv, plaintext):
 # Create an encryptor object
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
 encryptor = cipher.encryptor()
 # Pad the plaintext to be a multiple of the block size
 padder = padding.PKCS7(128).padder()
 padded_data = padder.update(plaintext.encode()) + padder.finalize()
 # Encrypt the padded plaintext
 ciphertext = encryptor.update(padded_data) + encryptor.finalize()
 return ciphertext
# Decrypt
def decrypt_data(key, iv, ciphertext):
 # Create a decryptor object
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
 decryptor = cipher.decryptor()
 # Decrypt the ciphertext
 padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
 # Unpad the plaintext
 unpadder = padding.PKCS7(128).unpadder()
 plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
 return plaintext.decode()
# Example usage
original_data = 'Sensitive Information'
ciphertext = encrypt_data(key, iv, original_data)
print(f'Ciphertext: {ciphertext}')
decrypted_data = decrypt_data(key, iv, ciphertext)
print(f'Decrypted Data: {decrypted_data}')
