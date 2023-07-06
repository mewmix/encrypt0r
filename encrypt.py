from cryptography.fernet import Fernet
import os

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    key_file_path = file_path + '.key'
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

# Generate a random encryption key
key = Fernet.generate_key()

# Encrypt a file
file_path = 'vault/file.txt'
encrypt_file(file_path, key)

