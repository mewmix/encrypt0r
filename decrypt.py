from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path, _ = os.path.splitext(encrypted_file_path)
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Load the encryption key from the key file
key_file_path = 'vault/file.txt.key'
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()

# Decrypt the file
encrypted_file_path = 'vault/file.txt.encrypted'
decrypt_file(encrypted_file_path, key)

