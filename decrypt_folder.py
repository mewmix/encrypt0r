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

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    file_path = encrypted_file_path[:-10]  # Remove the '.encrypted' extension
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    key_file_path = file_path + '.key'
    os.remove(key_file_path)  # Remove the key file

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.encrypted'):
                encrypted_file_path = os.path.join(root, file_name)
                decrypt_file(encrypted_file_path, key)

# Generate or provide the encryption key
key = b'<your-encryption-key>'

# Decrypt a folder and its contents
folder_path = 'vault'
decrypt_folder(folder_path, key)
